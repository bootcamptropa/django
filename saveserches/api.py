from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from saveserches.models import SavedSearch
from saveserches.serializers import SaveSerchesSerializer, SaveSerchesListSerializer


class SaveSerchesViewSet (GenericViewSet):

    serializer_class = SaveSerchesSerializer
    queryset = SavedSearch.objects.all()

    def list(self, request):

        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        self.serializer_class = SaveSerchesListSerializer

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

    def get_paginated_response(self, data):

        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)