# -*- coding: utf-8 -*-

from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination
from races.models import Race
from races.serializers import RacesSerializer

class RacesViewSet (GenericViewSet):

    pagination_class = PageNumberPagination
    serializer_class = RacesSerializer
    queryset = Race.objects.all()

    def list(self, request):

        races = Race.objects.all()
        self.paginate_queryset(races)  # pagino el resultado
        serializer = RacesSerializer(races, many=True)
        return self.get_paginated_response(serializer.data)  # devuelvo una respuesta paginada

