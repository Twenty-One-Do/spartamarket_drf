from django.db import models

from accounts.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100, blank=True)

def get_default_category():
    return ProductCategory.objects.first()

class Product(models.Model):
    title = models.CharField(max_length=100, default="title")
    content = models.TextField(max_length=500)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    likes_num = models.PositiveIntegerField(default=0)
    views_num = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory,
                                 on_delete=models.SET(get_default_category),
                                 null=True)
    image = models.ImageField(upload_to='images/', blank=True)
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