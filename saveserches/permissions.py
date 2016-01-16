from rest_framework.permissions import BasePermission


class SaveSearchesPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated() and view.action in ('list', 'retrieve', 'create', 'destroy'):
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):

        return request.user.is_superuser or request.user == obj.user
