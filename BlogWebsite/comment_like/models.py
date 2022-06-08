from django.db import models

# Create your models here.
class Comments(models.Model):
    userId = models.CharField(max_length=100)
    articleId = models.CharField(max_length=100)
    comment = models.TextField(max_length=100000)

class Likes(models.Model):
    userId = models.CharField(max_length=100)
    articleId = models.CharField(max_length=100)
    class Meta:
        unique_together = (('userId', 'articleId'))