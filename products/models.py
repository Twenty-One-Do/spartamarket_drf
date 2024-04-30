from django.db import models

from accounts.models import User


class Product(models.Model):
    PRODUCT_CATEGORY = (
        ('clothing', '의류'),
        ('electronics', '전자 제품'),
        ('toys', '장난감'),
        ('books', '도서'),
        ('foods', '음식'),
        ('hobbies', '취미'),
        ('etc', '기타'),
    )
    title = models.CharField(max_length=100, default="title")
    content = models.TextField(max_length=500)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    likes_num = models.PositiveIntegerField(default=0)
    views_num = models.PositiveIntegerField(default=0)
    category = models.CharField(choices=PRODUCT_CATEGORY, max_length=30, default='clothing')
    image = models.ImageField(upload_to='../static/images/', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.TextField(max_length=500)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

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