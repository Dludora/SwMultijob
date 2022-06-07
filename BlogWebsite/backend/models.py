from django.db import models
class Author(models.Model):
    # Author表项，含用户名和密码，均为字符串属性，并设置最大长度
    username = models.CharField(max_length=50,primary_key=False)
    password = models.CharField(max_length=40)
    email = models.EmailField()
    sex=models.CharField(max_length=5,null=True)
    birthday=models.CharField(max_length=20,null=True)
    discription=models.CharField(max_length=100,null=True)
    lastLogin=models.CharField(max_length=50,null=True)
class Article(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100,null=True)
    body=models.TextField(default=" ") #正文
    firstCreate=models.DateTimeField(auto_now_add=True)
    condition=models.IntegerField(default=0) #0代表审核中，1代表已发布，-1代表审核失败
    publisher=models.ForeignKey('Author',on_delete=models.CASCADE)