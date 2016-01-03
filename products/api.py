# -*- coding: utf-8 -*-

from oauth2_provider.ext.rest_framework import OAuth2Authentication, TokenHasScope
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from products.serializers import ProductsSerializer, ProductsListSerializer
from products.models import Product

class ProductsViewSet (ModelViewSet):

    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['read']
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()

    def list(self, request):

        self.serializer_class = ProductsListSerializer
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
          serializer = self.get_serializer(page, many=True)
          return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_paginated_response(self, data):

        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)