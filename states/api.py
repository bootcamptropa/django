from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from states.serializers import StatesSerializer
from states.models import State

class StatesViewSet (GenericViewSet):

    serializer_class = StatesSerializer
    queryset = State.objects.filter(active=1)

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
