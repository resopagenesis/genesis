# Generated by Django 4.0.6 on 2022-08-19 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0007_alter_proyecto_colortitulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='segundocolorpaginaprincipal',
            field=models.CharField(default='transparent', max_length=100),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='altocolumnaenderecha',
            field=models.IntegerField(default=60),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='altocolumnaenizquierda',
            field=models.IntegerField(default=60),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='altofilaenizcede',
            field=models.IntegerField(default=60),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='avatarheight',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='avatarwidth',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='colorfilaenizcede',
            field=models.CharField(default='transparent', max_length=100),
        ),
    ]
