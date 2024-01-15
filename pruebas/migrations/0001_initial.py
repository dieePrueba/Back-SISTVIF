# Generated by Django 3.2.16 on 2024-01-04 02:35

from django.db import migrations, models
import pruebas.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivoPDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('archivo', models.FileField(upload_to='pdfs/', validators=[pruebas.models.validate_pdf_size])),
            ],
        ),
    ]
