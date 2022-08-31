from django.db import models


class Schedule(models.Model):
    title = models.CharField(max_length=200, verbose_name='Расписание')
    image = models.ImageField(upload_to='schedule', verbose_name='фотография расписания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Расписание богослужений'
        verbose_name_plural = 'Расписание богослужений'


class PoorhousePeople(models.Model):
    name = models.CharField(max_length=80, verbose_name='Имя')
    text = models.TextField(verbose_name='История человека')
    image = models.ImageField(upload_to='poorhouse', verbose_name='Фотография подопечного')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подопечный богодельни'
        verbose_name_plural = 'Подопечные богодельни'
