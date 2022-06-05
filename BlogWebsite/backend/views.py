# publish/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from backend.models import Author,Article   # 引入数据库 Author 对象
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
@csrf_exempt    # 跨域设置
def register(request):  # 继承请求类
    if request.method == 'POST':  # 判断请求方式是否为 POST（此处要求为POST方式）
        username = request.POST.get('username')  # 获取请求体中的请求数据
        email=request.POST.get('email')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        if username is None or password_1 is None or password_2 is None or email is None:
            return JsonResponse({'errno': 2001, 'msg': "传入参数不足或错误"})
        if password_1 != password_2:    # 若两次输入的密码不同，则返回错误码errno和描述信息msg
            return JsonResponse({'errno': 1002, 'msg': "两次输入的密码不同"})
        for i in username:
            if not(i>='a'and i<='z') and not(i>='A' and i<='Z') and not(i>='0' and i<='9'):
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
        numFlag=0
        engFlag=0
        len=0
        for i in password_1:
            len=len+1
            if i>='0' and i<='9':
                numFlag=1
            elif (i>='a' and i<='z')or(i>='A' and i<='Z'):
                engFlag=1
        if numFlag==0 or engFlag==0 or len<8 or len>18:
            return JsonResponse({'errno': 1005, 'msg': "密码不合法"})
        # 新建 Author 对象，赋值用户名和密码并保存
        new_author = Author(username=username, password=password_1,email=email)
        new_author.save()   # 一定要save才能保存到数据库中
        return JsonResponse({'errno': 0, 'msg': "注册成功"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
@csrf_exempt
def login(request):
    if request.session.has_key('email'):
        return JsonResponse({'errno': 1101, 'msg': "已有登录账号"})
    if request.method == 'POST':
        email = request.POST.get('email')  # 获取请求数据
        password = request.POST.get('password')
        if email is None or password is None:
            return JsonResponse({'errno': 2001, 'msg': "传入参数不足或错误"})
        try:
            author = Author.objects.get(email=email)
        except:
            return JsonResponse({'errno': 1002, 'msg': "用户名或密码错误"})
        if author.password == password:  # 判断请求的密码是否与数据库存储的密码相同
            # 密码正确则将用户名存储于session（django用于存储登录信息的数据库位置）
            request.session['email'] = email
            return JsonResponse({'errno': 0, 'msg': "登录成功", '用户id': author.id})
        else:
            return JsonResponse({'errno': 1002, 'msg': "用户名或密码错误"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
@csrf_exempt
def logout(request):
    if not request.session.has_key('email'):
        return JsonResponse({'errno': 1101, 'msg': "请先登录"})
    request.session.flush()
    return JsonResponse({'errno': 0, 'msg': "注销成功"})
@csrf_exempt
def delete(request):
    if request.method == 'POST':
        table=request.POST.get('table')
        key = request.POST.get('key')
        if table is None or key is None:
            return JsonResponse({'errno': 2001, 'msg': "传入参数不足或错误"})
        if table=='Author':
            try:
                item=Author.objects.get(email=key)
            except:
                return JsonResponse({'errno': 1003, 'msg': table + '中不存在包含 '+key+' 的条目'})
            else:
                item.delete()
                return JsonResponse({'errno': 0, 'msg': "删除成功"})
        elif table=='Article':
            try:
                item=Article.objects.get(id=key)
            except:
                return JsonResponse({'errno': 1003, 'msg': table + '中不存在包含 '+key+' 的条目'})
            else:
                item.delete()
                return JsonResponse({'errno': 0, 'msg': "删除成功"})
        else:
            return JsonResponse({'errno': 1002, 'msg': table+"不存在的表格"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
@csrf_exempt
def article_edit(request):
    if request.method == 'POST':
        op=request.POST.get('op') #1代表新发布，2代表修改，3代表查询状态
        condition=request.POST.get('condition')
        operator=request.session.get('username')
        title = request.POST.get('title')
        description = request.POST.get('description')
        body = request.POST.get('body')
        id=request.POST.get('id')
        aitem=Author.objects.get(username=operator)
        if op is None:
            return JsonResponse({'errno': 2002, 'msg': "参数错误：缺少操作类型"})
        if op=="1":
            if title is None or body is None:
                return JsonResponse({'errno': 2001, 'msg': "对于新建文章操作，至少需要传入文章title、body信息"})
            new_article=Article(publisher_id=aitem.id,title=title,body=body,condition=0)
            if description is not None:
                new_article.description=description
            new_article.save()
            return JsonResponse({'errno': 0, 'msg': "文章生成成功",'data':new_article.id})
        elif op=="2":
            if title is None or body is None or id is None:
                return JsonResponse({'errno': 2001, 'msg': "对于修改文章操作，至少需要传入文章title、body信息和文章id"})
            try:
                item=Article.objects.get(id=id)
            except:
                return JsonResponse({'errno': 1001, 'msg': "文章未找到"})
            if aitem.id!=item.publisher_id:
                return JsonResponse({'errno': 1002, 'msg': "非作者本人不可修改"})
            item.title=title
            item.body=body
            item.description=description
            item.description=None
            item.condition=0
            item.save()
            return JsonResponse({'errno': 0, 'msg': "文章修改成功"})
        elif op=="3":
            if condition is None:
                return JsonResponse({'errno': 2001, 'msg': "对于查询文章状态操作，需要传入文章condition"})
            try:
                items=Article.objects.filter(publisher_id=aitem.id,condition=condition)
            except:
                return JsonResponse({'errno': 1003, 'msg': "未知异常"})
            list=[]
            for i in items:
                if i.description is None:
                    list.append({"title":i.title,"create_time":i.firstCreate})
                else:
                    list.append({"title":i.title,"description":i.description,"create_time":i.firstCreate})
            if len(list)==0:
                return JsonResponse({'errno': 0, 'msg': "未查找到对应的文章"})
            return JsonResponse({'errno': 0, 'msg': "查询成功",'data':str(list)})
        return JsonResponse({'errno': 1004, 'msg': "操作类型错误"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
@csrf_exempt
def changeCondition(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        condition=request.POST.get('condition')
        if request.session.get('username')!="Administrator":
            return JsonResponse({'errno': 1002, 'msg': "非管理员不可操作"})
        if id is None or condition is None:
            return JsonResponse({'errno': 2001, 'msg': "需要文章id和需要修改成的condition"})
        if condition!="-1" and condition !="1" and condition!="0":
            return JsonResponse({'errno': 1003, 'msg': "输入的condition不正确"})
        try:
            item=Article.objects.get(id=id)
        except:
            return JsonResponse({'errno': 1003, 'msg': "文章未找到"})
        item.condition=condition
        item.save()
        return JsonResponse({'errno': 0, 'msg': "修改文章状态成功"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
@csrf_exempt
def changeUsername(request):
    if request.method == 'POST':
        if not request.session.has_key('email'):
            return JsonResponse({'errno': 1101, 'msg': "请先登录"})
        username=request.POST.get('username')
        if username is None:
            return JsonResponse({'errno': 2001, 'msg': "未输入新名称"})
        item=Author.objects.get(email=request.session.get('email'))
        if username==item.username:
            return JsonResponse({'errno': 1003, 'msg': "名称未修改"})
        item.username=username
        item.save()
        return JsonResponse({'errno': 0, 'msg': "名称修改成功"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
@csrf_exempt
def changePassword(request):
    if request.method == 'POST':
        if not request.session.has_key('email'):
            return JsonResponse({'errno': 1101, 'msg': "请先登录"})
        oldPassword=request.POST.get('oldPassword')
        newPassword1 = request.POST.get('newPassword1')
        newPassword2 = request.POST.get('newPassword2')
        if oldPassword is None or newPassword1 is None or newPassword2 is None:
            return JsonResponse({'errno': 2001, 'msg': "输入参数不足"})
        item=Author.objects.get(email=request.session['email'])
        if oldPassword!=item.password:
            return JsonResponse({'errno': 1002, 'msg': "旧密码输入错误"})
        if newPassword1!=newPassword2:
            return JsonResponse({'errno': 1003, 'msg': "两次新密码输入不相等"})
        if oldPassword==newPassword1:
            return JsonResponse({'errno': 1004, 'msg': "新密码不能与旧密码相同"})
        numFlag = 0
        engFlag = 0
        len = 0
        for i in newPassword1:
            len = len + 1
            if i >= '0' and i <= '9':
                numFlag = 1
            elif (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
                engFlag = 1
        if numFlag == 0 or engFlag == 0 or len < 8 or len > 18:
            return JsonResponse({'errno': 1005, 'msg': "新密码不合法"})
        item.password=newPassword1
        item.save()
        return JsonResponse({'errno': 0, 'msg': "密码修改成功"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})