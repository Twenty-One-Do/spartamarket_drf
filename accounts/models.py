from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    name = models.CharField(max_length=10, default="")
    nickname = models.CharField(max_length=10, default="", unique=True)
    age = models.PositiveSmallIntegerField(default=0)
    follower_num = models.PositiveIntegerField(default=0)
    following_num = models.PositiveIntegerField(default=0)

class Follow_Relation(models.Model):
    who = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    whom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')