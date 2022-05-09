from django.urls import path
from . import views


urlpatterns = [
    # route is a string contains a URL pattern
    path('movierecommender/',views.movie_recommendation_view, name='recommendations'),
    path('',views.list_of_movies.as_view(),name='movie'),
]
