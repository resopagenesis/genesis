# Generated by Django 4.0.6 on 2022-08-29 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0008_alter_columna_degradado_alter_seccion_degradado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fila',
            name='degradado',
            field=models.CharField(default='top', max_length=6),
        ),
    ]
