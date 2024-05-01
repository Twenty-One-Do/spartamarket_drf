from .models import Product, Comment
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'title',
            'content',
            'writer',
            'likes_num',
            'views_num',
            'category',
            'image',
            'date_created',
            'last_updated',
        )
        read_only_fields = (
            'writer',
            'likes_num',
            'views_num',
            'date_created',
            'last_updated',
        )

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = (
            'product',
            'writer',
            'date_created',
            'last_updated',
        )
