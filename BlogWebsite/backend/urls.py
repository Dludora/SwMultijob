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
    path('setSelfAvatar', setSelfAvatar),  # 修改头像，传入avatar
    path('addImg', addImg), #上传文章所需图片，传入img，可选传入articleId
    path('publish', publish), #发布文章，传入title(标题)、body(正文)、label(标签)、discription(简介，可选)，
                              #若非初次发布，则需传入articleId
    path('getEdit', getEdit), #编辑文章前获取文章信息，传入articleId，传回title(标题)、body(正文)、label(标签)、discription(简介)
    path('deleteArticle', deleteArticle), #传入articleId，删除自己所写的文章
    path('readArticle', readArticle),
    path('getOtherInformation', getOtherInformation)  # 根据id获取其它人的信息，token可选
]