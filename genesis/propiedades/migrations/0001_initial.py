# Generated by Django 3.2.11 on 2022-01-25 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modelos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('tipo', models.CharField(default='s', max_length=1)),
                ('foranea', models.CharField(default='nada', max_length=30)),
                ('textobotones', models.CharField(blank=True, max_length=100)),
                ('valorinicial', models.CharField(blank=True, max_length=30)),
                ('largostring', models.SmallIntegerField(default=30)),
                ('textoplaceholder', models.CharField(blank=True, max_length=50)),
                ('etiqueta', models.CharField(blank=True, max_length=100)),
                ('mandatoria', models.BooleanField(default=False)),
                ('noestaenformulario', models.BooleanField(default=False)),
                ('participabusquedalista', models.BooleanField(default=False)),
                ('totaliza', models.BooleanField(default=False)),
                ('enlista', models.BooleanField(default=False)),
                ('enmobile', models.BooleanField(default=False)),
                ('numerocolumnas', models.SmallIntegerField(default=1)),
                ('textocolumna', models.CharField(blank=True, max_length=100)),
                ('justificaciontextocolumna', models.CharField(default='i', max_length=1)),
                ('formatofecha', models.CharField(blank=True, default='', max_length=30)),
                ('enreporte', models.BooleanField(default=False)),
                ('anchoenreporte', models.SmallIntegerField(default=3)),
                ('etiquetaarriba', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelos.modelo')),
            ],
        ),
    ]
