# Generated by Django 3.2.16 on 2024-04-25 21:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventario', '0005_auto_20240425_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventarioist',
            name='asignado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
