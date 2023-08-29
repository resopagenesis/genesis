# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import datetime

# Create your models here.
class Proyecto(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to='proyectos',blank=True,null=True)
    imagenpaginaprincipal = models.ImageField(upload_to='proyectos',blank=True,null=True)
    colorpaginaprincipal = models.CharField(max_length=100,default='transparent')
    segundocolorpaginaprincipal = models.CharField(max_length=100,default='transparent')
    degradehaciaarriba = models.BooleanField(default=True)
    imagentitulo = models.ImageField(upload_to='proyectos',blank=True,null=True)
    titulo = models.CharField(max_length=30,default='',blank=True)
    descripcion = models.TextField(default='El proyecto ')
    # descripcion = models.TextField(blank=True,default='')
    conseguridad = models.BooleanField(default=False)
    conroles = models.BooleanField(default=False)
    conetiquetaspersonalizacion = models.BooleanField(default=False)
    estadogeneracion = models.SmallIntegerField(default=0)
    menuscontiguos = models.BooleanField(default=False)
    separacionsecciones = models.SmallIntegerField(default=2)
    usabaseparticular = models.BooleanField(default=False)
    
    # Busqueda
    conbusqueda = models.BooleanField(default=False)

    # Tamanio del logo del proyecto
    avatarwidth = models.IntegerField(default=50)
    avatarheight = models.IntegerField(default=50)

    # Tamanio de la imagen del titulo del proyecto
    imagentitulowidth = models.IntegerField(default=70)
    imagentituloheight = models.IntegerField(default=30)
    fonttitulo = models.CharField(max_length=100,default='Raleway,20,500')
    colortitulo = models.CharField(max_length=100,default='black')
    altocolumnatitulo = models.IntegerField(default=80)
    numerocolumnatitulo = models.IntegerField(default=8)
    colorcolumnatitulo = models.CharField(max_length=100,default='transparent')
    justificacionhorizontaltitulo = models.CharField(max_length=1, default='c')
    justificacionverticaltitulo = models.CharField(max_length=1, default='c')

    # altofilaencabezado = models.IntegerField(default=20)
    # altocolumnaencabezado = models.IntegerField(default=20)
    
    # COLUMNA SEPARACION IZQUIERDA PRIMERA FILA

    altofilaenizcede = models.IntegerField(default=80)
    colorfilaenizcede = models.CharField(max_length=100,default='transparent')
    numerocolumnaenizquierda = models.IntegerField(default=1)
    altocolumnaenizquierda = models.IntegerField(default=80)
    colorcolumnaenizquierda = models.CharField(max_length=100,default='transparent')
    # altocolumnaencentro = models.IntegerField(default=20)

    # COLUMNA SEPARACION DERECHA PRIMERA FILA
    # numerocolumnaencentro = models.IntegerField(default=4)
    numerocolumnaenderecha = models.IntegerField(default=1)
    altocolumnaenderecha = models.IntegerField(default=80)
    colorcolumnaenderecha = models.CharField(max_length=100,default='transparent')

    enanchoborde = models.SmallIntegerField(default=1)
    enborde = models.BooleanField(default=True)
    encolorborde = models.CharField(max_length=100,default='#e0e0e0')

    # altofilalotilo = models.IntegerField(default=20)

    # LOGO
    altocolumnalogo = models.IntegerField(default=80)
    colorcolumnalogo = models.CharField(max_length=100,default='transparent')
    numerocolumnalogo = models.IntegerField(default=1)
    justificacionhorizontallogo = models.CharField(max_length=1, default='c')
    justificacionverticallogo = models.CharField(max_length=1, default='c')

    # COLUMNA LOGIN PRIMERA FILA
    altocolumnalogin = models.IntegerField(default=80)
    numerocolumnalogin = models.IntegerField(default=1)
    colorcolumnalogin = models.CharField(max_length=100,default='transparent')

    altofilabume = models.IntegerField(default=60)
    colorfilabume = models.CharField(max_length=100,default='transparent')
    
    # COLUMAN SEPARACION IZQUIERDA SEGUNDA FILA
    numerocolumnabumeizquierda = models.IntegerField(default=1)
    altocolumnabumeizquierda = models.IntegerField(default=60)
    colorcolumnabumeizquierda = models.CharField(max_length=100,default='transparent')
    # altocolumnaencentro = models.IntegerField(default=20)

    # COLUMNA SEPARACION DERECHA SEGUNA FILA
    # numerocolumnaencentro = models.IntegerField(default=4)
    numerocolumnabumederecha = models.IntegerField(default=1)
    altocolumnabumederecha = models.IntegerField(default=60)
    colorcolumnabumederecha = models.CharField(max_length=100,default='transparent')


    bumeanchoborde = models.SmallIntegerField(default=1)
    bumeborde = models.BooleanField(default=False)
    bumecolorborde = models.CharField(max_length=100,default='#e0e0e0')

    # COLUMNA BUSQUEDA
    altocolumnabusqueda = models.IntegerField(default=60)
    numerocolumnabusqueda = models.IntegerField(default=3)
    colorcolumnabusqueda = models.CharField(max_length=100,default='transparent')

    # COLUMNA MENU
    altocolumnamenu = models.IntegerField(default=60)
    numerocolumnamenu = models.IntegerField(default=7)
    colorcolumnamenu = models.CharField(max_length=100,default='transparent')
    colorfondomenu = models.CharField(max_length=100,default='transparent')
    colormenu = models.CharField(max_length=100,default='black')
    fontmenu = models.CharField(max_length=100,default='Open+Sans,12,400')
    justificacionmenu = models.CharField(max_length=1, default='c')

    # COLMNAS TERCERA FILA
    altofilamedio = models.IntegerField(default=-100)
    colorfilamedio = models.CharField(max_length=100,default='transparent')
    altocolumnamedioizquierda = models.IntegerField(default=-100)
    numerocolumnamedioizquierda = models.IntegerField(default=1)
    colorcolumnamedioizquierda = models.CharField(max_length=100,default='transparent')
    altocolumnamediocentro = models.IntegerField(default=-100)
    numerocolumnamediocentro = models.IntegerField(default=10)
    colorcolumnamediocentro = models.CharField(max_length=100,default='transparent')
    altocolumnamedioderecha = models.IntegerField(default=-100)
    numerocolumnamedioderecha = models.IntegerField(default=1)
    colorcolumnamedioderecha = models.CharField(max_length=100,default='transparent')
    
    cenanchoborde = models.SmallIntegerField(default=1)
    cenborde = models.BooleanField(default=False)
    cencolorborde = models.CharField(max_length=100,default='#e0e0e0')

    imagenmedio = models.ImageField(upload_to='proyectos',blank=True,null=True)
    textomedio = models.TextField(blank=True,default='')
    colortextomedio = models.CharField(max_length=100,default='black')
    fonttextomedio = models.CharField(max_length=100,default='Roboto,12,500')

    altofilapie = models.IntegerField(default=70)
    colorfilapie = models.CharField(max_length=100,default='transparent')
    altocolumnapie = models.IntegerField(default=70)
    colorcolumnapie = models.CharField(max_length=100,default='transparent')

    # Imagen de volver
    imagenvolver = models.ImageField(upload_to='proyectos',blank=True,null=True)
    textovolver = models.CharField(max_length=30,blank=True,default='Volver')
    fonttextovolver = models.CharField(max_length=100,default='Open+Sans,12,400')
    colortextovolver = models.CharField(max_length=20,default='black')

    # Reportes
    # primeralinea = models.DecimalField(decimal_places=2, default=0, max_digits=5)    
    # maxlineas = models.IntegerField(default=49)
    # anchologo = models.DecimalField(decimal_places=2, default=0, max_digits=5)    
    # altologo = models.DecimalField(decimal_places=2, default=0, max_digits=5)    
    # posxlogo = models.DecimalField(decimal_places=2, default=0, max_digits=5)    
    # posylogo = models.DecimalField(decimal_places=2, default=0, max_digits=5)    
    # posxnombre = models.DecimalField(decimal_places=2, default=0, max_digits=5)    
    # posynombre = models.DecimalField(decimal_places=2, default=0, max_digits=5)    
    # iniciolineax = models.DecimalField(decimal_places=2, default=0, max_digits=5)    
    # finallineax = models.DecimalField(decimal_places=2, default=0, max_digits=5)    
    # iniciolineay = models.DecimalField(decimal_places=2, default=0, max_digits=5)    
    # grosorlinea = models.DecimalField(decimal_places=2, default=0, max_digits=5)    
    # piex = models.DecimalField(decimal_places=2, default=0, max_digits=5)    
    # piey = models.DecimalField(decimal_places=2, default=0, max_digits=5)    
    # lineapiex = models.DecimalField(decimal_places=2, default=0, max_digits=5)    
    # lineapiey = models.DecimalField(decimal_places=2, default=0, max_digits=5)    

    # colorfilaencabezado = models.CharField(max_length=100,default='transparent')
    # colorcolumnaencabezado = models.CharField(max_length=100,default='transparent')
    # colorcolumnaencentro = models.CharField(max_length=100,default='transparent')
    # colorfilalotilo = models.CharField(max_length=100,default='transparent')

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")


    def __str__(self):
        return self.nombre

