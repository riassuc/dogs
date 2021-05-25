from django.urls import path
from .views      import ActorList, MovieList

urlpatterns = [
    path('/actors', ActorList.as_view()),
    path('/movies', MovieList.as_view()),
]
