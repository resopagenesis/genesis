# Generated by Django 4.0.6 on 2022-08-30 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0015_columna_borde_fila_borde_seccion_borde'),
    ]

    operations = [
        migrations.AddField(
            model_name='columna',
            name='ingresosistema',
            field=models.BooleanField(default=False),
        ),
    ]
