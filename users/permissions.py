from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):

    def has_permission(self, request, view):

        if view.action in ['create', 'metadata']:
            return True
        else:
            return request.user.is_authenticated()

    def has_object_permission(self, request, view, user):

        return request.user.is_superuser or request.user == user

class LoginPermission(BasePermission):

    def has_permission(self, request, view):

        if view.action == 'list':
            return request.user.is_authenticated()
        else:
            return True
