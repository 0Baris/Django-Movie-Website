from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('home', views.home),
    path('movies', views.movies, name='movies'),
    path('movies/<int:id>', views.movie_details, name='movie_details'),
    path('category', views.home),
    path('category/<int:id>', views.category, name='category'),
]
