# Generated by Django 3.2.16 on 2024-04-10 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_bolsaempleo'),
    ]

    operations = [
        migrations.AddField(
            model_name='bolsaempleo',
            name='estadoVF',
            field=models.BooleanField(default=True),
        ),
    ]
