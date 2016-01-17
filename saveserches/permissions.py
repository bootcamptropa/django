from rest_framework.permissions import BasePermission


class SaveSerchesPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ('list', 'retrieve', 'create', 'destroy', 'metadata'):
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):

        return request.user == obj.user
