# Generated by Django 3.2.16 on 2024-02-09 02:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoInventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TipoInventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UbicacionInventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.CharField(max_length=400)),
                ('referencia', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InventarioIST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_unico', models.CharField(max_length=200)),
                ('cod_senescyt', models.CharField(max_length=200)),
                ('cod_instituto', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('materiales', models.TextField()),
                ('marca', models.CharField(max_length=200)),
                ('modelo', models.CharField(max_length=200)),
                ('serie', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('asignado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.estadoinventario')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.tipoinventario')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.ubicacioninventario')),
            ],
        ),
    ]
