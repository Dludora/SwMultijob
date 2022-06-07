from django.db import models


# Create your models here.
class Stars(models.Model):
    userId = models.CharField(max_length=50)
    articleId = models.CharField(max_length=50)

    class Meta:
        unique_together = (('userId', 'articleId'),)


class Follow(models.Model):
    userId = models.CharField(max_length=50)
    followId = models.CharField(max_length=50)

    class Meta:
        unique_together = (('userId', 'followId'),)


class History(models.Model):
    userId = models.CharField(max_length=50)
    articleId = models.CharField(max_length=50)

    time = models.DateTimeField(auto_now_add=True)

