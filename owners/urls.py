from django.urls import path
from .views      import OwnerAdd, DogAdd, OwnerList, DogList

urlpatterns = [
    path('/owner', OwnerAdd.as_view()),
    path('/dog', DogAdd.as_view()),
    path('/ownerlist', OwnerList.as_view()),
    path('/doglist', DogList.as_view()),
]
