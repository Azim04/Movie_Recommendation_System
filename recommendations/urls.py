# recommendations\urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_movies, name='search_movies'),
    path('movie/<int:item_id>/', views.movie_detail, name='movie_detail'),  # Use 'int' to match integer parameter
]
