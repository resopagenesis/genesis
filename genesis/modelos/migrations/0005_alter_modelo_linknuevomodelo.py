# Generated by Django 4.0.6 on 2022-08-31 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0004_alter_modelo_colorcolumnaslista_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelo',
            name='linknuevomodelo',
            field=models.BooleanField(default=True),
        ),
    ]
