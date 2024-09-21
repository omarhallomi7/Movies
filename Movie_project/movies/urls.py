# movies/urls.py
from django.urls import path
from . import views

#app name
app_name = 'movies' 

urlpatterns = [
    path('', views.movie_list, name='list'), # path for movies list
    path('<slug:slug>/', views.movie_detail, name='movie_detail'), # path for specific movie that includes all movie detail
    path('<slug:slug>/submit_review/', views.submit_review, name='submit_review'), # path for submitting review for logged in users
]
