from rest_framework import generics
from .models import *
from .serializers import *


class ListSchedule(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ListPoorhousePeople(generics.ListAPIView):
    queryset = PoorhousePeople.objects.all()
    serializer_class = PoorhousePeopleSerializer


class ListTemplePhotogallery(generics.ListAPIView):
    queryset = TemplePhotogallery.objects.all()
    serializer_class = TemplePhotogallerySerializer


class ListBelltowerPhotogallery(generics.ListAPIView):
    queryset = BelltowerPhotogallery.objects.all()
    serializer_class = BelltowerPhotogallerySerializer


class ListPoorhousePhotogallery(generics.ListAPIView):
    queryset = PoorhousePhotogallery.objects.all()
    serializer_class = PoorhousePhotogallerySerializer


class ListMercyBusPhotogallery(generics.ListAPIView):
    queryset = MercyBusPhotogallery.objects.all()
    serializer_class = MercyBusPhotogallerySerializer
