# Generated by Django 4.2.1 on 2023-05-31 17:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('sales_network', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='product',
            field=models.ManyToManyField(to='sales_network.product'),
        ),
    ]
