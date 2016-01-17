from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users.models import UserDetail
from users.permissions import UserPermission, LoginPermission
from users.serializers import UserSerializer


class UserViewSet(GenericViewSet):

    permission_classes = [UserPermission]
    queryset = UserDetail.objects.all()
    serializer_class = UserSerializer

    allowed_methods = ['get', 'post', 'put', 'delete', 'options']

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user_save = serializer.save()
            return Response(user_save.user_id, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):

        user = get_object_or_404(UserDetail, pk=pk)
        self.check_object_permissions(request, user)
        serializer = self.get_serializer(user)
        serialized_user = serializer.data
        return Response(serialized_user)

    def update(self, request, pk):

        user = get_object_or_404(UserDetail, pk=pk)
        self.check_object_permissions(request, user)
        serializer = self.get_serializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):

        user = get_object_or_404(UserDetail, pk=pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LoginViewSet(GenericViewSet):

    permission_classes = [LoginPermission]
    queryset = UserDetail.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):

        user = request.user

        if user is not None:
            if user.is_active:
                user_dateail = get_object_or_404(UserDetail, pk=user.id)
                serializer = self.get_serializer(user_dateail)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response('Not valid User', status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Not valid User', status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):

        username = request.data.get('user_name')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                user_dateail = get_object_or_404(UserDetail, pk=user.id)
                serializer = self.get_serializer(user_dateail)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response('Not valid User', status=status.HTTP_400_BAD_REQUEST)
        else:
             return Response('Not valid User', status=status.HTTP_400_BAD_REQUEST)
