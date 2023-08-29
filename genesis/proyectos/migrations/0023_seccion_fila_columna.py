# Generated by Django 4.1.1 on 2022-12-15 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0022_remove_fila_seccion_remove_seccion_proyecto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=30)),
                ('color1', models.CharField(default='transparent', max_length=20)),
                ('color2', models.CharField(default='transparent', max_length=20)),
                ('degradado', models.CharField(default='top', max_length=6)),
                ('borde', models.BooleanField(default=False)),
                ('altura', models.SmallIntegerField(default=1000)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='main')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyectos', to='proyectos.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Fila',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=30)),
                ('altura', models.SmallIntegerField(default=10)),
                ('color1', models.CharField(default='transparent', max_length=20)),
                ('color2', models.CharField(default='transparent', max_length=20)),
                ('degradado', models.CharField(default='top', max_length=6)),
                ('borde', models.BooleanField(default=False)),
                ('seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Seccion', to='proyectos.seccion')),
            ],
        ),
        migrations.CreateModel(
            name='Columna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=30)),
                ('color1', models.CharField(default='transparent', max_length=20)),
                ('color2', models.CharField(default='transparent', max_length=20)),
                ('degradado', models.CharField(default='top', max_length=6)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='main')),
                ('secciones', models.SmallIntegerField(default=10)),
                ('textocolumna', models.TextField(blank=True, default='', null=True)),
                ('fonttexto', models.CharField(default='Roboto,14,700', max_length=100)),
                ('colortexto', models.CharField(default='black', max_length=20)),
                ('justificacionhorizontaltexto', models.CharField(default='c', max_length=1)),
                ('justificacionverticaltexto', models.CharField(default='c', max_length=1)),
                ('borde', models.BooleanField(default=False)),
                ('funcion', models.CharField(default='o', max_length=1)),
                ('fila', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.fila')),
            ],
        ),
    ]
