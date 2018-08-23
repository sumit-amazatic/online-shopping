"""
    User App Permission
"""
from rest_framework.permissions import BasePermission


class UserAccessPermission(BasePermission):
    """
         UserViewSet Permissions
    """

    message = "Access Denied."

    def has_permission(self, request, view):

        if view.action in ['auth', 'create']:
            is_allowed = True
        elif view.action == 'list':
            if request.user.is_superuser:
                is_allowed = True
            else:
                is_allowed = False
        elif request.auth and view.action != 'destroy':
            if str(request.user.id) == view.kwargs['pk'] or request.user.is_superuser:
                is_allowed = True
            else:
                is_allowed = False
        else:
            is_allowed = False
        return is_allowed
