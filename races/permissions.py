from rest_framework.permissions import BasePermission

class RacesPermission(BasePermission):

    def has_permission(self, request, view):

        if view.action in ['list', 'metadata']:
            return True
        else:
            return request.user.is_authenticated() and request.user.is_admin()
