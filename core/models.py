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
        verbose_name = 'Подопечного богодельни'
        verbose_name_plural = 'Подопечные богодельни'


class TemplePhotogallery(models.Model):
    image = models.ImageField(upload_to='photogallery/temple', verbose_name='Фотография храма')

    def __str__(self):
        return 'Фотография храма'

    class Meta:
        verbose_name = 'Фотографию храма'
        verbose_name_plural = 'Фотографии храма'


class BelltowerPhotogallery(models.Model):
    image = models.ImageField(upload_to='photogallery/belltower', verbose_name='Фотография колокольни')

    def __str__(self):
        return 'Фотография колокольни'

    class Meta:
        verbose_name = 'Фотографию колокольни'
        verbose_name_plural = 'Фотографии колокольни'


class PoorhousePhotogallery(models.Model):
    image = models.ImageField(upload_to='photogallery/poorhouse', verbose_name='Фотография богадельни')

    def __str__(self):
        return 'Фотография богадельни'

    class Meta:
        verbose_name = 'Фотографию богадельни'
        verbose_name_plural = 'Фотографии богадельни'


class MercyBusPhotogallery(models.Model):
    image = models.ImageField(upload_to='photogallery/mercybus', verbose_name='Фотография автобуса милосердия')

    def __str__(self):
        return 'Фотография автобуса милосердия'

    class Meta:
        verbose_name = 'Фотографию автобуса милосердия'
        verbose_name_plural = 'Фотографии автобуса милосердия'