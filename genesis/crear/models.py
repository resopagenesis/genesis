from django.db import models

from aplicaciones.models import Aplicacion
from proyectos.models import Proyecto

# Create your models here.

class ErroresCreacion(models.Model):
    proyecto = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50,default='')
    etapa = models.CharField(max_length=50)
    paso = models.TextField(default='')
    descripcion = models.TextField(default='')
    severo = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    def __str__(self):
        return self.etapa

class Reporte(models.Model):
    reportesize = models.CharField(max_length=1,default='l')
    orientacion = models.CharField(max_length=1,default='p')
    logox = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    logoy = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    titulox = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    tituloy = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    lineaencabezadox = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    lineaencabezadoy = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    nombrex = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    nombrey = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    fechax = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    fechay = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    lineacolumnasx = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    lineacolumnasy = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    lineacolumnaix = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    lineacolumnaiy = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    nombrecolumnasy = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    colorcolumna = models.CharField(max_length=100,default='black')
    fontcolumna = models.CharField(max_length=100,default='Helvetica,12,400')
    fontdatos = models.CharField(max_length=100,default='Helvetica,12,400')
    lineapiex = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    lineapiey = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    pagenumberx = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    pagenumbery = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    numerolineaspp = models.IntegerField(default='1')
    numerolineassp = models.IntegerField(default='1')
    numerolineasocupatitulohijo = models.IntegerField(default='1')
    primeralineapp = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    primeralineasp = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    colornombre = models.CharField(max_length=100,default='black')
    fontnombre = models.CharField(max_length=100,default='Helvetica,30,400')
    colortitulo = models.CharField(max_length=100,default='black')
    fonttitulo = models.CharField(max_length=100,default='Helvetica,24,400')
    colorfecha = models.CharField(max_length=100,default='red')
    fontfecha = models.CharField(max_length=100,default='Helvetica,12,400')
    colorpie = models.CharField(max_length=100,default='black')
    fontpie = models.CharField(max_length=100,default='Helvetica,8,400')
    colortitulohijo = models.CharField(max_length=100,default='black')
    fonttitulohijo = models.CharField(max_length=100,default='Helvetica,24,400')
    colorcolumnahijo = models.CharField(max_length=100,default='black')
    fontcolumnahijo = models.CharField(max_length=100,default='Helvetica,12,400')
    identacionposdatoshijo = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    separacionlineasuperiorcolumnas = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    separacioncolumnaslineainferior = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    grosorlineacolumnas = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    grosorlineaencabezado = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    altologo = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    anchologo = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    saltolineadatospadreiniciotitulohijo = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    posxdatospadre = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    saltolineainferiorcolumnadato = models.DecimalField(decimal_places=2, default=0, max_digits=5)

    def __str__(self):
        return self.reportesize

class ReporteNuevo(models.Model):
    
    reportesize = models.CharField(max_length=1,default='l')
    orientacion = models.CharField(max_length=1,default='p')
    posxlogo = models.DecimalField(decimal_places=2, default=1, max_digits=5)
    posylogo = models.DecimalField(decimal_places=2, default=25.70, max_digits=5)
    iniciolineax = models.DecimalField(decimal_places=2, default=1, max_digits=5)
    finallineax = models.DecimalField(decimal_places=2, default=20.50, max_digits=5)
    posxnombre = models.DecimalField(decimal_places=2, default=15, max_digits=5)
    posynombre = models.DecimalField(decimal_places=2, default=26, max_digits=5)
    iniciolineay = models.DecimalField(decimal_places=2, default=25.30, max_digits=5)
    lineapiex = models.DecimalField(decimal_places=2, default=20.50, max_digits=5)
    lineapiey = models.DecimalField(decimal_places=2, default=1.70, max_digits=5)
    piex = models.DecimalField(decimal_places=2, default=20.50, max_digits=5)
    piey = models.DecimalField(decimal_places=2, default=1, max_digits=5)
    maxlineas = models.IntegerField(default=49)
    primeralinea = models.DecimalField(decimal_places=2, default=24.50, max_digits=5)
    grosorlinea = models.DecimalField(decimal_places=2, default=0.9, max_digits=5)
    altologo = models.DecimalField(decimal_places=2, default=1.5, max_digits=5)
    anchologo = models.DecimalField(decimal_places=2, default=1.5, max_digits=5)

    def __str__(self):
        return self.reportesize


