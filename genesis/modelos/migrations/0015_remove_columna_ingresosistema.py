# Generated by Django 4.1.1 on 2022-11-20 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0014_seccion_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='columna',
            name='ingresosistema',
        ),
    ]
