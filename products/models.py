from django.db import models

from accounts.models import User


class Product(models.Model):
    CATEGORY = {
        '' : ''
    }
    title = models.CharField(max_length=100, default="title")
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    likes_num = models.PositiveIntegerField(default=0)
    views_num = models.PositiveIntegerField(default=0)
    category = models.CharField(choices=CATEGORY, max_length=10)
    image = models.ImageField(upload_to='../static/images/')

class Tag(models.Model):
    name=models.CharField(max_length=10, unique=True, default="no tag")

class Tag_Relation(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='tags')
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='products')

class Likes_Relation(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes_users')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes_products')

class Views_Relation(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='views_users')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='views_products')