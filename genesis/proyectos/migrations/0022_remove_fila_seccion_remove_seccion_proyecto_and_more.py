# Generated by Django 4.1.1 on 2022-12-13 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0021_alter_fila_seccion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fila',
            name='seccion',
        ),
        migrations.RemoveField(
            model_name='seccion',
            name='proyecto',
        ),
        migrations.DeleteModel(
            name='Columna',
        ),
        migrations.DeleteModel(
            name='Fila',
        ),
        migrations.DeleteModel(
            name='Seccion',
        ),
    ]