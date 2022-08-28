from django.urls import path

from core.views import ListSchedule

urlpatterns = [
    path('schedule/', ListSchedule.as_view()),
]