class Crear(models.Model):
    proyectoid = models.IntegerField(default=0)
    aplicacionid = models.IntegerField(default=0)
    modeloid = models.IntegerField(default=0)
    propiedadid = models.IntegerField(default=0)
    reglaid = models.IntegerField(default=0)
    elemento = models.CharField(max_length=1)
    nombre = models.CharField(max_length=30)
    padre = models.CharField(max_length=30,default='')
    primero = models.BooleanField(default='False')
    identa = models.IntegerField(default=0)
    restoidenta = models.IntegerField(default=0)
    posicion = models.IntegerField(default=1)
    ultimoregistro = models.CharField(max_length=1,default='p')
    expand = models.CharField(max_length=8,default='expand')

    def __str__(self):
        return self.elemento + ' ' + self.nombre        

# opciones: 1=gratuito un mes, 2=trimestral, 3=semestral, 4=anual
class LicenciaUso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    opcion = models.IntegerField(default=1)
    inicio = models.DateTimeField()
    expira = models.DateTimeField()
    vigente = models.BooleanField(default='True')
    precio = models.DecimalField(max_digits=5, decimal_places=2,default=0)

    def __str__(self):
        return self.usuario.username        

class ProyectoTexto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=20)
    texto_texto = RichTextField()
    proyecto = models.IntegerField(default=0)
    lineacontigua = models.BooleanField(default='True')

    def __str__(self):
        return self.titulo    

