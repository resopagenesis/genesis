# Generated by Django 4.0.6 on 2022-08-19 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0009_proyecto_degradehaciaarriba'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='colorfondomenu',
            field=models.CharField(default='transparent', max_length=100),
        ),
    ]