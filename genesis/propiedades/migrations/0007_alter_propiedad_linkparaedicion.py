# Generated by Django 4.0.6 on 2022-08-19 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propiedades', '0006_propiedad_linkparaedicion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='linkparaedicion',
            field=models.BooleanField(default=False),
        ),
    ]
