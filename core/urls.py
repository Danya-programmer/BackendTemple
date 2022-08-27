from django.urls import path

from core.views import ListSchedule

urlpatterns = [
    path('', ListSchedule.as_view()),
]
