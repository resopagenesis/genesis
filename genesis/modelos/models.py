from django.db import models
from ckeditor.fields import RichTextField
from aplicaciones.models import Aplicacion
from proyectos.models import Proyecto

# Create your models here.

class Modelo(models.Model):
    # DATOS GENERALES
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(default='El modelo ')
    padre = models.CharField(max_length=30,default='nada')
    nombreself = models.CharField(max_length=100, default='')
    nombreborrar = models.CharField(max_length=100,default='')
    aplicacion = models.ForeignKey(Aplicacion, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    textoopcionmenu = models.CharField(max_length=30, blank=True,default='')
    modeloenmenu = models.BooleanField(default=True)    
    sinbasedatos = models.BooleanField(default=False)   
    imagenmenu = models.ImageField(upload_to='proyectos',blank=True,null=True)
    tooltip = models.CharField(max_length=30,blank=True,default='')
    ordengeneracion = models.SmallIntegerField(default=1) 
    ultimoregistro = models.CharField(max_length=1,blank=True,default='p')
    usabaseparticular = models.BooleanField(default=False)
    identa = models.SmallIntegerField(default=1) 

    # LISTA
    # Titulo
    titulolista = models.CharField(max_length=30,blank=True,default='Lista de registros')
    fonttitulolista = models.CharField(max_length=100,default='Arvo,20,700')
    colorfondotitulolista = models.CharField(max_length=20,default='transparent')
    colortitulolista = models.CharField(max_length=20,default='black')
    altotitulolista = models.SmallIntegerField(default=50)  
    mayusculastitulolista = models.BooleanField(default=False)  
    justificacionverticaltitulolista = models.CharField(max_length=1,default='c')
    justificacionhorizontaltitulolista = models.CharField(max_length=1,default='i')
    bordeexteriorlista = models.BooleanField(default=True) 

    # Comentario
    fontcomentariolista = models.CharField(max_length=100,default='Roboto,10,normal')
    comentariolista = models.CharField(max_length=200,default='',blank=True)
    colorfondocomentariolista = models.CharField(max_length=20,default='#f5f5f5')
    colorcomentariolista = models.CharField(max_length=20,default='black')
    bordecomentariolista = models.BooleanField(default=True) 

    # Columnas
    mayusculascolumnas = models.BooleanField(default=False) 
    altocolumnas = models.SmallIntegerField(default=30) 
    colorfondocolumnaslista = models.CharField(max_length=20,default='#e8eaed')
    colorcolumnaslista = models.CharField(max_length=20,default='#505050')
    fontcolumnaslista = models.CharField(max_length=100,default='Roboto,11,700')
    columnaslistaconborde = models.BooleanField(default=True)  

    # Datos
    fonttextolista = models.CharField(max_length=100,default='Arial,10,normal')
    colorfondotextolista = models.CharField(max_length=20,default='transparent')
    colortextolista = models.CharField(max_length=20,default='black')
    buscadorlista = models.BooleanField(default=False)  

    # Editar Borrar
    fonteditarborrar = models.CharField(max_length=100,default='Arial,10,normal')
    coloreditarborrar = models.CharField(max_length=20,default='blue')
    textoeditarborrar = models.CharField(max_length=30,default='Edita,Borra')

    # Nuevo modelo
    fontlinknuevomodelo = models.CharField(max_length=100,default='Roboto,14,700')
    colorlinknuevomodelo = models.CharField(max_length=20,default='white')
    colorbotonlinknuevomodelo = models.CharField(max_length=20,default='primary')
    textolinknuevomodelo = models.CharField(max_length=30,default='Nuevo Modelo')
    linknuevomodelo = models.BooleanField(default=True) 

    # reporte
    reportsize = models.CharField(max_length=20,default='L')
    reportorientation = models.CharField(max_length=20,default='P')
    # titulox = models.DecimalField(decimal_places=2, default=10.5, max_digits=5)    
    # fechax = models.DecimalField(decimal_places=2, default=10.5, max_digits=5)    
    # lineaix = models.DecimalField(decimal_places=2, default=1, max_digits=5)    
    # lineafx = models.DecimalField(decimal_places=2, default=20.50, max_digits=5)    
    grosorlinea = models.DecimalField(decimal_places=2, default=0.3, max_digits=5)    
    # datoinicialx = models.DecimalField(decimal_places=2, default=1.5, max_digits=5)    
    # identacionautomatica = models.BooleanField(default=True) 
    dimensioneslogo = models.CharField(max_length=15,default='15,15')

    # Reporte platypus
    margenes = models.CharField(max_length=20,default='20,20,20,20')
    font_titulo = models.CharField(max_length=100,default='Helvetica,10,500')
    # font_titulo_size = models.SmallIntegerField(default=10)
    font_columnas = models.CharField(max_length=100,default='Helvetica,10,500')
    # font_columnas_size = models.SmallIntegerField(default=10)
    font = models.CharField(max_length=100,default='Helvetica,10,500')
    # font_size = models.SmallIntegerField(default=10)
    font_encabezado = models.CharField(max_length=100,default='Helvetica,10,500')
    # font_encabezado_size = models.SmallIntegerField(default=16)
    font_totales = models.CharField(max_length=100,default='Helvetica,10,500')
    saltopagina = models.BooleanField(default=False) 
    grosorlineaencabezado = models.DecimalField(decimal_places=2, default=0.5, max_digits=5)    
    colortitulo = models.CharField(max_length=20,default='black')
    colorcolumnas = models.CharField(max_length=20,default='black')
    colortexto = models.CharField(max_length=20,default='black')
    colorencabezado = models.CharField(max_length=20,default='black')
    colortotales = models.CharField(max_length=20,default='black')

    # INSERTA
    # titulo
    tituloinserta = models.CharField(max_length=30,default='Nuevo Modelo')
    fonttituloinserta = models.CharField(max_length=100,default='Arvo,20,700')
    colortituloinserta = models.CharField(max_length=20,default='black')
    colorfondotituloinserta = models.CharField(max_length=20,default='transparent')
    colorfondofilatituloinserta = models.CharField(max_length=20,default='transparent')
    altofilatituloinserta = models.SmallIntegerField(default=50)    
    justificacionverticaltituloinserta = models.CharField(max_length=1,default='c')
    justificacionhorizontaltituloinserta = models.CharField(max_length=1,default='i')
    mayusculastituloinserta = models.BooleanField(default=False)  
    bordeexteriorinserta = models.BooleanField(default=False) 
    bordeformularioinserta = models.BooleanField(default=True) 

    # Comentario inserta
    colorfondocomentarioinserta = models.CharField(max_length=20,default='#f5f5f5')
    colorcomentarioinserta = models.CharField(max_length=20,default='black')
    fontcomentarioinserta = models.CharField(max_length=100,default='Open+Sans,10,normal')
    comentarioinserta = models.CharField(max_length=200,default='',blank=True)
    bordecomentarioinserta = models.BooleanField(default=True) 

    # Diagrama
    numerocolumnasizquierdainserta = models.SmallIntegerField(default=1)    
    numerocolumnasmodeloinserta = models.SmallIntegerField(default=10)  
    numerocolumnasderechainserta = models.SmallIntegerField(default=1)  

    # UPDATE
    # titulo
    tituloupdate = models.CharField(max_length=30,default='Modelo a editar: ')
    fonttituloupdate = models.CharField(max_length=100,default='Arvo,20,700')
    colortituloupdate = models.CharField(max_length=20,default='black')
    colorfondotituloupdate = models.CharField(max_length=20,default='transparent')
    colorfondofilatituloupdate = models.CharField(max_length=20,default='transparent')
    altofilatituloupdate = models.SmallIntegerField(default=50) 
    justificacionverticaltituloupdate = models.CharField(max_length=1,default='c')
    justificacionhorizontaltituloupdate = models.CharField(max_length=1,default='i')
    mayusculastituloupdate = models.BooleanField(default=False)  
    bordeexteriorupdate = models.BooleanField(default=False) 
    bordeformularioupdate = models.BooleanField(default=False) 
    
    # Comentario update
    comentarioupdate = models.CharField(max_length=200,default='',blank=True)
    colorfondocomentarioupdate = models.CharField(max_length=20,default='#f5f5f5')
    fontcomentarioupdate = models.CharField(max_length=100,default='Open+Sans,10,normal')
    colorcomentarioupdate = models.CharField(max_length=20,default='black')
    bordecomentarioupdate = models.BooleanField(default=True) 

    # Diagrama
    numerocolumnasizquierdaupdate = models.SmallIntegerField(default=1)
    numerocolumnasderechaupdate = models.SmallIntegerField(default=1)
    numerocolumnasmodeloupdate = models.SmallIntegerField(default=10)

    # Labels
    fontlabelmodelo = models.CharField(max_length=100,default='Arial,10,bold')
    colorlabelmodelo = models.CharField(max_length=20,default='black')
    controlesautomaticos = models.BooleanField(default=False)   

    # BORRAR
    # titulo
    tituloborra = models.CharField(max_length=30,blank=True,default='Borrar el modelo')
    fonttituloborra = models.CharField(max_length=100,default='Arvo,20,700')
    colortituloborra = models.CharField(max_length=20,default='black')
    colorfondotituloborra = models.CharField(max_length=20,default='transparent')
    colorfondofilatituloborra = models.CharField(max_length=20,default='transparent')
    altofilatituloborra = models.SmallIntegerField(default=50)  
    justificacionverticaltituloborra = models.CharField(max_length=1,default='c')
    justificacionhorizontaltituloborra = models.CharField(max_length=1,default='i')
    mayusculastituloborra = models.BooleanField(default=False)  
    bordeexteriorborra = models.BooleanField(default=False) 

    # Comentario borra
    colorfondocomentarioborra = models.CharField(max_length=20,default='#f5f5f5')
    colorcomentarioborra = models.CharField(max_length=20,default='black')
    fontcomentarioborra = models.CharField(max_length=100,default='Open+Sans,10,normal')
    comentarioborra = models.CharField(max_length=200,default='',blank=True)
    bordecomentarioborra = models.BooleanField(default=True) 

    # Texto borra
    colorfondotextoborra = models.CharField(max_length=20,default='transparent')
    colortextoborra = models.CharField(max_length=20,default='black')
    fonttextoborra = models.CharField(max_length=100,default='Arial,10,normal')
    textoborra = models.CharField(max_length=200,default='Borrar el modelo:',blank=True)

    # Boton borra
    textobotonborra = models.CharField(max_length=30,blank=True,default='Borrar')

    # Diagrama
    numerocolumnasizquierdaborra = models.SmallIntegerField(default=1)
    numerocolumnasderechaborra = models.SmallIntegerField(default=1)
    numerocolumnasmodeloborra = models.SmallIntegerField(default=10)

    # HIJOS
    hijoscontiguos = models.BooleanField(default=False) 
    numerocolumnashijosupdate = models.SmallIntegerField(default=5)

    # SEGURIDAD
    listastaff = models.BooleanField(default=False) 
    listalogin = models.BooleanField(default=False) 
    crearstaff = models.BooleanField(default=False) 
    crearlogin = models.BooleanField(default=False) 
    editarstaff = models.BooleanField(default=False)    
    editarlogin = models.BooleanField(default=False)    
    borrarstaff = models.BooleanField(default=False)    
    borrarlogin = models.BooleanField(default=False)    

    # Columnas de labels y controles
    numerocolumnaslabels = models.SmallIntegerField(default=5)
    numerocolumnascontroles = models.SmallIntegerField(default=7)

    # registro unico
    registrounico = models.BooleanField(default=False) 
    # El link de editar esta en la lista de registros
    editarenlista = models.BooleanField(default=True)

    # La edicion puede hacerse por treeview del modelo y sus dependientes 
    treeview = models.BooleanField(default=False) 
    colorfondotreeview = models.CharField(max_length=20,default='#0375B4')
    colortreeview = models.CharField(max_length=20,default='white')
    fonttreeview = models.CharField(max_length=100,default='Open+Sans,8,normal')
    columnastreeview = models.SmallIntegerField(default=3)

    # nivel para identacion
    nivelidentacion = models.SmallIntegerField(default=1)
    ultimoregistro = models.CharField(max_length=1,default='p')

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    def __str__(self):
        return self.nombre

class Seccion(models.Model):
    # DATOS GENERALES
    nombre = models.CharField(max_length=30,default='')
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    color1 = models.CharField(max_length=20,default='transparent')
    color2 = models.CharField(max_length=20,default='transparent')
    degradado = models.CharField(max_length=6,default='top')
    borde = models.BooleanField(default=False)
    # altura = models.SmallIntegerField(default=1000) 
    altura = models.CharField(max_length=20,default='1000px')
    imagen = models.ImageField(upload_to='main',blank=True,null=True)

    def __str__(self):
        return self.modelo.nombre

class Fila(models.Model):
    # DATOS GENERALES
    nombre = models.CharField(max_length=30,default='')
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
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

class ZonaReporte(models.Model):
    nombre = models.CharField(max_length=30,default='')
    texto = models.TextField()
    modeloid = models.IntegerField(default=0)

    def __str__(self):
        return str(self.modeloid)
    
class ZonaReporteAdHoc(models.Model):
    texto = models.TextField()
    modeloid = models.IntegerField(default=0)

    def __str__(self):
        return str(self.modeloid)    
    
class ReporteAdHocObjeto(models.Model):
    nombre = models.CharField(max_length=30,default='')
    texto = RichTextField()
    modeloid = models.IntegerField(default=0)
    codigo = models.TextField()

    def __str__(self):
        return str(self.modeloid)    

class DashObjeto(models.Model):
    nombre = models.TextField(max_length=30,default='')
    modeloid = models.IntegerField(default=0)
    codigo = models.TextField()

    def __str__(self):
        return str(self.modeloid)    
