from rest_framework.viewsets import ModelViewSet
from saveserches.models import SavedSearch
from saveserches.permissions import SaveSerchesPermission
from saveserches.serializers import SaveSerchesSerializer, SaveSerchesListSerializer

class SaveSerchesViewSet (ModelViewSet):

    serializer_class = SaveSerchesSerializer
    permission_classes = (SaveSerchesPermission,)

    def get_queryset(self):
        return SavedSearch.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return SaveSerchesListSerializer
        else:
            return SaveSerchesSerializer

    def get_paginated_response(self, data):

        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)