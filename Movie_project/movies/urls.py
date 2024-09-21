# movies/urls.py
from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name='list'),
    path('<slug:slug>/', views.movie_detail, name='movie_detail'),
    path('<slug:slug>/submit_review/', views.submit_review, name='submit_review'),
]
