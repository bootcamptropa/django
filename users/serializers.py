# -*- coding: utf-8 -*-

from users.models import UserDetail
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    password = serializers.CharField(source='user.password')
    longitude = serializers.FloatField()
    latitude = serializers.FloatField()
    token_facebook = serializers.CharField()
    avatar_url = serializers.URLField()

    def create(self, validated_data):

        instance = UserDetail()
        userData = validated_data.get('user')
        user = User.objects.create_user(username=userData.get('username'), email=userData.get('email'), password=userData.get('password'), first_name=userData.get('first_name'), last_name=userData.get('last_name'))

        if user:
            instance.user = user
            userExt = self.update(instance, validated_data)

        return userExt

    def update(self, instance, validated_data):

        userData = validated_data.get('user')

        instance.user.first_name = userData.get('first_name')
        instance.user.last_name = userData.get('last_name')
        instance.user.username = userData.get('username')
        instance.user.email = userData.get('email')
        instance.user.set_password(userData.get('password'))
        instance.latitude = validated_data.get('latitude')
        instance.longitude = validated_data.get('longitude')
        instance.avatar_url = validated_data.get('avatar_url')
        instance.token_facebook = validated_data.get('token_facebook')

        instance.save()

        return instance


    def validate_username(self, data):

        users = User.objects.filter(username=data)
        if not self.instance and len(users) != 0:
            raise serializers.ValidationError(u'Ya existe un usuario con ese username')
        elif self.instance and self.instance.username != data and len(users) != 0:
            raise serializers.ValidationError(u'Ya existe un usuario con ese username')
        else:
            return data