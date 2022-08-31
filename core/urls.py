from django.urls import path

from core.views import ListSchedule, ListPoorhousePeople

urlpatterns = [
    path('schedule/', ListSchedule.as_view()),
    path('poorhousepeople/', ListPoorhousePeople.as_view()),
]
