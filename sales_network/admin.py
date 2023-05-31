from django.contrib import admin

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
    pass
