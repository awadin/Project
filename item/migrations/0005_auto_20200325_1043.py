# Generated by Django 3.0.4 on 2020-03-25 14:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    atomic=False

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0004_cart_quantity'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart',
            new_name='OrderItem',
        ),
    ]
