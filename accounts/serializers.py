from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = (
            'name',
            'age',
            'email',
            'nickname',
            'username',
            'password',
            'password2',
            'date_joined',
            'last_login',
            'is_superuser',
            'is_staff',
            'is_active',
        )
        read_only_fields = (
            'date_joined',
            'last_login',
            'is_superuser',
            'is_staff',
            'is_active',
            'follower_num',
            'following_num',
        )

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "Passwords don't match"}
            )

        data.pop('password2')
        return data

    def create(self, validated_data):
        user = User(
            name=validated_data['name'],
            age=validated_data['age'],
            email=validated_data['email'],
            nickname=validated_data['nickname'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

