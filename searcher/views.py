from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Video


class VideoList(generic.ListView):
    model = Video
    paginate_by = 100
