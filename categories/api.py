import datetime

from rest_framework import status
from categories.models import Category
from categories.permissions import CategoryPermission
from categories.serializers import CategorySerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

class CategoryViewSet (GenericViewSet):

    permission_classes = [CategoryPermission]

    queryset = Category.objects.filter(active=1)
    serializer_class = CategorySerializer

    def list(self, request):

        queryset = self.filter_queryset(self.get_queryset())
        date_update_string = self.request.query_params.get('dateUpdate', None)

        if date_update_string is not None:

            try:
                date_update = datetime.datetime.strptime(date_update_string, "%Y-%m-%dT%H:%M:%S")
            except ValueError:
                return Response("Error parse date update", status=status.HTTP_400_BAD_REQUEST)

            queryset = queryset.filter(updated_at__gte=date_update)

        page = self.paginate_queryset(queryset)

        if page is not None:

            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
