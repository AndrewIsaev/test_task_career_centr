from rest_framework import permissions
from rest_framework.request import Request

from sales_network.views import UnitViewSet


class IsActivePermission(permissions.IsAuthenticated):
    """Class with API permissions"""

    message: str = 'Only active users has API permission'

    def has_permission(self, request: Request, view: UnitViewSet) -> bool:
        """Only active users has API permission"""
        return request.user.is_active
