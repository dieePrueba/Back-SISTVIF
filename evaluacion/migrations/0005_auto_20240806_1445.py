# Generated by Django 3.2.16 on 2024-08-06 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0004_auto_20240706_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentoevaluacion',
            name='estado',
            field=models.IntegerField(choices=[(1, 'Por revisar'), (2, 'Aprobado'), (3, 'Corregir')], default=1),
        ),
        migrations.AddField(
            model_name='documentoevaluacion',
            name='observacion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='documentoevaluacion',
            name='evidenciaEvaluacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documentos', to='evaluacion.evidenciaevaluacion'),
        ),
        migrations.AlterField(
            model_name='evidenciaevaluacion',
            name='indicadorEvaluacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evidencias', to='evaluacion.indicadorevaluacion'),
        ),
    ]
