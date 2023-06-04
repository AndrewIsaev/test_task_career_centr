from rest_framework import permissions


class IsActivePermission(permissions.IsAuthenticated):
    """Class with API permissions"""
    message = "Only active users has API permission"

    def has_permission(self, request, view):
        """Only active users has API permission"""
        return request.user.is_active
