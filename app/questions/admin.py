from django.contrib import admin

from .models import Choice, Participant, ParticipantAnswer, Question, QuizAttempt

admin.site.register(Choice)
admin.site.register(Participant)
admin.site.register(ParticipantAnswer)
admin.site.register(Question)
admin.site.register(QuizAttempt)
