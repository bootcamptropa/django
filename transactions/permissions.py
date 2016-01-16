from rest_framework.permissions import BasePermission


class TransactionPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ('list', 'retrieve', 'create'):
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):

        return request.user.is_superuser or request.user == obj.seller or request.user == obj.buyer
