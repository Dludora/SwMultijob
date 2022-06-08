from django.shortcuts import render

# Create your views here.
import time
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from backend.models import Author, Article
from stars.models import Stars, Follow, History
from comment_like.models import Comments, Likes
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from jwt import PyJWT
import hashlib
from django.utils import timezone
import pytz

from backend.views import TK


################################# comment #################################
@csrf_exempt
def addComment(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    articleId = request.POST.get('articleId')
    token = request.POST.get('token')
    content = request.POST.get('content')

    # userId = request.POST.get('id')  ####
    userId = TK.check_token_return(token, 0)
    if not isinstance(userId, str):
        return userId

    new_comment = Comments(articleId=articleId, userId=userId, comment=content)
    new_comment.save()
    article = Article.objects.get(id=articleId)
    article.commentsCount += 1
    article.save()
    return JsonResponse({'errno': 0, 'msg': "评论发表成功", 'commentId': new_comment.id})


@csrf_exempt
def delComment(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    commentId = request.POST.get('commentId')
    token = request.POST.get('token')

    # userId = request.POST.get('id')  ####
    userId = TK.check_token_return(token, 0)
    if not isinstance(userId, str):
        return userId
    comment = Comments.objects.get(id=commentId)
    article = Article.objects.get(id=comment.articleId)
    article.commentsCount -= 1
    article.save()
    comment.delete()


    return JsonResponse({'errno': 0, 'msg': "评论删除成功"})


################################# like #################################
@csrf_exempt
def addLike(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    articleId = request.POST.get('articleId')
    token = request.POST.get('token')

    # userId = request.POST.get('id')  ####
    userId = TK.check_token_return(token, 0)
    if not isinstance(userId, str):
        return userId

    new_like = Likes(articleId=articleId, userId=userId)
    new_like.save()
    article = Article.objects.get(id=articleId)
    article.likes += 1
    article.save()
    return JsonResponse({'errno': 0, 'msg': "点赞成功"})


@csrf_exempt
def delLike(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    articleId = request.POST.get('articleId')
    token = request.POST.get('token')

    # userId = request.POST.get('id')  ####
    userId = TK.check_token_return(token, 0)
    if not isinstance(userId, str):
        return userId

    like = Likes.objects.get(articleId=articleId, userId=userId)
    like.delete()
    article = Article.objects.get(id=articleId)
    article.likes -= 1
    article.save()
    return JsonResponse({'errno': 0, 'msg': "取消点赞成功"})
