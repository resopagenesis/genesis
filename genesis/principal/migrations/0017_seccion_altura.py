# Generated by Django 4.0.6 on 2022-08-30 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0016_columna_ingresosistema'),
    ]

    operations = [
        migrations.AddField(
            model_name='seccion',
            name='altura',
            field=models.SmallIntegerField(default=1000),
        ),
    ]
