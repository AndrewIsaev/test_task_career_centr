from django.contrib import admin
from django.db.models import QuerySet
from django.urls import reverse
from django.utils.html import format_html

from sales_network.models import Contact, Product, Unit


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'debt', 'supplier_url']
    list_filter = ('contact__city',)
    actions = ('set_debt_to_zero',)

    def supplier_url(self, obj):
        if obj.supplier:
            return format_html(
                '<a href="{0}">{1}</a>'.format(
                    reverse('admin:sales_network_unit_change', args=(obj.supplier.pk,)),
                    obj.supplier,
                )
            )

    supplier_url.short_description = 'Supplier'

    @admin.action(description='Clear debt')
    def set_debt_to_zero(self, request, queryset: QuerySet):
        queryset.update(debt=0)
