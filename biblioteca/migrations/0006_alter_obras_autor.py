# Generated by Django 3.2.16 on 2024-04-16 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0005_alter_obrasautores_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obras',
            name='autor',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
    ]
