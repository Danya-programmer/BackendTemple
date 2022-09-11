from django.urls import path

from core.views import *

urlpatterns = [
    path('schedule/', ListSchedule.as_view()),
    path('poorhousepeople/', ListPoorhousePeople.as_view()),
    path('photogallery/temple', ListTemplePhotogallery.as_view()),
    path('photogallery/belltower', ListBelltowerPhotogallery.as_view()),
    path('photogallery/poorhouse', ListPoorhousePhotogallery.as_view()),
    path('photogallery/mersybus', ListMercyBusPhotogallery.as_view()),
]
