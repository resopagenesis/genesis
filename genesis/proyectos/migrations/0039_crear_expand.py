# Generated by Django 4.1.1 on 2023-07-16 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0038_remove_crear_expand'),
    ]

    operations = [
        migrations.AddField(
            model_name='crear',
            name='expand',
            field=models.BooleanField(default='True'),
        ),
    ]
