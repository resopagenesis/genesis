# Generated by Django 4.1.1 on 2022-10-07 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0013_filap_nombre_seccionp_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='usabaseparticular',
            field=models.BooleanField(default=False),
        ),
    ]
