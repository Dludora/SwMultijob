# publish/views.py
import os
import re

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from backend.models import Author, Article,FileInArticle
from stars.models import Stars,Follow
from comment_like.models import Comments,Likes
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from jwt import PyJWT
import hashlib
from django.utils import timezone
import pytz


class TK:
    secretKey = "a kEy@混入中文?"

    def getTimeNum(strIn):
        Y = (int)(strIn[0:4])
        M = (int)(strIn[5:7])
        D = (int)(strIn[8:10])
        h = (int)(strIn[11:13])
        m = (int)(strIn[14:16])
        s = (int)(strIn[17:19])
        ans = (Y - 1) * 365 + ((int)((Y - 1) / 4)) - ((int)((Y - 1) / 100)) + ((int)((Y - 1) / 400)) - 730000
        ans = ans + (M - 1) * 30
        if M > 2 and Y % 4 == 0 and (Y % 100 != 0 or Y % 400 == 0):
            ans = ans + 1
        elif M == 2 or M == 6 or M == 7:
            ans = ans + 1
        elif M == 3:
            ans = ans - 1
        elif M == 8:
            ans = ans + 2
        elif M == 9 or M == 10:
            ans = ans + 3
        elif M == 11 or M == 12:
            ans = ans + 4
        ans = ans + D
        ans = ans * 86400
        ans = ans + h * 3600 + m * 60 + s
        return ans

    def checkToken(token, isLogout):
        bytes_data = bytes(token, encoding='utf-8')
        decoded = PyJWT().decode(bytes_data, TK.secretKey, algorithms="HS256")
        id = None
        time = None
        for temp in decoded:
            if temp == 'userid':
                id = decoded[temp]
            elif temp == 'time':
                time = decoded[temp]
        if id is None or time is None:
            return -1
        try:
            user = Author.objects.get(id=id)
        except:
            return -3
        if user.lastLogin is None or user.lastLogin != time:
            return -4
        tz = pytz.timezone('Asia/Shanghai')
        now_time = (str)(timezone.now().astimezone(tz=tz))
        timediff = TK.getTimeNum(now_time) - TK.getTimeNum(time)
        if timediff > 24 * 60 * 60:
            return -2
        if isLogout == 1:
            user.lastLogin = None
            user.save()
        return id

    def check_token_return(token,isLogout):
        if token is None:
            return JsonResponse({'errno': 500, 'msg': "未找到令牌"})
        try:
            id = TK.checkToken(token, 0)
        except:
            return JsonResponse({'errno': 501, 'msg': "无效的令牌"})
        if id == -1:
            return JsonResponse({'errno': 501, 'msg': "无效的令牌"})
        if id == -2:
            return JsonResponse({'errno': 502, 'msg': "登录已过期"})
        if id == -3:
            return JsonResponse({'errno': 503, 'msg': "用户不存在"})
        if id == -4:
            return JsonResponse({'errno': 504, 'msg': "用户已注销或已在别处登录"})
        return id


