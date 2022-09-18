from rest_framework import serializers
from .models import *


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class PoorhousePeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoorhousePeople
        fields = '__all__'


class TemplePhotogallerySerializer(serializers.ModelSerializer): # templephotogallery
    class Meta:
        model = TemplePhotogallery
        fields = '__all__'


class BelltowerPhotogallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = BelltowerPhotogallery
        fields = '__all__'


class PoorhousePhotogallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = PoorhousePhotogallery
        fields = '__all__'


class MercyBusPhotogallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = MercyBusPhotogallery
        fields = '__all__'


class MersyBusStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MersyBusStation
        fields = '__all__'