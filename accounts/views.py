from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404

from .models import User

class Accounts(APIView):

    def get(self, request, who):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

        if request.user.id != who:
            return Response(status=status.HTTP_403_FORBIDDEN)

        user = get_object_or_404(User, id=who)
        serializer = UserSerializer(user)

        return Response(serializer.data)

    def post(self, request):
        userserializer = UserSerializer(data=request.data)
        if userserializer.is_valid():
            userserializer.save()
            return Response(userserializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(userserializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, who):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

        if request.user.id != who:
            return Response(status=status.HTTP_403_FORBIDDEN)

        user = get_object_or_404(User, pk=who)
        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, who):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

        if request.user.id != who:
            return Response(status=status.HTTP_403_FORBIDDEN)

        user = get_object_or_404(User, pk=who)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Follow(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        pass