from datetime import date, datetime

from django.db import models


# Create your models here.
class Product(models.Model):
    """Product model"""

    title: str = models.CharField(max_length=100)
    model: str = models.CharField(max_length=50)
    release_date: date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self) -> str:
        return f'{self.title} {self.model}'


class Contact(models.Model):
    """Contact model"""

    email: str = models.EmailField()
    country: str = models.CharField(max_length=100, null=True, blank=True)
    city: str = models.CharField(max_length=100, null=True, blank=True)
    street: str = models.CharField(max_length=100, null=True, blank=True)
    building: str = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self) -> str:
        return f'{self.country}, {self.city}, {self.street}'


class Unit(models.Model):
    """Unit model"""

    class Type(models.IntegerChoices):
        """Unit types"""

        PLANT = 0
        RETAIL_NETWORK = 1
        INDIVIDUAL_ENTREPRENEUR = 2

    title: str = models.CharField(max_length=100, blank=True)
    type: int = models.PositiveSmallIntegerField(choices=Type.choices)
    contact: Contact = models.ForeignKey(
        'sales_network.Contact', on_delete=models.SET_NULL, null=True, blank=True
    )
    product: Product = models.ManyToManyField(
        'sales_network.Product', null=True, blank=True
    )
    supplier = models.ForeignKey(
        'sales_network.Unit', on_delete=models.SET_NULL, null=True, blank=True
    )
    debt: float = models.FloatField(default=0)
    created: datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Звено'
        verbose_name_plural = 'Звенья'

    def __str__(self) -> str:
        return f'{self.title}'
