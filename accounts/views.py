from django.db.models import F
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404

from .models import User, Follow_Relation

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

        user = get_object_or_404(User, id=who)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Follow(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        who = request.user

        whom = get_object_or_404(
            User,
            id=request.data.get('whom')
        )

        follow_relation, create = \
            Follow_Relation.objects.get_or_create(
                who=who,
                whom=whom
            )

        if create:
            who.following_num = F('following_num') + 1
            whom.follower_num = F('follower_num') + 1
            response_status = status.HTTP_201_CREATED
        else:
            who.following_num = F('following_num') - 1
            whom.follower_num = F('follower_num') - 1
            follow_relation.delete()
            response_status = status.HTTP_204_NO_CONTENT

        who.save()
        whom.save()
        who.refresh_from_db()
        whom.refresh_from_db()
        return Response(
            {
                'my': {
                    'new_follower_num': who.follower_num,
                    'new_following_num': who.following_num,
                },
                'whom': {
                    'new_follower_num': whom.follower_num,
                    'new_following_num': whom.following_num,
                },
            },
            status=response_status
        )
