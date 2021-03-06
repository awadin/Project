# Generated by Django 3.0.4 on 2020-03-25 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_auto_20200325_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='is_ordered',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='items',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='item.Item'),
            preserve_default=False,
        ),
    ]
