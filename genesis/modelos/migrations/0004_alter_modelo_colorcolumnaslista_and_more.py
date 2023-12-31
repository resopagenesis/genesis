# Generated by Django 4.0.6 on 2022-08-28 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0003_alter_modelo_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelo',
            name='colorcolumnaslista',
            field=models.CharField(default='black', max_length=20),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='colorcomentarioborra',
            field=models.CharField(default='black', max_length=20),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='colorcomentarioinserta',
            field=models.CharField(default='black', max_length=20),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='colorcomentariolista',
            field=models.CharField(default='black', max_length=20),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='colorcomentarioupdate',
            field=models.CharField(default='black', max_length=20),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='colorfondocolumnaslista',
            field=models.CharField(default='transparent', max_length=20),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='colorfondotextoborra',
            field=models.CharField(default='transparent', max_length=20),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='colorlabelmodelo',
            field=models.CharField(default='black', max_length=20),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='colorlinknuevomodelo',
            field=models.CharField(default='white', max_length=20),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='colortextoborra',
            field=models.CharField(default='black', max_length=20),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='colortextolista',
            field=models.CharField(default='black', max_length=20),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='colortituloborra',
            field=models.CharField(default='black', max_length=20),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='colortituloinserta',
            field=models.CharField(default='black', max_length=20),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='colortitulolista',
            field=models.CharField(default='black', max_length=20),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='colortituloupdate',
            field=models.CharField(default='black', max_length=20),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='columnaslistaconborde',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='fontlinknuevomodelo',
            field=models.CharField(default='Roboto,14,700', max_length=100),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='fonttituloborra',
            field=models.CharField(default='Roboto,14,700', max_length=100),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='fonttituloinserta',
            field=models.CharField(default='Roboto,14,700', max_length=100),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='fonttitulolista',
            field=models.CharField(default='Roboto,14,700', max_length=100),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='fonttituloupdate',
            field=models.CharField(default='Roboto,14,700', max_length=100),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='linknuevomodelo',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='textolinknuevomodelo',
            field=models.CharField(default='Nuevo Modelo', max_length=30),
        ),
    ]
