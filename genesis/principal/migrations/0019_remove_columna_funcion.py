# Generated by Django 4.1.1 on 2022-12-13 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0018_columna_funcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='columna',
            name='funcion',
        ),
    ]
