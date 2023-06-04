# Generated by Django 4.2.1 on 2023-05-31 17:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(
                default=True,
                help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
                verbose_name='active',
            ),
        ),
    ]
