from rest_framework import serializers
from .models import Schedule, PoorhousePeople


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class PoorhousePeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoorhousePeople
        fields = '__all__'