# Generated by Django 4.1.1 on 2023-07-16 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0037_remove_crear_despliega_crear_expand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crear',
            name='expand',
        ),
    ]
