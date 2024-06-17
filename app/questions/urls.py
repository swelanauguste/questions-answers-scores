from django.urls import path

from .views import (
    HomeView,
    ParticipantDetailView,
    ParticipantListView,
    QuizAttemptDetailView,
    QuizAttemptListView,
    QuizView,
    ResultView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("quiz/<int:participant_id>/", QuizView.as_view(), name="quiz"),
    path("result/<int:attempt_id>/", ResultView.as_view(), name="result"),
    path("participants/", ParticipantListView.as_view(), name="participant-list"),
    path(
        "participant/detail/<int:pk>/",
        ParticipantDetailView.as_view(),
        name="participant-detail",
    ),
    path("attempt/", QuizAttemptListView.as_view(), name="attempt-list"),
    path(
        "attempt/detail/<int:pk>/",
        QuizAttemptDetailView.as_view(),
        name="attempt-detail",
    ),
]
