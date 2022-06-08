from django.urls import path
from .views import *
urlpatterns = [
    path('addComment',addComment),
    path('delComment',delComment),
    path('addLike',addLike),
    path('delLike',delLike),
]