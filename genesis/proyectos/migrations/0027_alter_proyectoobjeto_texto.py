# Generated by Django 4.1.1 on 2023-02-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0026_alter_proyectoobjeto_texto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectoobjeto',
            name='texto',
            field=models.CharField(max_length=10),
        ),
    ]
