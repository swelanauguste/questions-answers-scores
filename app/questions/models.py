from django.db import models
from django.urls import reverse


class Participant(models.Model):
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse("participant-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="choices"
    )
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class QuizAttempt(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    score = models.FloatField()
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("attempt-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.participant.name} - {self.score}"


class ParticipantAnswer(models.Model):
    attempt = models.ForeignKey(
        QuizAttempt, related_name="answers", on_delete=models.CASCADE
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, null=True, blank=True, on_delete=models.SET_NULL)
    is_correct = models.BooleanField()

    def get_absolute_url(self):
        return reverse("answer-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.attempt.participant.name} - {self.question.text} - {self.choice.text}"
