# Generated by Django 4.1.1 on 2022-12-06 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0017_proyecto_conroles'),
    ]

    operations = [
        migrations.CreateModel(
            name='DespliegaArbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cambia', models.BooleanField(default=False)),
                ('proyecto', models.IntegerField(default=0)),
            ],
        ),
    ]
