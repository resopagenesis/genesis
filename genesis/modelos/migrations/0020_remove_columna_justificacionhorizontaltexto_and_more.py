# Generated by Django 4.1.1 on 2022-11-22 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0019_columna_colortexto_columna_fonttexto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='columna',
            name='justificacionhorizontaltexto',
        ),
        migrations.RemoveField(
            model_name='columna',
            name='justificacionverticaltexto',
        ),
    ]