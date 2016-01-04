from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from products.serializers import ProductsSerializer, ProductsListSerializer
from products.models import Product

class ProductsViewSet (ModelViewSet):

    pagination_class = PageNumberPagination
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()

    def list(self, request):

        products = Product.objects.all()
        self.paginate_queryset(products)  # pagino el resultado
        serializer = ProductsListSerializer(products, many=True)
        return self.get_paginated_response(serializer.data)  # devuelvo una respuesta paginada
