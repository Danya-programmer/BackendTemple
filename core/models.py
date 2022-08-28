from django.db import models


class Schedule(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Расписание богослужений'
        verbose_name_plural = 'Расписание богослужений'