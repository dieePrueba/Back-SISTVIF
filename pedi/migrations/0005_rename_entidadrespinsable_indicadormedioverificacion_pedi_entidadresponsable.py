# Generated by Django 3.2.16 on 2024-05-11 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedi', '0004_indicadormedioverificacion_pedi_medio_verificacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indicadormedioverificacion_pedi',
            old_name='entidadRespinsable',
            new_name='entidadResponsable',
        ),
    ]
