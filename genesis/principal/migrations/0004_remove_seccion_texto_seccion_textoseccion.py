# Generated by Django 4.0.6 on 2022-08-29 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_alter_seccion_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seccion',
            name='texto',
        ),
        migrations.AddField(
            model_name='seccion',
            name='textoseccion',
            field=models.TextField(default=''),
        ),
    ]
