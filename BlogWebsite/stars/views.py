from django.shortcuts import render

# Create your views here.
import time
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from backend.models import Author, Article
from stars.models import Stars, Follow, History
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from jwt import PyJWT
import hashlib
from django.utils import timezone
import pytz

from backend.views import TK


################################# star #################################
@csrf_exempt
def addStars(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    articleId = request.POST.get('articleId')
    token = request.POST.get('token')
    # userId = request.POST.get('id')  ####
    userId = TK.check_token_return(token, 0)
    if not isinstance(userId, str):
        return userId

    new_star = Stars(articleId=articleId, userId=userId)
    try:
        new_star.save()
        return JsonResponse({'errno': 0, 'msg': "添加收藏成功"})
    except:
        return JsonResponse({'errno': 1002, 'msg': "文章已收藏过"})


@csrf_exempt
def delStars(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    articleId = request.POST.get('articleId')
    token = request.POST.get('token')

    # userId = request.POST.get('id')  ####
    userId = TK.check_token_return(token, 0)
    if not isinstance(userId, str):
        return userId

    star = Stars.objects.get(userId=userId, articleId=articleId)
    star.delete()
    return JsonResponse({'errno': 0, 'msg': "取消收藏成功"})


@csrf_exempt
def get_all_star_article(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    token = request.POST.get('token')
    # userId = request.POST.get('id')  ####
    userId = TK.check_token_return(token, 0)
    if not isinstance(userId, str):
        return userId
    stars = Stars.objects.filter(userId=userId)
    stars = stars.values()
    if len(stars) == 0:
        return JsonResponse({'errno': 1002, 'msg': '不存在收藏文章'})
    else:
        stars_list = []
        for s in stars:
            dic = {}
            dic['articleId'] = s['articleId']
            article = Article.objects.get(id=s['articleId'])
            dic['title'] = article.title
            author = Author.objects.get(id=article.publisher_id)
            dic['author'] = author.username
            # print(dic)
            stars_list.append(dic)
        return JsonResponse({'errno': 0, 'size': len(stars_list), 'stars_list': stars_list})


################################# history #################################
@csrf_exempt
def addHistory(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    articleId = request.POST.get('articleId')
    token = request.POST.get('token')
    # userId = request.POST.get('id')  ####
    userId = TK.check_token_return(token, 0)
    if not isinstance(userId, str):
        return userId
    try:
        history = History.objects.get(userId=userId, articleId=articleId)
        history.delete()
        new_history = History(userId=userId, articleId=articleId)
        history.save()
        return JsonResponse({'errno': 1, 'msg': "修改历史记录成功"})
    except:
        new_history = History(userId=userId, articleId=articleId)
        new_history.save()
        return JsonResponse({'errno': 0, 'msg': "添加历史记录成功"})


@csrf_exempt
def get_history_list(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    token = request.POST.get('token')
    # userId = request.POST.get('id')  ####
    userId = TK.check_token_return(token, 0)
    if not isinstance(userId, str):
        return userId
    history = History.objects.filter(userId=userId)
    history = history.values()
    print(history)
    if len(history) == 0:
        return JsonResponse({'errno': 1002, 'msg': '无历史记录'})
    else:
        history_list = []
        for s in history:
            dic = {}
            dic['articleId'] = s['articleId']
            article = Article.objects.get(id=s['articleId'])
            dic['title'] = article.title
            author = Author.objects.get(id=article.publisher_id)
            dic['author'] = author.username
            dic['time'] = s['time']
            # print(dic)
            history_list.append(dic)
        return JsonResponse({'errno': 0, 'size': len(history), 'history_list': history_list})


################################# follow #################################
@csrf_exempt
def addFollow(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    followId = request.POST.get('followId')
    token = request.POST.get('token')
    # userId = request.POST.get('id')  ####
    userId = TK.check_token_return(token, 0)
    if not isinstance(userId, str):
        return userId

    new_follow = Follow(userId=userId, followId=followId)
    try:
        new_follow.save()
        return JsonResponse({'errno': 0, 'msg': "关注成功"})
    except:
        return JsonResponse({'errno': 1002, 'msg': "已关注过该用户"})


@csrf_exempt
def delFollow(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    followId = request.POST.get('followId')
    token = request.POST.get('token')

    # userId = request.POST.get('id')  ####
    userId = TK.check_token_return(token, 0)
    if not isinstance(userId, str):
        return userId

    follow = Follow.objects.get(userId=userId, followId=followId)
    follow.delete()
    return JsonResponse({'errno': 0, 'msg': "取消关注成功"})


@csrf_exempt
def get_follow_list(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    token = request.POST.get('token')
    # userId = request.POST.get('id')  ####
    userId = TK.check_token_return(token, 0)
    if not isinstance(userId, str):
        return userId
    follows = Follow.objects.filter(userId=userId)
    follows = follows.values()
    print(follows)
    if len(follows) == 0:
        return JsonResponse({'errno': 1002, 'msg': ''})
    else:
        follows_list = []
        for f in follows:
            dic = {}
            dic['followId'] = f['followId']
            author = Author.objects.get(id=f['followId'])
            dic['followName'] = author.username
            avatar = author.avatar
            if avatar is None:
                avatarAddr = ''
            else:
                avatarAddr = avatar.path
                avatarAddr = avatarAddr.split('\\')
                avatarAddr = avatarAddr[len(avatarAddr) - 1]
                avatarAddr = "http://127.0.0.1:8000/files/user_img/" + avatarAddr
            dic['followAvatar'] = avatarAddr
            follows_list.append(dic)
        return JsonResponse({'errno': 0, 'size': len(follows), 'follows_list': follows_list})