class ProyectoJson(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=20)
    texto = RichTextField()
    proyecto = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo    

class ProyectoObjeto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto_objeto = RichTextField()
    proyecto = models.IntegerField(default=0)

    def __str__(self):
        return self.textoobjetos

class Seccion(models.Model):
    # DATOS GENERALES
    nombre = models.CharField(max_length=30,default='')
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='proyectos')
    color1 = models.CharField(max_length=20,default='transparent')
    color2 = models.CharField(max_length=20,default='transparent')
    degradado = models.CharField(max_length=6,default='top')
    borde = models.BooleanField(default=False)
    # altura = models.SmallIntegerField(default=1000) 
    altura = models.CharField(max_length=20,default='auto')
    imagen = models.ImageField(upload_to='main',blank=True,null=True)

    def __str__(self):
        return self.nombre

class Fila(models.Model):
    # DATOS GENERALES
    nombre = models.CharField(max_length=30,default='')
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE,related_name='Seccion')
    # altura = models.SmallIntegerField(default=10) 
    altura = models.CharField(max_length=20,default='100px')
    color1 = models.CharField(max_length=20,default='transparent')
    color2 = models.CharField(max_length=20,default='transparent')
    degradado = models.CharField(max_length=6,default='top')
    borde = models.BooleanField(default=False)

    def __str__(self):
        return self.altura        

class Columna(models.Model):
    # DATOS GENERALES
    nombre = models.CharField(max_length=30,default='')
    fila = models.ForeignKey(Fila, on_delete=models.CASCADE)
    color1 = models.CharField(max_length=20,default='transparent')
    color2 = models.CharField(max_length=20,default='transparent')
    degradado = models.CharField(max_length=6,default='top')
    imagen = models.ImageField(upload_to='main',blank=True,null=True)
    secciones = models.SmallIntegerField(default=10) 
    textocolumna = models.TextField(default='',blank=True,null=True)
    fonttexto = models.CharField(max_length=100,default='Roboto,14,700')
    colortexto = models.CharField(max_length=20,default='black')
    justificacionhorizontaltexto = models.CharField(max_length=6, default='center')
    justificacionverticaltexto = models.CharField(max_length=6, default='center')
    borde = models.BooleanField(default=False)
    funcion = models.CharField(max_length=1,default='o')
    dimensionesimagen = models.CharField(max_length=50, default='100%,100%')
    margeninterno = models.CharField(max_length=50, default='0px')

    def __str__(self):
        return self.nombre

class DespliegaArbol(models.Model):
    cambia = models.BooleanField(default=False)
    proyecto = models.IntegerField(default=0)

    def __str__(self):
        return self.cambia    