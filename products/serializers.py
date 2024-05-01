from .models import Product, Comment, Tag
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id',
                  'title',
                  'content',
                  'writer',
                  'likes_num',
                  'views_num',
                  'category',
                  'image',
                  'date_created',
                  'last_updated',)
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

class TagSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()
    class Meta:
        model = Tag
        fields = '__all__'

    def get_name(self, obj):
        return obj.tag_id.name

class ProductDetailSerializer(ProductSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta(ProductSerializer.Meta):
        fields = ProductSerializer.Meta.fields + ('comments', 'tags')

