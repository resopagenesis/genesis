# Generated by Django 4.1.1 on 2023-08-15 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0052_modelo_bordecomentarioborra_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelo',
            name='mayusculastituloborra',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='modelo',
            name='mayusculastituloinserta',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='modelo',
            name='mayusculastituloupdate',
            field=models.BooleanField(default=False),
        ),
    ]