from rest_framework.viewsets import ModelViewSet
from saveserches.models import SavedSearch
from saveserches.permissions import SaveSearchesPermission
from saveserches.serializers import SaveSearchesSerializer, SaveSearchesListSerializer

class SaveSearchesViewSet (ModelViewSet):

    serializer_class = SaveSearchesSerializer
    permission_classes = (SaveSearchesPermission,)

    def get_queryset(self):
        return SavedSearch.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return SaveSearchesListSerializer
        else:
            return SaveSearchesSerializer

    def get_paginated_response(self, data):

        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)