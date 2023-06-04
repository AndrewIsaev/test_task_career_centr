from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets

from sales_network.filters import CountryFilter
from sales_network.models import Unit
from sales_network.permissions import IsActivePermission
from sales_network.serializers import UnitSerializer, UnitCreateSerializer


@extend_schema_view(
    list=extend_schema(
        description='List of Units',
        summary='Units list',
    ),
    create=extend_schema(
        description='Create Unit',
        summary='Create Unit',
    ),
    retrieve=extend_schema(
        description='Detail Unit',
        summary='Detail Unit',
    ),
    update=extend_schema(
        description='Update of Units',
        summary='Update Unit',
    ),
    partial_update=extend_schema(
        description='Partial update of Unit', summary='Partial update Unit'
    ),
    destroy=extend_schema(description='Delete Unit', summary='Delete Unit'),
)
class UnitViewSet(viewsets.ModelViewSet):
    default_serializer = UnitSerializer
    serializers = {
        'create': UnitCreateSerializer,
        'update': UnitCreateSerializer,
        'partial_update': UnitCreateSerializer,
    }
    queryset = Unit.objects.all()

    filter_backends = (DjangoFilterBackend,)
    filterset_class = CountryFilter
    permission_classes = [
        IsActivePermission,
    ]

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)
