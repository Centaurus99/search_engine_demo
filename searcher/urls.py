from django.urls import path

from . import views

app_name = 'searcher'
urlpatterns = [
    path('', views.VideoList.as_view(), name='videolist'),
]
