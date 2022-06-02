## 1、前后端项目合并

### 后端项目

#### 项目创建/运行

​	在前端项目同级命令行中打开终端，输入`django-admin startproject 项目名称`

​	cd进该目录，输入 `python manage.py runserver`，运行该项目，终端上出现链接

#### 配置数据库

​	找到第一次创建出的文件夹下，找到`settings.py`文件，找到如下代码

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

​	如果想要更换为自己的`mysql`数据库，可以参考以下设置进行更改

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xxx',				# 数据库名称
        'USER': 'root'				# 连接数据库的用户名称
        'PASSWORD': 'xxxx'			# 用户密码
        'HOST': '127.0.0.1'			 # 访问的数据库的主机ip地址
        'PORT': '3306'				# 默认mysql访问端口
    }
}
```

运行 `python manage.py migrate`

#### 新建应用

​	再次在终端上输入`python manage.py startapp xxx`，创建出`xxx`应用

​	找到第一次创建出的文件夹下，找到`settings.py`文件，找到如下代码

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend.apps.BackendConfig',
]
```

​	把新建的应用添加进去,修改如下

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend.apps.BackendConfig',
    'xxx.apps.XxxConfig',
]
```

在`models.py`文件中添加好自己想要的内容后，运行`python manage.py makemigrations`, `python manage.py migrate`

#### 超级管理员

在终端中，输入`python manage.py createsuperuser`后，按照提示创建超级管理员账号

在服务端口后加`/admin`，即可进入超级管理员界面，如果想要在该界面管理新建出的xxx应用，则修改改应用目录下的admin.py文件

`admin.py`文件

```python
from django.contrib import admin
from .models import Author
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'email']


admin.site.register(Author, AuthorAdmin)

```

`models.py`文件

```python
from django.db import models
class Author(models.Model):
    # Author表项，含用户名和密码，均为字符串属性，并设置最大长度
    username = models.CharField(max_length=50,primary_key=False)
    password = models.CharField(max_length=20)
    email = models.EmailField()
```

#### 安装def-rest-framework

##### 终端依次输入指令

`pip install djangorestframework`

`pip install markdown`

`pip install django-filter`

##### 配置`drf settings.py`文件

###### 引入app

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',	// 写在所有自定义模块之上
    'backend.apps.BackendConfig',
]
```

###### 引入drf

放在DATA_BASE以下

```
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
```

#### 实现cors跨域

命令行输入`pip install django-cors-headers`

在`settings.py` 中的`INSTALED_APPS`中引入`corsheaders` , `MIDDLEWARE`中的第三位引入`corsheaders.middleware.CorsMiddleware`

文件最下方加入

```python
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:8080',
    'http://localhost:8080',
)
CORS_ALLOW_CREDENTIALS = True  # 指明在跨域访问中，后端是否支持对cookie的操作。

CORS_ALLOW_METHODS = (
 'DELETE',
 'GET',
 'OPTIONS',
 'PATCH',
 'POST',
 'PUT',
 'VIEW',
)
CORS_ALLOW_HEADERS = (
 'XMLHttpRequest',
 'X_FILENAME',
 'accept-encoding',
 'authorization',
 'content-type',
 'dnt',
 'origin',
 'user-agent',
 'x-csrftoken',
 'x-requested-with',
 'Pragma',
)
```
