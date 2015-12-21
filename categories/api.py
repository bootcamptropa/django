# -*- coding: utf-8 -*-
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination
from categories.models import Category
from categories.serializers import CategorySerializer

class CategoryViewSet (GenericViewSet):

    pagination_class = PageNumberPagination
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def list(self, request):

        categories = Category.objects.all()
        self.paginate_queryset(categories)  # pagino el resultado
        serializer = CategorySerializer(categories, many=True)
        return self.get_paginated_response(serializer.data)  # devuelvo una respuesta paginada
