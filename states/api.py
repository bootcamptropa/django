# -*- coding: utf-8 -*-

from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination
from states.serializers import StatesSerializer
from states.models import State

class StatesViewSet (GenericViewSet):

    pagination_class = PageNumberPagination
    serializer_class = StatesSerializer
    queryset = State.objects.all()

    def list(self, request):

        states = State.objects.all()
        self.paginate_queryset(states)  # pagino el resultado
        serializer = StatesSerializer(states, many=True)
        return self.get_paginated_response(serializer.data)  # devuelvo una respuesta paginada