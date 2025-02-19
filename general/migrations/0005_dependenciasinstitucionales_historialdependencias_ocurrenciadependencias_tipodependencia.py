# Generated by Django 3.2.16 on 2024-05-10 22:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import general.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('general', '0004_auto_20240411_1018'),
    ]

    operations = [
        migrations.CreateModel(
            name='OcurrenciaDependencias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDependencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('activo', models.BooleanField(default=True)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('digitador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HistorialDependencias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('archivo', models.FileField(blank=True, null=True, upload_to='dependencias/pdfs/', validators=[general.models.validate_pdf_size])),
                ('fecha', models.DateField(auto_now_add=True)),
                ('edicion', models.BooleanField(default=True)),
                ('digitador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ocurrencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.ocurrenciadependencias')),
            ],
        ),
        migrations.CreateModel(
            name='DependenciasInstitucionales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('activo', models.BooleanField(default=True)),
                ('digitador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='digitador', to=settings.AUTH_USER_MODEL)),
                ('representante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='representante', to=settings.AUTH_USER_MODEL)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.tipodependencia')),
            ],
        ),
    ]
