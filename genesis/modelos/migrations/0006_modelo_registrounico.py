# Generated by Django 4.0.6 on 2022-09-01 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0005_alter_modelo_linknuevomodelo'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelo',
            name='registrounico',
            field=models.BooleanField(default=False),
        ),
    ]
