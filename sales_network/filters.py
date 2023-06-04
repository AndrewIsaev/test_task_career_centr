import django_filters
from django_filters.rest_framework import FilterSet

from sales_network.models import Unit


class CountryFilter(FilterSet):
    country = django_filters.CharFilter(field_name="contact__country", lookup_expr="icontains", )

    class Meta:
        model = Unit
        fields = ("contact__country", )
