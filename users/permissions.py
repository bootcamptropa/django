# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):

        if view.action in ['create', 'metadata']:
            return True
        elif request.user.is_superuser:
            return True
        elif view.action in ['retrieve', 'update', 'destroy', 'metadata']:
            return True
        else:
            if view.action in ['options', 'metadata']:
                return True
            else:
                return False

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user == obj