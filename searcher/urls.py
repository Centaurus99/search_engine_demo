from django.urls import path

from . import views

app_name = 'searcher'
urlpatterns = [
    path('', views.VideoList.as_view(), name='videolist'),
    path('up/', views.UpList.as_view(), name='uplist'),
    path('video/detail/<int:pk>/', views.VideoDetail.as_view(), name='video-detail'),
    path('up/detail/<int:pk>/', views.UpDetail.as_view(), name='up-detail'),
    path('video/search/', views.VideoSearch.as_view(), name='video-search'),
    path('up/search/', views.UpSearch.as_view(), name='up-search'),
]
