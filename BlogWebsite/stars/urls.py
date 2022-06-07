# publish/urls.py
from django.urls import path
from .views import *
urlpatterns = [
    path('addStars',addStars),
    path('get_all_star_article',get_all_star_article),
    path('delStars',delStars),
    path('addFollow',addFollow),
    path('delFollow',delFollow),
    path('addFollow',addFollow),
    path('get_follow_list',get_follow_list),
    path('addHistory',addHistory),
    path('get_history_list',get_history_list),
]