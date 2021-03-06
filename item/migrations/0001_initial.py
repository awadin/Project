# Generated by Django 3.0.4 on 2020-03-23 20:49

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('itemname', models.CharField(max_length=100)),
                ('descrip', models.CharField(max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('inv_count', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000000)])),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
