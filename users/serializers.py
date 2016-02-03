from django.contrib.auth.models import User
from users.models import UserDetail
from rest_framework import serializers

class UserSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField(source='user.id')
    first_name = serializers.CharField(allow_null=True, source='user.first_name', default='')
    last_name = serializers.CharField(allow_null=True, source='user.last_name', default='')
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    password = serializers.CharField(source='user.password')
    longitude = serializers.FloatField(allow_null=True, default=None)
    latitude = serializers.FloatField(allow_null=True, default=None)
    token_facebook = serializers.CharField(allow_null=True, default=None)
    avatar_url = serializers.URLField(allow_null=True, default=None)

    def create(self, validated_data):

        instance = UserDetail()
        user_data = validated_data.get('user')
        user = User.objects.create_user(username=user_data.get('username'),
                                        email=user_data.get('email'),
                                        password=user_data.get('password'),
                                        first_name=user_data.get('first_name'),
                                        last_name=user_data.get('last_name'))

        if user:
            instance.user = user
            user_ext = self.update(instance, validated_data)

        return user_ext

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
        elif self.instance and self.instance.user.username != data and len(users) != 0:
            raise serializers.ValidationError(u'Ya existe un usuario con ese username')
        else:
            return data

class UserListSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='user.id')
    first_name = serializers.CharField(allow_null=True, source='user.first_name', default='')
    last_name = serializers.CharField(allow_null=True, source='user.last_name', default='')
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')

    class Meta:
        model = UserDetail
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'avatar_url', 'avatar_thumbnail_url', 'products_count')

class UserPublicListSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='user.id')
    first_name = serializers.CharField(allow_null=True, source='user.first_name', default='')
    last_name = serializers.CharField(allow_null=True, source='user.last_name', default='')
    username = serializers.CharField(source='user.username')

    class Meta:
        model = UserDetail
        fields = ('id', 'first_name', 'last_name', 'username', 'avatar_url', 'avatar_thumbnail_url', 'products_count')


