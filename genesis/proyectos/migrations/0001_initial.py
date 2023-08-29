# Generated by Django 3.2.11 on 2022-01-25 19:41

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Crear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proyectoid', models.IntegerField(default=0)),
                ('aplicacionid', models.IntegerField(default=0)),
                ('modeloid', models.IntegerField(default=0)),
                ('propiedadid', models.IntegerField(default=0)),
                ('reglaid', models.IntegerField(default=0)),
                ('elemento', models.CharField(max_length=1)),
                ('nombre', models.CharField(max_length=30)),
                ('padre', models.CharField(default='', max_length=30)),
                ('primero', models.BooleanField(default='False')),
                ('identa', models.IntegerField(default=0)),
                ('restoidenta', models.IntegerField(default=0)),
                ('posicion', models.IntegerField(default=1)),
                ('ultimoregistro', models.CharField(default='p', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='ProyectoTexto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('texto', ckeditor.fields.RichTextField()),
                ('proyecto', models.IntegerField(default=0)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='proyectos')),
                ('imagenpaginaprincipal', models.ImageField(blank=True, null=True, upload_to='proyectos')),
                ('colorpaginaprincipal', models.CharField(default='transparent', max_length=100)),
                ('imagentitulo', models.ImageField(blank=True, null=True, upload_to='proyectos')),
                ('titulo', models.CharField(blank=True, default='', max_length=30)),
                ('descripcion', models.TextField()),
                ('conseguridad', models.BooleanField(default=False)),
                ('conetiquetaspersonalizacion', models.BooleanField(default=False)),
                ('estadogeneracion', models.SmallIntegerField(default=0)),
                ('menuscontiguos', models.BooleanField(default=False)),
                ('separacionsecciones', models.SmallIntegerField(default=2)),
                ('conbusqueda', models.BooleanField(default=False)),
                ('avatarwidth', models.IntegerField(default=30)),
                ('avatarheight', models.IntegerField(default=30)),
                ('imagentitulowidth', models.IntegerField(default=70)),
                ('imagentituloheight', models.IntegerField(default=30)),
                ('fonttitulo', models.CharField(default='Raleway,20,500', max_length=100)),
                ('colortitulo', models.CharField(default='white', max_length=100)),
                ('altocolumnatitulo', models.IntegerField(default=40)),
                ('numerocolumnatitulo', models.IntegerField(default=8)),
                ('colorcolumnatitulo', models.CharField(default='transparent', max_length=100)),
                ('justificacionhorizontaltitulo', models.CharField(default='c', max_length=1)),
                ('justificacionverticaltitulo', models.CharField(default='c', max_length=1)),
                ('altofilaenizcede', models.IntegerField(default=40)),
                ('colorfilaenizcede', models.CharField(default='#4e4c45', max_length=100)),
                ('numerocolumnaenizquierda', models.IntegerField(default=1)),
                ('altocolumnaenizquierda', models.IntegerField(default=40)),
                ('colorcolumnaenizquierda', models.CharField(default='transparent', max_length=100)),
                ('numerocolumnaenderecha', models.IntegerField(default=1)),
                ('altocolumnaenderecha', models.IntegerField(default=40)),
                ('colorcolumnaenderecha', models.CharField(default='transparent', max_length=100)),
                ('enanchoborde', models.SmallIntegerField(default=1)),
                ('enborde', models.BooleanField(default=False)),
                ('encolorborde', models.CharField(default='black', max_length=100)),
                ('altocolumnalogo', models.IntegerField(default=40)),
                ('colorcolumnalogo', models.CharField(default='transparent', max_length=100)),
                ('numerocolumnalogo', models.IntegerField(default=1)),
                ('justificacionhorizontallogo', models.CharField(default='c', max_length=1)),
                ('justificacionverticallogo', models.CharField(default='c', max_length=1)),
                ('altocolumnalogin', models.IntegerField(default=20)),
                ('numerocolumnalogin', models.IntegerField(default=1)),
                ('colorcolumnalogin', models.CharField(default='transparent', max_length=100)),
                ('altofilabume', models.IntegerField(default=30)),
                ('colorfilabume', models.CharField(default='#f1f3f4', max_length=100)),
                ('numerocolumnabumeizquierda', models.IntegerField(default=1)),
                ('altocolumnabumeizquierda', models.IntegerField(default=30)),
                ('colorcolumnabumeizquierda', models.CharField(default='transparent', max_length=100)),
                ('numerocolumnabumederecha', models.IntegerField(default=1)),
                ('altocolumnabumederecha', models.IntegerField(default=30)),
                ('colorcolumnabumederecha', models.CharField(default='transparent', max_length=100)),
                ('bumeanchoborde', models.SmallIntegerField(default=1)),
                ('bumeborde', models.BooleanField(default=False)),
                ('bumecolorborde', models.CharField(default='black', max_length=100)),
                ('altocolumnabusqueda', models.IntegerField(default=30)),
                ('numerocolumnabusqueda', models.IntegerField(default=3)),
                ('colorcolumnabusqueda', models.CharField(default='transparent', max_length=100)),
                ('altocolumnamenu', models.IntegerField(default=30)),
                ('numerocolumnamenu', models.IntegerField(default=7)),
                ('colorcolumnamenu', models.CharField(default='transparent', max_length=100)),
                ('colormenu', models.CharField(default='#6d6d6d', max_length=100)),
                ('fontmenu', models.CharField(default='Open+Sans,10,400', max_length=100)),
                ('justificacionmenu', models.CharField(default='c', max_length=1)),
                ('altofilamedio', models.IntegerField(default=-100)),
                ('colorfilamedio', models.CharField(default='transparent', max_length=100)),
                ('altocolumnamedioizquierda', models.IntegerField(default=-100)),
                ('numerocolumnamedioizquierda', models.IntegerField(default=1)),
                ('colorcolumnamedioizquierda', models.CharField(default='transparent', max_length=100)),
                ('altocolumnamediocentro', models.IntegerField(default=-100)),
                ('numerocolumnamediocentro', models.IntegerField(default=10)),
                ('colorcolumnamediocentro', models.CharField(default='transparent', max_length=100)),
                ('altocolumnamedioderecha', models.IntegerField(default=-100)),
                ('numerocolumnamedioderecha', models.IntegerField(default=1)),
                ('colorcolumnamedioderecha', models.CharField(default='transparent', max_length=100)),
                ('cenanchoborde', models.SmallIntegerField(default=1)),
                ('cenborde', models.BooleanField(default=False)),
                ('cencolorborde', models.CharField(default='black', max_length=100)),
                ('imagenmedio', models.ImageField(blank=True, null=True, upload_to='proyectos')),
                ('textomedio', models.TextField(blank=True, default='')),
                ('colortextomedio', models.CharField(default='black', max_length=100)),
                ('fonttextomedio', models.CharField(default='Raleway,12,500', max_length=100)),
                ('altofilapie', models.IntegerField(default=70)),
                ('colorfilapie', models.CharField(default='transparent', max_length=100)),
                ('altocolumnapie', models.IntegerField(default=70)),
                ('colorcolumnapie', models.CharField(default='#fdfdfd', max_length=100)),
                ('imagenvolver', models.ImageField(blank=True, null=True, upload_to='proyectos')),
                ('textovolver', models.CharField(blank=True, default='Volver', max_length=30)),
                ('fonttextovolver', models.CharField(default='Arial,10,normal', max_length=100)),
                ('colortextovolver', models.CharField(default='green', max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LicenciaUso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcion', models.IntegerField(default=1)),
                ('inicio', models.DateTimeField()),
                ('expira', models.DateTimeField()),
                ('vigente', models.BooleanField(default='True')),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]