@csrf_exempt  # 跨域设置
def register(request):  # 继承请求类
    if request.method == 'POST':  # 判断请求方式是否为 POST（此处要求为POST方式）
        username = request.POST.get('username')  # 获取请求体中的请求数据
        email = request.POST.get('email')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        if username is None or password_1 is None or password_2 is None or email is None:
            return JsonResponse({'errno': 2001, 'msg': "传入参数不足或错误"})
        if password_1 != password_2:  # 若两次输入的密码不同，则返回错误码errno和描述信息msg
            return JsonResponse({'errno': 1002, 'msg': "两次输入的密码不同"})
        for i in username:
            if not (i >= 'a' and i <= 'z') and not (i >= 'A' and i <= 'Z') and not (i >= '0' and i <= '9'):
                return JsonResponse({'errno': 1003, 'msg': "用户名不合法"})
        try:
            validate_email(email)
        except ValidationError:
            return JsonResponse({'errno': 1004, 'msg': "邮箱不合法"})
        try:
            user = Author.objects.get(email=email)
        except:
            None
        else:
            return JsonResponse({'errno': 1005, 'msg': "该邮箱已被注册过"})
        try:
            user = Author.objects.get(username=username)
        except:
            None
        else:
            return JsonResponse({'errno': 1006, 'msg': "该用户名已被使用"})
        numFlag = 0
        engFlag = 0
        len = 0
        for i in password_1:
            len = len + 1
            if i >= '0' and i <= '9':
                numFlag = 1
            elif (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
                engFlag = 1
        if numFlag == 0 or engFlag == 0 or len < 8 or len > 18:
            return JsonResponse({'errno': 1005, 'msg': "密码不合法"})
        # 新建 Author 对象，赋值用户名和密码并保存
        md5_str = hashlib.md5(password_1.encode()).hexdigest()
        new_author = Author(username=username, password=md5_str, email=email,avatar="user_img/default_img.png")
        new_author.save()  # 一定要save才能保存到数据库中
        return JsonResponse({'errno': 0, 'msg': "注册成功"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # 获取请求数据
        password = request.POST.get('password')
        if email is None or password is None:
            return JsonResponse({'errno': 2001, 'msg': "传入参数不足或错误"})
        try:
            author = Author.objects.get(email=email)
        except:
            return JsonResponse({'errno': 1002, 'msg': "用户名或密码错误"})
        md5_str = hashlib.md5(password.encode()).hexdigest()
        if author.password == md5_str:
            tz = pytz.timezone('Asia/Shanghai')
            now_time = timezone.now().astimezone(tz=tz)
            author.lastLogin = now_time
            author.save()
            encoded = PyJWT().encode({'userid': (str)(author.id), 'time': (str)(now_time)}, TK.secretKey,
                                     algorithm="HS256")
            files = FileInArticle.objects.filter(userId=author.id)
            for file in files:
                try:
                    os.remove(file.file.path)
                    print(file.file.path+" is removed")
                except:
                    None
                file.delete()
            if type(encoded) == type("str"):
                return JsonResponse({'errno': 0, 'msg': "登录成功", 'token': encoded})
            return JsonResponse({'errno': 0, 'msg': "登录成功", 'token': (str)(encoded, encoding='utf-8')})
        else:
            return JsonResponse({'errno': 1002, 'msg': "用户名或密码错误"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def logout(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    token = request.POST.get('token')
    if token is None:
        return JsonResponse({'errno': 500, 'msg': "未找到令牌"})
    try:
        id = TK.checkToken(token, 1)
    except:
        return JsonResponse({'errno': 501, 'msg': "无效的令牌"})
    if id == -1:
        return JsonResponse({'errno': 501, 'msg': "无效的令牌"})
    if id == -2:
        return JsonResponse({'errno': 502, 'msg': "登录已过期"})
    if id == -3:
        return JsonResponse({'errno': 503, 'msg': "用户不存在"})
    if id == -4:
        return JsonResponse({'errno': 504, 'msg': "用户已注销或已在别处登录"})
    files = FileInArticle.objects.filter(userId=id)
    for file in files:
        try:
            os.remove(file.file.path)
            print(file.file.path + " is removed")
        except:
            None
        file.delete()
    return JsonResponse({'errno': 0, 'msg': "注销成功"})


@csrf_exempt
def getSelfInformation(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    token = request.POST.get('token')
    if token is None:
        return JsonResponse({'errno': 500, 'msg': "未找到令牌"})
    try:
        id = TK.checkToken(token, 0)

    except:
        print('-----try_failed-----')
        return JsonResponse({'errno': 501, 'msg': "无效的令牌"})
    if id == -1:
        return JsonResponse({'errno': 501, 'msg': "无效的令牌"})
    if id == -2:
        return JsonResponse({'errno': 502, 'msg': "登录已过期"})
    if id == -3:
        return JsonResponse({'errno': 503, 'msg': "用户不存在"})
    if id == -4:
        return JsonResponse({'errno': 504, 'msg': "用户已注销或已在别处登录"})
    user = Author.objects.get(id=id)
    username = user.username
    sex = user.sex
    if sex is None:
        sex = '未知'
        user.sex = '未知'
        user.save()
    birthday = user.birthday
    if birthday is None:
        birthday = ''
    email = user.email
    discription = user.discription
    if discription is None:
        discription = ''
    avatar = user.avatar
    if avatar is None:
        avatarAddr = ''
    else:
        avatarAddr = avatar.path
        avatarAddr = avatarAddr.split('\\')
        avatarAddr = avatarAddr[len(avatarAddr) - 1]
        avatarAddr = "http://127.0.0.1:8000/files/user_img/" + avatarAddr
    return JsonResponse(
        {'errno': 0, 'msg': "获取信息成功", 'username': username, 'email': email, 'sex': sex, 'birthday': birthday,
         'discription': discription, 'avatar': avatarAddr})


@csrf_exempt
def setSelfUsername(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    token = request.POST.get('token')
    if token is None:
        return JsonResponse({'errno': 500, 'msg': "未找到令牌"})
    try:
        id = TK.checkToken(token, 0)
    except:
        return JsonResponse({'errno': 501, 'msg': "无效的令牌"})
    if id == -1:
        return JsonResponse({'errno': 501, 'msg': "无效的令牌"})
    if id == -2:
        return JsonResponse({'errno': 502, 'msg': "登录已过期"})
    if id == -3:
        return JsonResponse({'errno': 503, 'msg': "用户不存在"})
    if id == -4:
        return JsonResponse({'errno': 504, 'msg': "用户已注销或已在别处登录"})
    user = Author.objects.get(id=id)
    username = request.POST.get('username')
    if username is None or username == '':
        return JsonResponse({'errno': 1002, 'msg': "用户名不能为空"})
    for i in username:
        if not (i >= 'a' and i <= 'z') and not (i >= 'A' and i <= 'Z') and not (i >= '0' and i <= '9'):
            return JsonResponse({'errno': 1003, 'msg': "用户名不合法"})
    try:
        temp = Author.objects.get(username=username)
    except:
        None
    else:
        return JsonResponse({'errno': 1004, 'msg': "该用户名已被使用"})
    user.username = username
    user.save()
    return JsonResponse({'errno': 0, 'msg': "昵称修改成功"})


@csrf_exempt
def setSelfEmail(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    token = request.POST.get('token')
    if token is None:
        return JsonResponse({'errno': 500, 'msg': "未找到令牌"})
    try:
        id = TK.checkToken(token, 0)
    except:
        return JsonResponse({'errno': 501, 'msg': "无效的令牌"})
    if id == -1:
        return JsonResponse({'errno': 501, 'msg': "无效的令牌"})
    if id == -2:
        return JsonResponse({'errno': 502, 'msg': "登录已过期"})
    if id == -3:
        return JsonResponse({'errno': 503, 'msg': "用户不存在"})
    if id == -4:
        return JsonResponse({'errno': 504, 'msg': "用户已注销或已在别处登录"})
    user = Author.objects.get(id=id)
    email = request.POST.get('email')
    if email is None or email == '':
        return JsonResponse({'errno': 1002, 'msg': "邮箱不能为空"})
    try:
        validate_email(email)
    except ValidationError:
        return JsonResponse({'errno': 1003, 'msg': "邮箱不合法"})
    try:
        temp = Author.objects.get(email=email)
    except:
        None
    else:
        return JsonResponse({'errno': 1004, 'msg': "该邮箱已被注册"})
    user.email = email
    user.save()
    return JsonResponse({'errno': 0, 'msg': "邮箱修改成功"})


@csrf_exempt
def setSelfSex(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    token = request.POST.get('token')
    if token is None:
        return JsonResponse({'errno': 500, 'msg': "未找到令牌"})
    try:
        id = TK.checkToken(token, 0)
    except:
        return JsonResponse({'errno': 501, 'msg': "无效的令牌"})
    if id == -1:
        return JsonResponse({'errno': 501, 'msg': "无效的令牌"})
    if id == -2:
        return JsonResponse({'errno': 502, 'msg': "登录已过期"})
    if id == -3:
        return JsonResponse({'errno': 503, 'msg': "用户不存在"})
    if id == -4:
        return JsonResponse({'errno': 504, 'msg': "用户已注销或已在别处登录"})
    user = Author.objects.get(id=id)
    sex = request.POST.get('sex')
    if sex is None or sex == '':
        return JsonResponse({'errno': 1002, 'msg': "性别不能为空"})
    if sex != '男' and sex != '女' and sex != '未知':
        return JsonResponse({'errno': 1003, 'msg': "传入的性别异常"})
    user.sex = sex
    user.save()
    return JsonResponse({'errno': 0, 'msg': "性别修改成功"})


@csrf_exempt
def setSelfBirthday(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    token = request.POST.get('token')
    if token is None:
        return JsonResponse({'errno': 500, 'msg': "未找到令牌"})
    try:
        id = TK.checkToken(token, 0)

    except:
        return JsonResponse({'errno': 501, 'msg': "无效的令牌"})
    if id == -1:
        return JsonResponse({'errno': 501, 'msg': "无效的令牌"})
    if id == -2:
        return JsonResponse({'errno': 502, 'msg': "登录已过期"})
    if id == -3:
        return JsonResponse({'errno': 503, 'msg': "用户不存在"})
    if id == -4:
        return JsonResponse({'errno': 504, 'msg': "用户已注销或已在别处登录"})
    user = Author.objects.get(id=id)
    birthday = request.POST.get('birthday')
    if birthday is None:
        return JsonResponse({'errno': 1002, 'msg': "未传入生日"})
    if birthday == '':
        user.birthday = None
    else:
        user.birthday = birthday
    user.save()
    return JsonResponse({'errno': 0, 'msg': "生日修改成功"})


@csrf_exempt
def setSelfDiscription(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    token = request.POST.get('token')
    if token is None:
        return JsonResponse({'errno': 500, 'msg': "未找到令牌"})
    try:
        id = TK.checkToken(token, 0)
    except:
        return JsonResponse({'errno': 501, 'msg': "无效的令牌"})
    if id == -1:
        return JsonResponse({'errno': 501, 'msg': "无效的令牌"})
    if id == -2:
        return JsonResponse({'errno': 502, 'msg': "登录已过期"})
    if id == -3:
        return JsonResponse({'errno': 503, 'msg': "用户不存在"})
    if id == -4:
        return JsonResponse({'errno': 504, 'msg': "用户已注销或已在别处登录"})
    user = Author.objects.get(id=id)
    discription = request.POST.get('discription')
    if discription is None:
        return JsonResponse({'errno': 1002, 'msg': "未传入个人简介"})
    if discription == '':
        user.discription = None
    else:
        if len(discription) > 100:
            return JsonResponse({'errno': 1003, 'msg': "简介长度过大"})
        user.discription = discription
    user.save()
    return JsonResponse({'errno': 0, 'msg': "个人简介修改成功"})
@csrf_exempt
def setSelfAvatar(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    token = request.POST.get('token')
    if token is None:
        return JsonResponse({'errno': 500, 'msg': "未找到令牌"})
    try:
        id = TK.checkToken(token, 0)
    except:
        return JsonResponse({'errno': 501, 'msg': "无效的令牌"})
    if id == -1:
        return JsonResponse({'errno': 501, 'msg': "无效的令牌"})
    if id == -2:
        return JsonResponse({'errno': 502, 'msg': "登录已过期"})
    if id == -3:
        return JsonResponse({'errno': 503, 'msg': "用户不存在"})
    if id == -4:
        return JsonResponse({'errno': 504, 'msg': "用户已注销或已在别处登录"})
    user=Author.objects.get(id=id)
    avatar=request.FILES.get('avatar')
    if avatar is None:
        return JsonResponse({'errno': 1002, 'msg': "未传入头像"})
    oldAvatar=user.avatar
    try:
        user.avatar=avatar
        user.save()
    except:
        return JsonResponse({'errno': 1002, 'msg': "头像上传失败"})
    if oldAvatar is not None and oldAvatar!="user_img/default_img.png":
        try:
            os.remove(oldAvatar.path)
        except:
            None
    return JsonResponse({'errno': 0, 'msg': "头像修改成功"})
@csrf_exempt
def addFile(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    token = request.POST.get('token')
    userId = TK.check_token_return(token, 0)
    if not isinstance(userId, str):
        return userId
    file=request.FILES.get('file')
    if file is None:
        return JsonResponse({'errno': 1002, 'msg': "未传入文件"})
    new_file=FileInArticle(file=file,userId=userId)
    articleId=request.POST.get('articleId')
    if articleId is not None:
        new_file.articleId=articleId
    else:
        new_file.articleId=None
    new_file.save()
    Addr = new_file.file.path
    Addr = Addr.split('\\')
    Addr = Addr[len(Addr) - 1]
    Addr = "http://127.0.0.1:8000/files/article_file/"+Addr
    new_file.url=Addr
    new_file.save()
    return JsonResponse({'errno': 0, 'msg': "上传成功","url":Addr})
@csrf_exempt
def publish(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    token = request.POST.get('token')
    userId = TK.check_token_return(token, 0)
    if not isinstance(userId, str):
        return userId
    user = Author.objects.get(id=userId)
    title=request.POST.get('title')
    body=request.POST.get('body')
    label=request.POST.get('label')
    if title is None or body is None or label is None:
        return JsonResponse({'errno': 1002, 'msg': "传入参数不足"})
    if title=="" or body=="":
        return JsonResponse({'errno': 1003, 'msg': "标题和正文内容不能为空"})
    if len(title)>100:
        return JsonResponse({'errno': 1004, 'msg': "文章标题过长"})
    discription=request.POST.get('discription')
    if discription is not None and len(discription)>100:
        return JsonResponse({'errno': 1005, 'msg': "文章简介过长"})
    elif discription is None:
        discription=""
    articleId=request.POST.get('articleId')
    if articleId is not None and articleId!="" and articleId!="-1":
        try:
            article=Article.objects.get(id=articleId)
        except:
            return JsonResponse({'errno': 1006, 'msg': "文章不存在"})
        if article.publisher_id!=user.id:
            return JsonResponse({'errno': 1007, 'msg': "修改者不是发布者"})
        article.title=title
        article.body=body
        article.label=label
        article.discription=discription
        article.save()
        files = FileInArticle.objects.filter(articleId=articleId)
        for file in files:
            if re.search(file.url,body) is not None:
                file.userId=None
                file.save()
            else:
                try:
                    os.remove(file.file.path)
                    print(file.file.path+" is removed")
                except:
                    None
                file.delete()
        return JsonResponse({'errno': 0, 'msg': "文章修改成功",'articleId':article.id})
    else:
        article=Article(title=title,body=body,label=label,discription=discription,publisher=user)
        article.save()
        files = FileInArticle.objects.filter(userId=userId)
        for file in files:
            if re.search(file.url,body) is not None:
                file.userId=None
                file.articleId=article.id
                file.save()
        return JsonResponse({'errno': 0, 'msg': "文章发布成功",'articleId':article.id})
@csrf_exempt
def getEdit(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    token = request.POST.get('token')
    userId = TK.check_token_return(token, 0)
    if not isinstance(userId, str):
        return userId
    user = Author.objects.get(id=userId)
    articleId = request.POST.get('articleId')
    if articleId is None or articleId=="":
        return JsonResponse({'errno': 1002, 'msg': "articleId不能为空"})
    try:
        article = Article.objects.get(id=articleId)
    except:
        return JsonResponse({'errno': 1003, 'msg': "文章不存在"})
    if article.publisher_id!=user.id:
        return JsonResponse({'errno': 1004, 'msg': "不能修改非本人所写文章"})
    labels=article.label.split(',')
    label=[]
    for lb in labels:
        label.append(lb)
    return JsonResponse({'errno': 0, 'msg': "信息获取成功",'title':article.title,'body':article.body,'label':label,'discription':article.discription})
@csrf_exempt
def deleteArticle(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    token = request.POST.get('token')
    userId = TK.check_token_return(token, 0)
    if not isinstance(userId, str):
        return userId
    user = Author.objects.get(id=userId)
    articleId = request.POST.get('articleId')
    if articleId is None or articleId=="":
        return JsonResponse({'errno': 1002, 'msg': "articleId不能为空"})
    try:
        article = Article.objects.get(id=articleId)
    except:
        return JsonResponse({'errno': 1003, 'msg': "文章不存在"})
    if article.publisher_id!=user.id:
        return JsonResponse({'errno': 1004, 'msg': "不能删除非本人所写文章"})
    files = FileInArticle.objects.filter(articleId=articleId)
    for file in files:
        try:
            os.remove(file.file.path)
            print(file.file.path + " is removed")
        except:
            None
        file.delete()
    likes=Likes.objects.filter(articleId=articleId)
    for like in likes:
        like.delete()
    stars=Stars.objects.filter(articleId=articleId)
    for star in stars:
        star.delete()
    comments=Comments.objects.filter(articleId=articleId)
    for comment in comments:
        comment.delete()
    article.delete()
    return JsonResponse({'errno': 0, 'msg': "删除成功"})
@csrf_exempt
def readArticle(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    token = request.POST.get('token')
    userId = TK.check_token_return(token, 0)
    if not isinstance(userId, str):
        return userId
    articleId = request.POST.get('articleId')
    if articleId is None or articleId=="":
        return JsonResponse({'errno': 1002, 'msg': "articleId不能为空"})
    try:
        article = Article.objects.get(id=articleId)
    except:
        return JsonResponse({'errno': 1003, 'msg': "文章不存在"})
    user=Author.objects.get(id=article.publisher_id)
    discription=article.discription
    if discription is None:
        discription=""
    likes=article.likes
    commentnum=article.commentsCount
    stars=len(Stars.objects.filter(articleId=articleId))
    follows=len(Follow.objects.filter(followId=user.id))
    avatarAddr = user.avatar.path
    avatarAddr = avatarAddr.split('\\')
    avatarAddr = avatarAddr[len(avatarAddr) - 1]
    avatarAddr = "http://127.0.0.1:8000/files/user_img/" + avatarAddr
    comments = Comments.objects.filter(articleId=articleId)
    comments = comments.values()
    comment_list = []
    for c in comments:
        dic = {}
        comment=Comments.objects.get(id=c['id'])
        dic['comment'] = c['comment']
        author = Author.objects.get(id=comment.userId)
        dic['username'] = author.username
        # print(dic)
        comment_list.append(dic)
    try:
        like=Likes.objects.get(userId=userId,articleId=articleId)
        isLiked=1
    except:
        isLiked=0
    try:
        follow=Follow.objects.get(userId=userId,followId=user.id)
        isFollowed=1
    except:
        isFollowed=0
    try:
        star=Stars.objects.get(userId=userId,articleId=articleId)
        isStared=1
    except:
        isStared=0
    labels = article.label.split(',')
    label = []
    for lb in labels:
        label.append(lb)
    return JsonResponse({'errno': 0, 'msg': "查询成功",'title':article.title,'body':article.body,'label':label,
                         'discription':discription,'authorId':user.id,'likes':likes,'commentnum':commentnum,
                         'stars':stars,'follows':follows,'avatarAddr':avatarAddr,'comment_list':comment_list,
                         'authorName':user.username,"isLiked":isLiked,"isFollowed":isFollowed,"isStared":isStared})
@csrf_exempt
def getOtherInformation(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
    token = request.POST.get('token')
    if token is not None and token!="":
        userId = TK.check_token_return(token, 0)
        if not isinstance(userId, str):
            return userId
    authorId = request.POST.get('authorId')
    if authorId is None or authorId=="":
        return JsonResponse({'errno': 1002, 'msg': "authorId不能为空"})
    try:
        author = Author.objects.get(id=authorId)
    except:
        return JsonResponse({'errno': 1003, 'msg': "该用户不存在"})
    try:
        follow=Follow.objects.get(userId=userId,followId=author.id)
        isFollowed=1
    except:
        isFollowed=0
    follows=len(Follow.objects.filter(followId=author.id))
    avatarAddr = author.avatar.path
    avatarAddr = avatarAddr.split('\\')
    avatarAddr = avatarAddr[len(avatarAddr) - 1]
    avatarAddr = "http://127.0.0.1:8000/files/user_img/" + avatarAddr
    blogs = Article.objects.filter(publisher_id=author)
    blogs = blogs.values()
    blog_list = []
    for blog in blogs:
        dic = {}
        dic['title'] = blog['title']
        dic['discription'] = blog['discription']
        # print(dic)
        blog_list.append(dic)
    return JsonResponse({'errno': 0, 'msg': "查询成功",'username':author.username,'avatarAddr':avatarAddr,
                         'sex':author.sex,'birthday':author.birthday,'discription':author.discription,
                         'email':author.email,'follows':follows,'isFollowed':isFollowed,'blogs':blog_list})