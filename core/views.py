from rest_framework import generics
from .models import Schedule, PoorhousePeople
from .serializers import ScheduleSerializer, PoorhousePeopleSerializer


class ListSchedule(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ListPoorhousePeople(generics.ListAPIView):
    queryset = PoorhousePeople.objects.all()
    serializer_class = PoorhousePeopleSerializer