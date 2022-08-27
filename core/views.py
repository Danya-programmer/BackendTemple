from rest_framework import generics
from .models import Schedule
from .serializers import ScheduleSerializer


class ListSchedule(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer