# Generated by Django 4.1.1 on 2023-07-13 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propiedades', '0015_rename_camposfill_propiedad_prefijofill_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='randomfill',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='prefijofill',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]
