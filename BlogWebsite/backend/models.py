from django.db import models


class Author(models.Model):
    # Author表项，含用户名和密码，均为字符串属性，并设置最大长度
    username = models.CharField(max_length=50, primary_key=False)
    password = models.CharField(max_length=40)
    email = models.EmailField()
    sex = models.CharField(max_length=5, null=True)
    birthday = models.CharField(max_length=20, null=True)
    discription = models.CharField(max_length=100, null=True)
    lastLogin = models.CharField(max_length=50, null=True)
    avatar = models.ImageField(null=True, upload_to="user_img/")


class Article(models.Model):
    title = models.CharField(max_length=100)
    discription = models.CharField(max_length=100, null=True)
    body = models.TextField(default=" ")  # 正文
    firstCreate = models.DateTimeField(auto_now_add=True, null=True)
    publisher = models.ForeignKey('Author', on_delete=models.CASCADE)
    label = models.CharField(max_length=10000)
    likes = models.IntegerField(default=0)
    commentsCount = models.IntegerField(default=0)


class FileInArticle(models.Model):
    file = models.FileField(upload_to="article_file/")
    articleId = models.IntegerField(null=True)
    userId = models.IntegerField(null=True)
    url = models.CharField(max_length=200)
