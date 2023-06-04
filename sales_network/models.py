from django.db import models


# Create your models here.
class Product(models.Model):
    """Product model"""

    title = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    release_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.title} {self.model}'


class Contact(models.Model):
    """Contact model"""

    email = models.EmailField()
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    building = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f'{self.country}, {self.city}, {self.street}'


class Unit(models.Model):
    """Unit model"""

    class Type(models.IntegerChoices):
        PLANT = 0
        RETAIL_NETWORK = 1
        INDIVIDUAL_ENTREPRENEUR = 2

    title = models.CharField(max_length=100)
    type = models.PositiveSmallIntegerField(choices=Type.choices)
    contact = models.ForeignKey(
        'sales_network.Contact', on_delete=models.SET_NULL, null=True, blank=True
    )
    product = models.ManyToManyField('sales_network.Product')
    supplier = models.ForeignKey(
        'sales_network.Unit', on_delete=models.SET_NULL, null=True, blank=True
    )
    debt = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Звено'
        verbose_name_plural = 'Звенья'

    def __str__(self):
        return f'{self.title}'