class TextFiles(models.Model):
    file = models.CharField(max_length=100)
    texto = models.TextField(default='')

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    def __str__(self):
        return self.file
    
class formatoSeccion(models.Model):
    # base principal
    
    # seccion
    ubicacion = models.CharField(max_length=1,default='p')
    color1 = models.CharField(max_length=20,default='transparent')
    color2 = models.CharField(max_length=20,default='transparent')
    degradado = models.CharField(max_length=6,default='top')
    borde = models.BooleanField(default=False)
    altura = models.SmallIntegerField(default=1000) 


class formatoFila(models.Model):
    # base principal
    
    # fila
    seccion = models.ForeignKey(formatoSeccion, on_delete=models.CASCADE)    
    altura = models.SmallIntegerField(default=1000) 
    color1 = models.CharField(max_length=20,default='transparent')
    color2 = models.CharField(max_length=20,default='transparent')
    degradado = models.CharField(max_length=6,default='top')
    borde = models.BooleanField(default=False)

class formatoColumna(models.Model):
    # base principal
    
    # columna
    fila = models.ForeignKey(formatoFila, on_delete=models.CASCADE)    
    altura = models.SmallIntegerField(default=1000) 
    color1 = models.CharField(max_length=20,default='transparent')
    color2 = models.CharField(max_length=20,default='transparent')
    degradado = models.CharField(max_length=6,default='top')
    font_texto = models.CharField(max_length=100,default='Roboto,14,700')
    color_texto = models.CharField(max_length=20,default='black')
    justificacion_horizontal_texto = models.CharField(max_length=1, default='c')
    justificacion_vertical_texto = models.CharField(max_length=1, default='c')
    borde = models.BooleanField(default=False)

# class formatoGeneral(models.Model):
#     # lista modelo
#     font_titulo_lista
#     color_titulo_lista
#     color_fondo_titulo_lista
#     alto_titulo_lista
#     titulo_mayusculas
#     justificacion_horizontal_titulo_lista
#     justificacion_vertical_titulo_lista
#     font_comentario_lista
#     color_comentario_lista
#     color_fondo_comentario_lista
#     columnas_mayusculas
#     altura_columna
#     color_fondo_columna
#     font_columna
#     columna_borde
#     font_texto
#     color_texto
#     color_fondo_texto
#     font_editar_borrar
#     color_editar_borrar

#     # inserta

#     font_titulo_inserta
#     color_titulo_inserta
#     color_fondo_titulo_inserta
#     color_fondo_fila_titulo_inserta
#     altura_titulo_inserta
#     justificacion_vertical_titulo_inserta
#     justificacion_horizontal_titulo_inserta
#     font_comentario_inserta
#     color_comentario_inserta
#     color_fondo_comentario_inserta
#     numero_secciones_izquierda_inserta
#     numero_secciones_centro_inserta
#     numero_secciones_derecha_inserta

#     # modifica modelo

#     font_titulo_modifica
#     color_titulo_modifica
#     color_fondo_titulo_modifica
#     color_fondo_fila_titulo_modifica
#     altura_titulo_modifica
#     justificacion_vertical_titulo_modifica
#     justificacion_horizontal_titulo_modifica
#     font_comentario_modifica
#     color_comentario_modifica
#     color_fondo_comentario_modifica
#     numero_secciones_izquierda_modifica
#     numero_secciones_centro_modifica
#     numero_secciones_derecha_modifica
#     hijos_contiguos

#     # borra modelo

#     font_titulo_borra
#     color_titulo_borra
#     color_fondo_titulo_borra
#     color_fondo_fila_titulo_borra
#     altura_titulo_borra
#     justificacion_vertical_titulo_borra
#     justificacion_horizontal_titulo_borra
#     font_comentario_borra
#     color_comentario_borra
#     color_fondo_comentario_borra
#     font_texto_borrado
#     color_texto_borrado
#     color_fondo_texto_borrado
#     numero_secciones_izquierda_modifica
#     numero_secciones_centro_modifica
#     numero_secciones_derecha_modifica
