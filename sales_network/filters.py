from typing import Type

from django_filters import CharFilter
from django_filters.rest_framework import FilterSet

from sales_network.models import Unit


class CountryFilter(FilterSet):
    """Filer by country"""

    country: CharFilter = CharFilter(
        field_name='contact__country',
        lookup_expr='icontains',
    )

    class Meta:
        model: Type[Unit] = Unit
        fields: tuple[str] = ('contact__country',)
