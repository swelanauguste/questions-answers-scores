import random
from datetime import datetime

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, ListView

from .models import Choice, Participant, ParticipantAnswer, Question, QuizAttempt


class QuizAttemptListView(ListView):
    model = QuizAttempt


class QuizAttemptDetailView(DetailView):
    model = QuizAttempt


class ParticipantListView(ListView):
    model = Participant


class ParticipantDetailView(DetailView):
    model = Participant


class HomeView(View):
    def get(self, request):
        return render(request, "home.html")

    def post(self, request):
        name = request.POST.get("name")
        if name:
            participant, created = Participant.objects.get_or_create(name=name)
            return redirect(reverse("quiz", args=[participant.id]))
        return render(request, "home.html")


class QuizView(View):
    def get_random_questions(self, count=10):
        questions = list(Question.objects.all())
        if len(questions) > count:
            questions = random.sample(questions, count)
        return questions

    def get(self, request, participant_id):
        participant = get_object_or_404(Participant, id=participant_id)
        questions = self.get_random_questions(10)
        request.session["question_ids"] = [question.id for question in questions]
        request.session["quiz_start_time"] = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        return render(
            request, "quiz.html", {"questions": questions, "participant": participant}
        )

    def post(self, request, participant_id):
        participant = get_object_or_404(Participant, id=participant_id)
        attempt = QuizAttempt.objects.create(participant=participant, score=0)

        score = 0
        question_ids = request.session.get("question_ids", [])
        questions = Question.objects.filter(id__in=question_ids)

        for question in questions:
            choice_id = request.POST.get(f"question_{question.id}")
            if choice_id:
                choice = get_object_or_404(Choice, id=choice_id)
                is_correct = choice.is_correct
                ParticipantAnswer.objects.create(
                    attempt=attempt,
                    question=question,
                    choice=choice,
                    is_correct=is_correct,
                )
                if is_correct:
                    score += 1
            else:
                ParticipantAnswer.objects.create(
                    attempt=attempt, question=question, choice=None, is_correct=False
                )

        attempt.score = score
        attempt.end_time = datetime.now()
        attempt.save()
        return redirect(reverse("result", args=[attempt.id]))


class ResultView(View):
    def get(self, request, attempt_id):
        attempt = get_object_or_404(QuizAttempt, id=attempt_id)
        answers = attempt.answers.all()
        return render(request, "result.html", {"attempt": attempt, "answers": answers})
