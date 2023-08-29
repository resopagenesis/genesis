from django.db import models
from ckeditor.fields import RichTextField
from proyectos.models import Proyecto

# Create your models here.

class Seccion(models.Model):
    # DATOS GENERALES
    nombre = models.CharField(max_length=30,default='')
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE,related_name='principal')
    color1 = models.CharField(max_length=20,default='transparent')
    color2 = models.CharField(max_length=20,default='transparent')
    degradado = models.CharField(max_length=6,default='top')
    borde = models.BooleanField(default=False)
    # altura = models.SmallIntegerField(default=1000) 
    altura = models.CharField(max_length=20,default='1000px')

    def __str__(self):
        return self.nombre

class Fila(models.Model):
    # DATOS GENERALES
    nombre = models.CharField(max_length=30,default='')
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    altura = models.CharField(max_length=20,default='10%')
    # altura = models.SmallIntegerField(default=10) 
    color1 = models.CharField(max_length=20,default='transparent')
    color2 = models.CharField(max_length=20,default='transparent')
    degradado = models.CharField(max_length=6,default='top')
    borde = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre        

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
    ingresosistema = models.BooleanField(default=False)
    dimensionesimagen = models.CharField(max_length=50, default='100%,100%')
    margeninterno = models.CharField(max_length=50, default='0px')
    
    def __str__(self):
        return self.nombre
