# Generated by Django 4.0.6 on 2022-08-18 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aplicacion',
            name='descripcion',
            field=models.TextField(default='La aplicacion '),
        ),
    ]
