# Generated by Django 4.0.6 on 2022-08-18 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0004_proyectojson'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyectotexto',
            name='lineacontigua',
            field=models.BooleanField(default='True'),
        ),
    ]
