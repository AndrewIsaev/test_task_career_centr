from django.contrib import admin
from django.db.models import QuerySet
from django.urls import reverse
from django.utils.html import format_html

from sales_network.models import Contact, Product, Unit


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Contact admin panel
    """

    list_display: list[str] = ['email', 'country', 'city', 'street', 'building']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Product admin panel
    """

    list_display: list[str] = ['title', 'model', 'release_date']


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    """
    Unit admin panel
    """

    list_display: list[str] = [
        'id',
        'title',
        'supplier_url',
        'debt',
    ]
    list_display_links: list[str] = ['id', 'title']
    list_filter: tuple[str] = ('contact__city',)
    actions: tuple[str] = ('set_debt_to_zero',)

    def supplier_url(self, obj: Unit) -> str | None:
        """Get supplier url"""
        if obj.supplier:
            return format_html(  # type: ignore
                '<a href="{0}">{1}</a>'.format(
                    reverse('admin:sales_network_unit_change', args=(obj.supplier.pk,)),
                    obj.supplier,
                )
            )

    supplier_url.short_description = 'Supplier'  # type: ignore

    @admin.action(description='Clear debt')
    def set_debt_to_zero(self, queryset: QuerySet) -> None:
        """
        Clear supplier debt for selected units
        """
        queryset.update(debt=0)
