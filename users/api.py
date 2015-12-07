# -*- coding: utf-8 -*-

from users.models import UserDetail
from users.serializers import UserSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from users.permissions import UserPermission
from rest_framework.viewsets import GenericViewSet

class UserViewSet(GenericViewSet):

    pagination_class = PageNumberPagination
    permission_classes = (UserPermission,)
    serializer_class = UserSerializer
    queryset = UserDetail.objects.all()

    def list(self, request):

        users = UserDetail.objects.all()
        self.paginate_queryset(users)  # pagino el resultado
        serializer = UserSerializer(users, many=True)
        return self.get_paginated_response(serializer.data)  # devuelvo una respuesta paginada

    def create(self, request):

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk):
        user = get_object_or_404(UserDetail, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        serialized_user = serializer.data

        return Response(serialized_user)

    def update(self, request, pk):
        user = get_object_or_404(UserDetail, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(instance=user, data=request.data)
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

    def get_serializer_class(self):
        return UserSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)