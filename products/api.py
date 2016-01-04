from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from products.serializers import ProductsSerializer
from products.models import Product

class ProductsViewSet (ModelViewSet):

    serializer_class = ProductsSerializer
    queryset = Product.objects.filter(active=1)

    def list(self, request):

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
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)