# Generated by Django 4.0.6 on 2022-08-18 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0002_modelo_font_modelo_font_columnas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelo',
            name='descripcion',
            field=models.TextField(default='El modelo '),
        ),
    ]
