# Generated by Django 4.1.1 on 2023-08-03 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0047_alter_fila_altura_alter_seccion_altura'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelo',
            name='saltopagina',
            field=models.BooleanField(default=False),
        ),
    ]