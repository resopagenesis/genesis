# Generated by Django 4.1.1 on 2023-02-03 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0024_proyectoobjeto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyectoobjeto',
            name='titulo',
        ),
    ]
