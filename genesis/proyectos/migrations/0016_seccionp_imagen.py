# Generated by Django 4.1.1 on 2022-10-27 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0015_alter_columnap_justificacionhorizontaltexto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='seccionp',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='main'),
        ),
    ]
