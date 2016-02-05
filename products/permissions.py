from rest_framework.permissions import BasePermission

class ProductPermission(BasePermission):

    def has_permission(self, request, view):

        if view.action in ['list', 'metadata', 'retrieve']:
            return True
        elif view.action in ['create', 'update']:
            return request.user.is_authenticated()
        else:
            return request.user.is_authenticated() and request.user.is_staff


class UserProductPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated()
