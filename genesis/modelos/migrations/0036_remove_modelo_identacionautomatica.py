# Generated by Django 4.1.1 on 2023-04-11 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0035_remove_modelo_datoinicialx_remove_modelo_fechax_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelo',
            name='identacionautomatica',
        ),
    ]
