
from categories.models import Category
from categories.serializers import CategorySerializer

from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from oauth2_provider.ext.rest_framework import OAuth2Authentication, TokenHasScope

class CategoryViewSet (GenericViewSet):

    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['read']

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request):

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