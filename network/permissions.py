from rest_framework import permissions


class IsActiveEmployee(permissions.BasePermission):
    """
    Право доступа только активным сотрудникам.
    """
    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated
                and request.user.is_active)
