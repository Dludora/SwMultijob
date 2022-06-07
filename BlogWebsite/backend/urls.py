# publish/urls.py
from django.urls import path
from .views import *
urlpatterns = [
    path('register', register),
    path('login', login),#若登录后重新登录，原令牌失效
    path('logout', logout),#logout后，令牌失效
    path('getSelfInformation',getSelfInformation),#输入token，查询下面五种个人信息，下面的修改信息均需传入token
    path('setSelfUsername',setSelfUsername),#修改昵称，传入username
    path('setSelfEmail',setSelfEmail),#修改邮箱，传入email
    path('setSelfSex',setSelfSex),#修改性别，传入sex，只能是‘男’‘女’或‘未知’
    path('setSelfBirthday',setSelfBirthday),#修改生日，传入birthday
    path('setSelfDiscription',setSelfDiscription), #修改个人简介，传入discription
    path('getBlog',getBlog)
]