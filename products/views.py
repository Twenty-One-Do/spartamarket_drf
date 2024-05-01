from django.db.models import F
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Product, Tag, Tag_Relation, Comment, Likes_Relation
from .serializers import ProductSerializer, CommentSerializer

import re
tag_pattern = re.compile(r'^[가-힣#\s]+$')

class ProductList(APIView):

    def tags_save(self, raw_tags, product):
        tags = raw_tags.replace(' ', '').split('#')[1:]
        for tag_name in tags:
            tag, create = Tag.objects.get_or_create(name=tag_name)
            if create:
                Tag_Relation.objects.get_or_create(tag_id=tag, product_id=product)

    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

        raw_tags = request.data.get('tags')
        if not bool(tag_pattern.match(raw_tags)):
            return Response({"tags": "태그 입력란에는 한글, 공백, 해시 기호(#)만 입력이 가능합니다."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save(writer=request.user)
            self.tags_save(raw_tags, product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Products(APIView):

    def get(self, request, what):
        product = get_object_or_404(Product, id=what)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, what):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

        product = get_object_or_404(Product, id=what)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(writer=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, what):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

        product = get_object_or_404(Product, id=what, writer=request.user)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Comments(APIView):

    def get(self, request, what):
        product = get_object_or_404(Product, id=what)
        serializer = CommentSerializer(product.comments, many=True)
        return Response(serializer.data)

    def post(self, request, what):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)
        product = get_object_or_404(Product, id=what)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(writer=request.user, product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, comment_id):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)
        comment = get_object_or_404(Comment, id=comment_id, writer=request.user)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, comment_id):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

        comment = get_object_or_404(Comment, id=comment_id, writer=request.user)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Likes(APIView):

    def post(self, request):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)
        product_id = request.data.get('what')
        product = get_object_or_404(Product, id=product_id)

        like_relation, create = Likes_Relation.objects.get_or_create(
            product_id=product,
            user_id=request.user
        )

        if create:
            product.likes_num = F('likes_num') + 1
            response_status = status.HTTP_201_CREATED
        else:
            product.likes_num = F('likes_num') - 1
            like_relation.delete()
            response_status = status.HTTP_204_NO_CONTENT

        product.save()
        product.refresh_from_db()

        return Response(
            {'new_likes_num':product.likes_num},
                status=response_status
        )