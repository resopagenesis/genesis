# Generated by Django 4.1.1 on 2022-11-22 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0016_remove_columna_borde_remove_columna_color1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='columna',
            name='color1',
            field=models.CharField(default='transparent', max_length=20),
        ),
        migrations.AddField(
            model_name='columna',
            name='color2',
            field=models.CharField(default='transparent', max_length=20),
        ),
        migrations.AddField(
            model_name='columna',
            name='degradado',
            field=models.CharField(default='top', max_length=6),
        ),
    ]
