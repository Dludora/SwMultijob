from django.urls import path
from .views import *

urlpatterns = [
    path('addComment', addComment),
    path('delComment', delComment),
    path('addLike', addLike),
    path('delLike', delLike),
    path('search', search),
    path('display', display),
    path('get_my_article',get_my_article),
]
