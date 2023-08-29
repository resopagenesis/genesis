from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, FormView
from django.views.generic.list import ListView

from proyectos.models import Proyecto
from aplicaciones.models import Aplicacion
from modelos.models import Modelo, ZonaReporte, ReporteAdHocObjeto
from propiedades.models import Propiedad
from reglas.models import Regla
from personalizacion.models import Personaliza
from principal.models import Seccion,Fila,Columna
from .models import ErroresCreacion
from core.models import Genesis
from registration.views import VerificaVigenciaUsuario
from crear.models import Reporte, ReporteNuevo
from django.urls import reverse_lazy
from .models import ReporteNuevo, TextFiles
from .forms import ReporteForm
import crear.rutinas as rutinas
from .rutinas import CrearArchivoJs, PropiedadesModelo as PropMod, IdentificacionModelo, VistaEditarRaiz
from .rutinas import VistaEditarModeloHijo, VistaCrearModeloHijo, VistaBorrarModeloHijo
from .rutinas import VistaListarRaiz, VistaEditarRaiz, VistaCrearRaiz, VistaBorrarRaiz, VistaModeloSinBase
from .rutinas import VistaReporteEscalonado,VistaReportePlatypus
from proyectos.models import Seccion as SeccionP, Fila as FilaP, Columna as ColumnaP

import os
import errno
import shutil
import string
import json, pickle

class HomeView(TemplateView):
    template_name = "crear/home.html"

    def get_context_data(self,**kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
        gen = Genesis.objects.get(nombre='GENESIS')
        user = self.request.user
        # directorio = '/home/alterego/Documents/proyectos/'
        # directorioArchivosTexto = '/home/alterego/Documents/proyectos/genesisnuevo/core/static/core/textfiles/'
        directorio = gen.directorio
        directoriogenesis = gen.directoriogenesis
        directorioArchivosTexto = gen.directoriotexto
        context['errores'] = False
        estado=int(self.request.GET['estado'])
        if estado == 1: # Se esta creando el proyecto
            CrearProyecto(proyecto,directorio, directorioArchivosTexto,user.username)
            if ErroresCreacion.objects.filter(proyecto=proyecto).count() > 0:
                context['errores'] = True
            else:
                proyecto.estadogeneracion = 1
                proyecto.save()
        if estado == 2: # Se estan creando las aplicaciones
            # CrearProyecto(proyecto,directorio, directorioArchivosTexto,user.username)
            CrearAplicaciones(proyecto,directorio, directorioArchivosTexto,user.username)
            if ErroresCreacion.objects.filter(proyecto=proyecto).count() > 0:
                context['errores'] = True
            else:
                proyecto.estadogeneracion = 2
                proyecto.save()
        if estado == 3: # Se estan creando los modelos
            # CrearProyecto(proyecto,directorio, directorioArchivosTexto,user.username)
            # CrearAplicaciones(proyecto,directorio, directorioArchivosTexto,user.username)
            CrearModelos(proyecto,directorio, directorioArchivosTexto,user.username)
            if ErroresCreacion.objects.filter(proyecto=proyecto).count() > 0:
                context['errores'] = True
            else:
                proyecto.estadogeneracion = 3
                proyecto.save()
        if estado == 4: # Se estan creando las vistas
            CrearVistas(proyecto,directorio, directorioArchivosTexto,user.username)
            if ErroresCreacion.objects.filter(proyecto=proyecto).count() > 0:
                context['errores'] = True
            else:
                proyecto.estadogeneracion = 4
                proyecto.save()
        if estado == 5: # Se estan creando las urls
            CrearUrls(proyecto,directorio, directorioArchivosTexto,user.username)
            if ErroresCreacion.objects.filter(proyecto=proyecto).count() > 0:
                context['errores'] = True
            else:
                proyecto.estadogeneracion = 5
                proyecto.save()
        if estado == 6: # Se estan creando los formularios
            CrearForms(proyecto,directorio, directorioArchivosTexto,user.username)
            if ErroresCreacion.objects.filter(proyecto=proyecto).count() > 0:
                context['errores'] = True
            else:
                proyecto.estadogeneracion = 6
                proyecto.save()
        if estado == 7: # Se estan creando los templates
            # context['avatarwidth'] = proyecto.avatarwidth
            # context['avatarheight'] = proyecto.avatarheight
            
            CrearTemplates(proyecto,directorio, directoriogenesis, directorioArchivosTexto,user.username)
            if ErroresCreacion.objects.filter(proyecto=proyecto).count() > 0:
                context['errores'] = True
            else:
                proyecto.estadogeneracion = 7
                proyecto.save()
        if estado == 8: # Se estan creando la seguridad
            CrearSeguridad(proyecto,directorio, directorioArchivosTexto,user.username)
            if ErroresCreacion.objects.filter(proyecto=proyecto).count() > 0:
                context['errores'] = True
            else:
                proyecto.estadogeneracion = 8
                proyecto.save()
        context['proyecto'] = proyecto
        context['tiene_errores'] = ErroresCreacion.objects.filter(proyecto=proyecto).count() > 0
        return context

class ListaErroresView(ListView):
    model = Proyecto
    template_name = 'crear/lista_errores.html'

    def get_context_data(self, **kwargs):
        context = super(ListaErroresView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            context['proyecto'] = proyecto
            context['lista_errores'] = ErroresCreacion.objects.filter(proyecto = proyecto)
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'        
        return context

class ConfigurarBaseNuevaView(TemplateView):
    template_name = "crear/configuracion_nueva.html"
    # template_name = "crear/panel_ajustable.html"

    def get_context_data(self,**kwargs):
        context = super(ConfigurarBaseNuevaView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)

        # Ver si esta en configuracion
        try:
            context['configuracion'] = self.request.GET['configuracion_proyecto']
        except:
            context['configuracion'] = 'false'

        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            context['anchoencabezadoizquierda'] = proyecto.numerocolumnaenizquierda 
            context['anchologo'] = proyecto.numerocolumnalogo
            context['anchotitulo'] = proyecto.numerocolumnatitulo
            context['anchologin'] = proyecto.numerocolumnalogin
            context['anchoencabezadoderecha'] = proyecto.numerocolumnaenderecha
            context['anchobumeizquierda'] = proyecto.numerocolumnabumeizquierda
            context['anchobusqueda'] = proyecto.numerocolumnabusqueda
            context['anchomenu'] = proyecto.numerocolumnamenu
            context['anchobumederecha'] = proyecto.numerocolumnabumederecha
            context['anchomedioizquierda'] = proyecto.numerocolumnamedioizquierda
            context['anchomediocentro'] = proyecto.numerocolumnamediocentro
            context['anchomedioderecha'] = proyecto.numerocolumnamedioderecha
            context['enfila'] = proyecto.altofilaenizcede
            context['bumefila'] = proyecto.altofilabume
            context['piefila'] = proyecto.altofilapie

            context['separacion'] = proyecto.separacionsecciones
            
            context['proyecto'] = proyecto
            try:
                seccion = self.request.GET['seccion']
                if seccion == 'enfila':
                    proyecto.altofilaenizcede = int(self.request.GET['valor'])
                    context['enfila'] = proyecto.altofilaenizcede
                    proyecto.save()
                if seccion == 'bumefila':
                    proyecto.altofilabume = int(self.request.GET['valor'])
                    context['bumefila'] = proyecto.altofilabume
                    proyecto.save()
                if seccion == 'piefila':
                    proyecto.altofilapie = int(self.request.GET['valor'])
                    context['piefila'] = proyecto.altofilapie
                    proyecto.save()

                if seccion == 'enizquierda':
                    proyecto.numerocolumnaenizquierda = int(self.request.GET['valor'])
                    context['enizquierda'] = proyecto.numerocolumnaenizquierda
                    proyecto.save()
                if seccion == 'enlogo':
                    proyecto.numerocolumnalogo = int(self.request.GET['valor'])
                    context['enlogo'] = proyecto.numerocolumnalogo
                    proyecto.save()
                if seccion == 'entitulo':
                    proyecto.numerocolumnatitulo = int(self.request.GET['valor'])
                    context['entitulo'] = proyecto.numerocolumnatitulo
                    proyecto.save()
                if seccion == 'enlogin':
                    proyecto.numerocolumnalogin = int(self.request.GET['valor'])
                    context['enlogin'] = proyecto.numerocolumnalogin
                    proyecto.save()
                if seccion == 'enderecha':
                    proyecto.numerocolumnaenderecha = int(self.request.GET['valor'])
                    context['enderecha'] = proyecto.numerocolumnaenderecha
                    proyecto.save()

                if seccion == 'bumeizquierda':
                    proyecto.numerocolumnabumeizquierda = int(self.request.GET['valor'])
                    context['anchobumeizquierda'] = proyecto.numerocolumnabumeizquierda
                    proyecto.save()
                if seccion == 'bumebusqueda':
                    proyecto.numerocolumnabusqueda = int(self.request.GET['valor'])
                    context['anchobusqueda'] = proyecto.numerocolumnabusqueda
                    proyecto.save()
                if seccion == 'bumemenu':
                    proyecto.numerocolumnamenu = int(self.request.GET['valor'])
                    context['anchomenu'] = proyecto.numerocolumnamenu
                    proyecto.save()
                if seccion == 'bumederecha':
                    proyecto.numerocolumnabumederecha = int(self.request.GET['valor'])
                    context['anchobumederecha'] = proyecto.numerocolumnabumederecha
                    proyecto.save()

                if seccion == 'cenizquierda':
                    proyecto.numerocolumnamedioizquierda = int(self.request.GET['valor'])
                    context['anchomedioizquierda'] = proyecto.numerocolumnamedioizquierda
                    proyecto.save()
                if seccion == 'cencentro':
                    proyecto.numerocolumnamediocentro = int(self.request.GET['valor'])
                    context['anchomediocentro'] = proyecto.numerocolumnamediocentro
                    proyecto.save()
                if seccion == 'cenderecha':
                    proyecto.numerocolumnamedioderecha = int(self.request.GET['valor'])
                    context['anchomedioderecha'] = proyecto.numerocolumnamedioderecha
                    proyecto.save()
            except:
                pass
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

class PreviewProyectoView(TemplateView):
    template_name = 'crear/preview_proyecto.html'

    def get_context_data(self,**kwargs):
        context = super(PreviewProyectoView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            context['proyecto'] = proyecto
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

class PreviewMainView(TemplateView):
    template_name = 'crear/preview_main.html'

    def get_context_data(self,**kwargs):
        context = super(PreviewMainView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            context['proyecto'] = proyecto
            context['font_size'] = str(proyecto.fonttextomedio).split(',')[1]
            context['font_name'] = str(proyecto.fonttextomedio).split(',')[0]
            context['font_bold'] = str(proyecto.fonttextomedio).split(',')[2]
            context['menu_font_size'] = str(proyecto.fontmenu).split(',')[1]
            context['menu_font_name'] = str(proyecto.fontmenu).split(',')[0]
            context['menu_font_bold'] = str(proyecto.fontmenu).split(',')[2]
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

class PreviewModeloInsertarView(TemplateView):
    template_name = 'crear/preview_modelo_insertar.html'

    def get_context_data(self,**kwargs):
        context = super(PreviewModeloInsertarView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            modelo = Modelo.objects.get(id=self.request.GET['modelo_id'])
            context['proyecto'] = proyecto
            context['modelo'] = modelo
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

class PreviewModeloUpdateView(TemplateView):
    template_name = 'crear/preview_modelo_update.html'

    def get_context_data(self,**kwargs):
        context = super(PreviewModeloUpdateView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            modelo = Modelo.objects.get(id=self.request.GET['modelo_id'])
            context['proyecto'] = proyecto
            context['modelo'] = modelo
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

class PreviewModeloBorrarView(TemplateView):
    template_name = 'crear/preview_modelo_borrar.html'

    def get_context_data(self,**kwargs):
        context = super(PreviewModeloBorrarView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            modelo = Modelo.objects.get(id=self.request.GET['modelo_id'])
            context['proyecto'] = proyecto
            context['modelo'] = modelo
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

class CrearBaseView(TemplateView):
    template_name = "crear/crear_base.html"

    def get_context_data(self,**kwargs):
        context = super(CrearBaseView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)  
        try:
            context['error'] = ''
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context
                        
class ConfigurarBaseView(TemplateView):
    # template_name = "crear/configurar_base.html"
    template_name = "crear/configuracion.html"

    def get_context_data(self,**kwargs):
        context = super(ConfigurarBaseView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)

        # Ver si esta en configuracion
        try:
            context['configuracion'] = self.request.GET['configuracion_proyecto']
        except:
            context['configuracion'] = 'false'

        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            context['altoencabezado'] = str(proyecto.altofilaenizcede) + 'px'
            context['altobume'] = str(proyecto.altofilabume) + 'px'
            context['altomedio'] = str(200) + 'px'
            context['altopie'] = str(proyecto.altofilapie) + 'px'
            context['anchoencabezadoizquierda'] = proyecto.numerocolumnaenizquierda 
            context['anchologo'] = proyecto.numerocolumnalogo
            context['anchotitulo'] = proyecto.numerocolumnatitulo
            context['anchologin'] = proyecto.numerocolumnalogin
            context['anchoencabezadoderecha'] = proyecto.numerocolumnaenderecha
            context['anchobumeizquierda'] = proyecto.numerocolumnabumeizquierda
            context['anchobusqueda'] = proyecto.numerocolumnabusqueda
            context['anchomenu'] = proyecto.numerocolumnamenu
            context['anchobumederecha'] = proyecto.numerocolumnabumederecha
            context['anchomedioizquierda'] = proyecto.numerocolumnamedioizquierda
            context['anchomedicocentro'] = proyecto.numerocolumnamediocentro
            context['anchomedioderecha'] = proyecto.numerocolumnamedioderecha
            context['numerocolumnaenizquierda'] = proyecto.numerocolumnaenizquierda
            context['numerocolumnalogo'] = proyecto.numerocolumnalogo
            context['numerocolumnatitulo'] = proyecto.numerocolumnatitulo
            context['numerocolumnalogin'] = proyecto.numerocolumnalogin
            context['numerocolumnaenderecha'] = proyecto.numerocolumnaenderecha
            context['numerocolumnabumeizquierda'] = proyecto.numerocolumnabumeizquierda
            context['numerocolumnabusqueda'] = proyecto.numerocolumnabusqueda
            context['numerocolumnamenu'] = proyecto.numerocolumnamenu
            context['numerocolumnabumederecha'] = proyecto.numerocolumnabumederecha
            context['numerocolumnamedioizquierda'] = proyecto.numerocolumnamedioizquierda
            context['numerocolumnamediocentro'] = proyecto.numerocolumnamediocentro
            context['numerocolumnamedioderecha'] = proyecto.numerocolumnamedioderecha
            # Alto y ancho de secciones

            try:
                flecha = self.request.GET['flecha']
                if flecha == "faltoencabezado": #alto encabezado
                    elpor = 5
                    if self.request.GET['direccion'] == 'menos':
                        elpor = -5
                    proyecto.altofilaenizcede = proyecto.altofilaenizcede + elpor
                    proyecto.altocolumnaenizquierda = proyecto.altofilaenizcede
                    proyecto.altocolumnalogo = proyecto.altofilaenizcede
                    proyecto.altocolumnatitulo = proyecto.altofilaenizcede
                    proyecto.altocolumnalogin = proyecto.altofilaenizcede
                    proyecto.altocolumnaenderecha = proyecto.altofilaenizcede
                    proyecto.save()
                    context['altoencabezado'] = str(int(self.request.GET['height']) + elpor) + 'px'
                if flecha == "ei": #ancho izquierda encabezado
                    direccion = self.request.GET['direccion']
                    if direccion == 'menos':
                        if proyecto.numerocolumnaenizquierda > 0:
                            context['numerocolumnaenizquierda'] =  proyecto.numerocolumnaenizquierda - 1
                            proyecto.numerocolumnaenizquierda =  proyecto.numerocolumnaenizquierda - 1
                            proyecto.save()
                            # context['numerocolumnalogo'] = proyecto.numerocolumnalogo + 1
                    else:
                        if proyecto.numerocolumnaenizquierda + proyecto.numerocolumnalogo + proyecto.numerocolumnatitulo + proyecto.numerocolumnalogin+ proyecto.numerocolumnaenderecha < 12:
                            context['numerocolumnaenizquierda'] =  proyecto.numerocolumnaenizquierda + 1
                            proyecto.numerocolumnaenizquierda =  proyecto.numerocolumnaenizquierda + 1
                            proyecto.save()
                if flecha == "logo": #ancho logo
                    direccion = self.request.GET['direccion']
                    if direccion == 'menos':
                        if proyecto.numerocolumnalogo > 0:
                            context['numerocolumnalogo'] =  proyecto.numerocolumnalogo - 1
                            proyecto.numerocolumnalogo =  proyecto.numerocolumnalogo - 1
                            proyecto.save()
                            # context['numerocolumnalogo'] = proyecto.numerocolumnalogo + 1
                    else:
                        if proyecto.numerocolumnaenizquierda + proyecto.numerocolumnalogo + proyecto.numerocolumnatitulo + proyecto.numerocolumnalogin+ proyecto.numerocolumnaenderecha < 12:
                            context['numerocolumnalogo'] =  proyecto.numerocolumnalogo + 1
                            proyecto.numerocolumnalogo =  proyecto.numerocolumnalogo + 1
                            proyecto.save()
                if flecha == "titulo": #ancho titulo
                    direccion = self.request.GET['direccion']
                    if direccion == 'menos':
                        if proyecto.numerocolumnatitulo > 0:
                            context['numerocolumnatitulo'] =  proyecto.numerocolumnatitulo - 1
                            proyecto.numerocolumnatitulo =  proyecto.numerocolumnatitulo - 1
                            proyecto.save()
                            # context['numerocolumnalogo'] = proyecto.numerocolumnalogo + 1
                    else:
                        if proyecto.numerocolumnaenizquierda + proyecto.numerocolumnalogo + proyecto.numerocolumnatitulo + proyecto.numerocolumnalogin+ proyecto.numerocolumnaenderecha < 12:
                            context['numerocolumnatitulo'] =  proyecto.numerocolumnatitulo + 1
                            proyecto.numerocolumnatitulo =  proyecto.numerocolumnatitulo + 1
                            proyecto.save()
                if flecha == "login": #ancho login encabezado
                    direccion = self.request.GET['direccion']
                    if direccion == 'menos':
                        if proyecto.numerocolumnalogin > 0:
                            context['numerocolumnalogin'] =  proyecto.numerocolumnalogin - 1
                            proyecto.numerocolumnalogin =  proyecto.numerocolumnalogin - 1
                            proyecto.save()
                            # context['numerocolumnalogo'] = proyecto.numerocolumnalogo + 1
                    else:
                        if proyecto.numerocolumnaenizquierda + proyecto.numerocolumnalogo + proyecto.numerocolumnatitulo + proyecto.numerocolumnalogin+ proyecto.numerocolumnaenderecha < 12:
                            context['numerocolumnalogin'] =  proyecto.numerocolumnalogin + 1
                            proyecto.numerocolumnalogin =  proyecto.numerocolumnalogin + 1
                            proyecto.save()
                if flecha == "ed": #ancho derecha encabezado
                    direccion = self.request.GET['direccion']
                    if direccion == 'menos':
                        if proyecto.numerocolumnaenderecha > 0:
                            context['numerocolumnaenderecha'] =  proyecto.numerocolumnaenderecha - 1
                            proyecto.numerocolumnaenderecha =  proyecto.numerocolumnaenderecha - 1
                            proyecto.save()
                            # context['numerocolumnalogo'] = proyecto.numerocolumnalogo + 1
                    else:
                        if proyecto.numerocolumnaenizquierda + proyecto.numerocolumnalogo + proyecto.numerocolumnatitulo + proyecto.numerocolumnalogin+ proyecto.numerocolumnaenderecha < 12:
                            context['numerocolumnaenderecha'] =  proyecto.numerocolumnaenderecha + 1
                            proyecto.numerocolumnaenderecha =  proyecto.numerocolumnaenderecha + 1
                            proyecto.save()
                if flecha == "faltobume": #alto bume
                    elpor = 5
                    if self.request.GET['direccion'] == 'menos':
                        elpor = -5
                    proyecto.altofilabume = proyecto.altofilabume + elpor
                    proyecto.altocolumnabumeizquierda = proyecto.altofilabume
                    proyecto.altocolumnabumederecha = proyecto.altofilabume
                    proyecto.altocolumnabusqueda = proyecto.altofilabume
                    proyecto.altocolumnamenu = proyecto.altofilabume
                    proyecto.save()
                    context['altobume'] = str(int(self.request.GET['height']) + elpor) + 'px'
                if flecha == "bi": #ancho izquierda busqueda
                    direccion = self.request.GET['direccion']
                    if direccion == 'menos':
                        if proyecto.numerocolumnabumeizquierda > 0:
                            context['numerocolumnabumeizquierda'] =  proyecto.numerocolumnabumeizquierda - 1
                            proyecto.numerocolumnabumeizquierda =  proyecto.numerocolumnabumeizquierda - 1
                            proyecto.save()
                            # context['numerocolumnalogo'] = proyecto.numerocolumnalogo + 1
                    else:
                        if proyecto.numerocolumnabumeizquierda + proyecto.numerocolumnabusqueda + proyecto.numerocolumnamenu + proyecto.numerocolumnabumederecha < 12:
                            context['numerocolumnabumeizquierda'] =  proyecto.numerocolumnabumeizquierda + 1
                            proyecto.numerocolumnabumeizquierda =  proyecto.numerocolumnabumeizquierda + 1
                            proyecto.save()
                if flecha == "busqueda": #ancho busqueda
                    direccion = self.request.GET['direccion']
                    if direccion == 'menos':
                        if proyecto.numerocolumnabusqueda > 0:
                            context['numerocolumnabusqueda'] =  proyecto.numerocolumnabusqueda - 1
                            proyecto.numerocolumnabusqueda =  proyecto.numerocolumnabusqueda - 1
                            proyecto.save()
                            # context['numerocolumnalogo'] = proyecto.numerocolumnalogo + 1
                    else:
                        if proyecto.numerocolumnabumeizquierda + proyecto.numerocolumnabusqueda + proyecto.numerocolumnamenu + proyecto.numerocolumnabumederecha < 12:
                            context['numerocolumnabusqueda'] =  proyecto.numerocolumnabusqueda + 1
                            proyecto.numerocolumnabusqueda =  proyecto.numerocolumnabusqueda + 1
                            proyecto.save()
                if flecha == "menu": #ancho menu
                    direccion = self.request.GET['direccion']
                    if direccion == 'menos':
                        if proyecto.numerocolumnamenu > 0:
                            context['numerocolumnamenu'] =  proyecto.numerocolumnamenu - 1
                            proyecto.numerocolumnamenu =  proyecto.numerocolumnamenu - 1
                            proyecto.save()
                            # context['numerocolumnalogo'] = proyecto.numerocolumnalogo + 1
                    else:
                        if proyecto.numerocolumnabumeizquierda + proyecto.numerocolumnabusqueda + proyecto.numerocolumnamenu + proyecto.numerocolumnabumederecha < 12:
                            context['numerocolumnamenu'] =  proyecto.numerocolumnamenu + 1
                            proyecto.numerocolumnamenu =  proyecto.numerocolumnamenu + 1
                            proyecto.save()
                if flecha == "bd": #ancho bume derecha
                    direccion = self.request.GET['direccion']
                    if direccion == 'menos':
                        if proyecto.numerocolumnabumederecha > 0:
                            context['numerocolumnabumederecha'] =  proyecto.numerocolumnabumederecha - 1
                            proyecto.numerocolumnabumederecha =  proyecto.numerocolumnabumederecha - 1
                            proyecto.save()
                            # context['numerocolumnalogo'] = proyecto.numerocolumnalogo + 1
                    else:
                        if proyecto.numerocolumnabumeizquierda + proyecto.numerocolumnabusqueda + proyecto.numerocolumnamenu + proyecto.numerocolumnabumederecha < 12:
                            context['numerocolumnabumederecha'] =  proyecto.numerocolumnabumederecha + 1
                            proyecto.numerocolumnabumederecha =  proyecto.numerocolumnabumederecha + 1
                            proyecto.save()
                if flecha == "mi": #ancho izquierda medio
                    direccion = self.request.GET['direccion']
                    if direccion == 'menos':
                        if proyecto.numerocolumnamedioizquierda > 0:
                            context['numerocolumnamedioizquierda'] =  proyecto.numerocolumnamedioizquierda - 1
                            proyecto.numerocolumnamedioizquierda =  proyecto.numerocolumnamedioizquierda - 1
                            proyecto.save()
                            # context['numerocolumnalogo'] = proyecto.numerocolumnalogo + 1
                    else:
                        if proyecto.numerocolumnamedioizquierda + proyecto.numerocolumnamediocentro + proyecto.numerocolumnamedioderecha < 12:
                            context['numerocolumnamedioizquierda'] =  proyecto.numerocolumnamedioizquierda + 1
                            proyecto.numerocolumnamedioizquierda =  proyecto.numerocolumnamedioizquierda + 1
                            proyecto.save()
                if flecha == "mc": #ancho medio
                    direccion = self.request.GET['direccion']
                    if direccion == 'menos':
                        if proyecto.numerocolumnamediocentro > 0:
                            context['numerocolumnamediocentro'] =  proyecto.numerocolumnamediocentro - 1
                            proyecto.numerocolumnamediocentro =  proyecto.numerocolumnamediocentro - 1
                            proyecto.save()
                            # context['numerocolumnalogo'] = proyecto.numerocolumnalogo + 1
                    else:
                        if proyecto.numerocolumnamedioizquierda + proyecto.numerocolumnamediocentro + proyecto.numerocolumnamedioderecha < 12:
                            context['numerocolumnamediocentro'] =  proyecto.numerocolumnamediocentro + 1
                            proyecto.numerocolumnamediocentro =  proyecto.numerocolumnamediocentro + 1
                            proyecto.save()
                if flecha == "md": #ancho medio derecha
                    direccion = self.request.GET['direccion']
                    if direccion == 'menos':
                        if proyecto.numerocolumnamedioderecha > 0:
                            context['numerocolumnamedioderecha'] =  proyecto.numerocolumnamedioderecha - 1
                            proyecto.numerocolumnamedioderecha =  proyecto.numerocolumnamedioderecha - 1
                            proyecto.save()
                            # context['numerocolumnalogo'] = proyecto.numerocolumnalogo + 1
                    else:
                        if proyecto.numerocolumnamedioizquierda + proyecto.numerocolumnamediocentro + proyecto.numerocolumnamedioderecha < 12:
                            context['numerocolumnamedioderecha'] =  proyecto.numerocolumnamedioderecha + 1
                            proyecto.numerocolumnamedioderecha =  proyecto.numerocolumnamedioderecha + 1
                            proyecto.save()
                if flecha == "faltopie": #alto pie
                    elpor = 5
                    if self.request.GET['direccion'] == 'menos':
                        elpor = -5
                    proyecto.altofilapie = proyecto.altofilapie + elpor
                    proyecto.save()
                    context['altopie'] = str(int(self.request.GET['height']) + elpor) + 'px'

            except:
                pass

            c1 = '#abadaf'
            c2 = '#bbbdbf'
            c3 = '#cbcdcf'
            c4 = '#dbdddf'
            c5 = '#ebedef'

            context['colorfilaenizcede'] = proyecto.colorfilaenizcede
            context['colorcolumnaenizquierda'] = c1
            context['colorcolumnalogo'] = c2
            context['colorcolumnatitulo'] = c3
            context['colorcolumnalogin'] = c4
            context['colorcolumnaenderecha'] = c5
            context['colorfilabume'] = proyecto.colorfilabume
            context['colorcolumnabumeizquierda'] = c1
            context['colorcolumnabusqueda'] = c2
            context['colorcolumnamenu'] = c3
            context['colorcolumnabumederecha'] = c4
            context['colorfilamedio'] = proyecto.colorfilamedio
            context['colorcolumnamedioizquierda'] = c1
            context['colorcolumnamedioderecha'] = c2
            context['colorcolumnamediocentro'] = c3
            context['colorfilapie'] = proyecto.colorfilapie
            context['colorcolumnapie'] = c1
            
            context['proyecto'] = proyecto
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

class PaletaView(TemplateView):
    # template_name = "crear/configurar_base.html"
    template_name = "crear/paleta.html"

    def get_context_data(self,**kwargs):
        context = super(PaletaView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)

        # Ver si esta en configuracion
        try:
            configuracion = self.request.GET['configuracion_proyecto']
            context['configuracion'] = configuracion
        except:
            context['configuracion'] = 'false'

        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            context['proyecto'] = proyecto
            context['div'] = self.request.GET['div']
            context['red'] = self.request.GET['red']
            context['green'] = self.request.GET['green']
            context['blue'] = self.request.GET['blue']

            listaf1 = []
            listaf2 = []

            # lista.append([te.topico.upper(),te.descripcion,str(te.correlativo) + '.',te.diagrama,'e',te.id])
            listaf1.append(['003366','10','-5'])
            listaf1.append(['336699','12','-5'])
            listaf1.append(['3366cc','14','-5'])
            listaf1.append(['003399','16','-5'])
            listaf1.append(['000099','18','-5'])
            listaf1.append(['0000cc','20','-5'])
            listaf1.append(['000066','22','-5'])

            listaf1.append(['006666','9','-3.3'])
            listaf1.append(['006699','11','-5'])
            listaf1.append(['0099cc','13','-5'])
            listaf1.append(['0066cc','15','-5'])
            listaf1.append(['0033cc','17','-5'])
            listaf1.append(['0000ff','19','-5'])
            listaf1.append(['3333ff','21','-5'])
            listaf1.append(['333399','23','-5'])

            listaf1.append(['669999','8','-3.3'])
            listaf1.append(['009999','10','-5'])
            listaf1.append(['33cccc','12','-5'])
            listaf1.append(['00ccff','14','-5'])
            listaf1.append(['0099ff','16','-5'])
            listaf1.append(['0066ff','18','-5'])
            listaf1.append(['3366ff','20','-5'])
            listaf1.append(['3333cc','22','-5'])
            listaf1.append(['666699','24','-5'])

            listaf1.append(['339966','7','-3.3'])
            listaf1.append(['00cc99','9','-5'])
            listaf1.append(['00ffcc','11','-5'])
            listaf1.append(['00ffff','13','-5'])
            listaf1.append(['33ccff','15','-5'])
            listaf1.append(['3399ff','17','-5'])
            listaf1.append(['6699ff','19','-5'])
            listaf1.append(['6666ff','21','-5'])
            listaf1.append(['6600ff','23','-5'])
            listaf1.append(['6600cc','25','-5'])

            listaf1.append(['339933','6','-3.3'])
            listaf1.append(['00cc66','8','-5'])
            listaf1.append(['00ff99','10','-5'])
            listaf1.append(['66ffcc','12','-5'])
            listaf1.append(['66ffff','14','-5'])
            listaf1.append(['66ccff','16','-5'])
            listaf1.append(['99ccff','18','-5'])
            listaf1.append(['9999ff','20','-5'])
            listaf1.append(['9966ff','22','-5'])
            listaf1.append(['9933ff','24','-5'])
            listaf1.append(['9900ff','26','-5'])

            listaf1.append(['006600','5','-3.3'])
            listaf1.append(['00cc00','7','-5'])
            listaf1.append(['00ff00','9','-5'])
            listaf1.append(['66ff99','11','-5'])
            listaf1.append(['99ffcc','13','-5'])
            listaf1.append(['ccffff','15','-5'])
            listaf1.append(['ccccff','17','-5'])
            listaf1.append(['cc99ff','19','-5'])
            listaf1.append(['cc66ff','21','-5'])
            listaf1.append(['cc33ff','23','-5'])
            listaf1.append(['cc00ff','25','-5'])
            listaf1.append(['9900cc','27','-5'])

            listaf1.append(['003300','4','-3.3'])
            listaf1.append(['009933','6','-5'])
            listaf1.append(['33cc33','8','-5'])
            listaf1.append(['66ff66','10','-5'])
            listaf1.append(['99ff99','12','-5'])
            listaf1.append(['ccffcc','14','-5'])
            listaf1.append(['ffffff','16','-5'])
            listaf1.append(['ffccff','18','-5'])
            listaf1.append(['ff99ff','20','-5'])
            listaf1.append(['ff66ff','22','-5'])
            listaf1.append(['ff00ff','24','-5'])
            listaf1.append(['cc00cc','26','-5'])
            listaf1.append(['660066','28','-5'])

            listaf1.append(['336600','5','-3.3'])
            listaf1.append(['009900','7','-5'])
            listaf1.append(['66ff33','9','-5'])
            listaf1.append(['99ff66','11','-5'])
            listaf1.append(['ccff99','13','-5'])
            listaf1.append(['ffffcc','15','-5'])
            listaf1.append(['ffcccc','17','-5'])
            listaf1.append(['ff99cc','19','-5'])
            listaf1.append(['ff66cc','21','-5'])
            listaf1.append(['ff33cc','23','-5'])
            listaf1.append(['cc0099','25','-5'])
            listaf1.append(['993399','27','-5'])

            listaf1.append(['333300','6','-3.3'])
            listaf1.append(['669900','8','-5'])
            listaf1.append(['99ff33','10','-5'])
            listaf1.append(['ccff66','12','-5'])
            listaf1.append(['ffff99','14','-5'])
            listaf1.append(['ffcc99','16','-5'])
            listaf1.append(['ff9999','18','-5'])
            listaf1.append(['ff6699','20','-5'])
            listaf1.append(['ff3399','22','-5'])
            listaf1.append(['cc3399','24','-5'])
            listaf1.append(['990099','26','-5'])

            listaf1.append(['666633','7','-3.3'])
            listaf1.append(['99cc00','9','-5'])
            listaf1.append(['ccff33','11','-5'])
            listaf1.append(['ffff66','13','-5'])
            listaf1.append(['ffcc66','15','-5'])
            listaf1.append(['ff9966','17','-5'])
            listaf1.append(['ff6666','19','-5'])
            listaf1.append(['ff0066','21','-5'])
            listaf1.append(['cc6699','23','-5'])
            listaf1.append(['993366','25','-5'])

            listaf1.append(['999966','8','-3.3'])
            listaf1.append(['cccc00','10','-5'])
            listaf1.append(['ffff00','12','-5'])
            listaf1.append(['ffcc00','14','-5'])
            listaf1.append(['ff9933','16','-5'])
            listaf1.append(['ff6600','18','-5'])
            listaf1.append(['ff5050','20','-5'])
            listaf1.append(['cc0066','22','-5'])
            listaf1.append(['660033','24','-5'])

            listaf1.append(['996633','9','-3.3'])
            listaf1.append(['cc9900','11','-5'])
            listaf1.append(['ff9900','13','-5'])
            listaf1.append(['cc6600','15','-5'])
            listaf1.append(['ff3300','17','-5'])
            listaf1.append(['ff0000','19','-5'])
            listaf1.append(['cc0000','21','-5'])
            listaf1.append(['990033','23','-5'])

            listaf1.append(['663300','10','-3.3'])
            listaf1.append(['996600','12','-5'])
            listaf1.append(['cc3300','14','-5'])
            listaf1.append(['993300','16','-5'])
            listaf1.append(['990000','18','-5'])
            listaf1.append(['800000','20','-5'])
            listaf1.append(['993333','22','-5'])

            # Nuevo colores

            listaf2.append(['008844','10','-5'])
            listaf2.append(['884422','12','-5'])
            listaf2.append(['8844cc','14','-5'])
            listaf2.append(['008822','16','-5'])
            listaf2.append(['000022','18','-5'])
            listaf2.append(['0000cc','20','-5'])
            listaf2.append(['000044','22','-5'])

            listaf2.append(['004444','9','-3.3'])
            listaf2.append(['004422','11','-5'])
            listaf2.append(['0022cc','13','-5'])
            listaf2.append(['0044cc','15','-5'])
            listaf2.append(['0088cc','17','-5'])
            listaf2.append(['0000ff','19','-5'])
            listaf2.append(['8888ff','21','-5'])
            listaf2.append(['888822','23','-5'])

            listaf2.append(['442222','8','-3.3'])
            listaf2.append(['002222','10','-5'])
            listaf2.append(['88cccc','12','-5'])
            listaf2.append(['00ccff','14','-5'])
            listaf2.append(['0022ff','16','-5'])
            listaf2.append(['0044ff','18','-5'])
            listaf2.append(['8844ff','20','-5'])
            listaf2.append(['8888cc','22','-5'])
            listaf2.append(['444422','24','-5'])

            listaf2.append(['882244','7','-3.3'])
            listaf2.append(['00cc22','9','-5'])
            listaf2.append(['00ffcc','11','-5'])
            listaf2.append(['00ffff','13','-5'])
            listaf2.append(['88ccff','15','-5'])
            listaf2.append(['8822ff','17','-5'])
            listaf2.append(['4422ff','19','-5'])
            listaf2.append(['4444ff','21','-5'])
            listaf2.append(['4400ff','23','-5'])
            listaf2.append(['4400cc','25','-5'])

            listaf2.append(['882288','6','-3.3'])
            listaf2.append(['00cc44','8','-5'])
            listaf2.append(['00ff22','10','-5'])
            listaf2.append(['44ffcc','12','-5'])
            listaf2.append(['44ffff','14','-5'])
            listaf2.append(['44ccff','16','-5'])
            listaf2.append(['22ccff','18','-5'])
            listaf2.append(['2222ff','20','-5'])
            listaf2.append(['2244ff','22','-5'])
            listaf2.append(['2288ff','24','-5'])
            listaf2.append(['2200ff','26','-5'])

            listaf2.append(['004400','5','-3.3'])
            listaf2.append(['00cc00','7','-5'])
            listaf2.append(['00ff00','9','-5'])
            listaf2.append(['44ff22','11','-5'])
            listaf2.append(['22ffcc','13','-5'])
            listaf2.append(['ccffff','15','-5'])
            listaf2.append(['ccccff','17','-5'])
            listaf2.append(['cc22ff','19','-5'])
            listaf2.append(['cc44ff','21','-5'])
            listaf2.append(['cc88ff','23','-5'])
            listaf2.append(['cc00ff','25','-5'])
            listaf2.append(['2200cc','27','-5'])

            listaf2.append(['008800','4','-3.3'])
            listaf2.append(['002288','6','-5'])
            listaf2.append(['88cc88','8','-5'])
            listaf2.append(['44ff44','10','-5'])
            listaf2.append(['22ff22','12','-5'])
            listaf2.append(['ccffcc','14','-5'])
            listaf2.append(['ffffff','16','-5'])
            listaf2.append(['ffccff','18','-5'])
            listaf2.append(['ff22ff','20','-5'])
            listaf2.append(['ff44ff','22','-5'])
            listaf2.append(['ff00ff','24','-5'])
            listaf2.append(['cc00cc','26','-5'])
            listaf2.append(['440044','28','-5'])

            listaf2.append(['884400','5','-3.3'])
            listaf2.append(['002200','7','-5'])
            listaf2.append(['44ff88','9','-5'])
            listaf2.append(['22ff44','11','-5'])
            listaf2.append(['ccff22','13','-5'])
            listaf2.append(['ffffcc','15','-5'])
            listaf2.append(['ffcccc','17','-5'])
            listaf2.append(['ff22cc','19','-5'])
            listaf2.append(['ff44cc','21','-5'])
            listaf2.append(['ff88cc','23','-5'])
            listaf2.append(['cc0022','25','-5'])
            listaf2.append(['228822','27','-5'])

            listaf2.append(['888800','6','-3.3'])
            listaf2.append(['442200','8','-5'])
            listaf2.append(['22ff88','10','-5'])
            listaf2.append(['ccff44','12','-5'])
            listaf2.append(['ffff22','14','-5'])
            listaf2.append(['ffcc22','16','-5'])
            listaf2.append(['ff2222','18','-5'])
            listaf2.append(['ff4422','20','-5'])
            listaf2.append(['ff8822','22','-5'])
            listaf2.append(['cc8822','24','-5'])
            listaf2.append(['220022','26','-5'])

            listaf2.append(['444488','7','-3.3'])
            listaf2.append(['22cc00','9','-5'])
            listaf2.append(['ccff88','11','-5'])
            listaf2.append(['ffff44','13','-5'])
            listaf2.append(['ffcc44','15','-5'])
            listaf2.append(['ff2244','17','-5'])
            listaf2.append(['ff4444','19','-5'])
            listaf2.append(['ff0044','21','-5'])
            listaf2.append(['cc4422','23','-5'])
            listaf2.append(['228844','25','-5'])

            listaf2.append(['222244','8','-3.3'])
            listaf2.append(['cccc00','10','-5'])
            listaf2.append(['ffff00','12','-5'])
            listaf2.append(['ffcc00','14','-5'])
            listaf2.append(['ff2288','16','-5'])
            listaf2.append(['ff4400','18','-5'])
            listaf2.append(['ff5050','20','-5'])
            listaf2.append(['cc0044','22','-5'])
            listaf2.append(['440088','24','-5'])

            listaf2.append(['224488','9','-3.3'])
            listaf2.append(['cc2200','11','-5'])
            listaf2.append(['ff2200','13','-5'])
            listaf2.append(['cc4400','15','-5'])
            listaf2.append(['ff8800','17','-5'])
            listaf2.append(['ff0000','19','-5'])
            listaf2.append(['cc0000','21','-5'])
            listaf2.append(['220088','23','-5'])

            listaf2.append(['448800','10','-3.3'])
            listaf2.append(['224400','12','-5'])
            listaf2.append(['cc8800','14','-5'])
            listaf2.append(['228800','16','-5'])
            listaf2.append(['220000','18','-5'])
            listaf2.append(['800000','20','-5'])
            listaf2.append(['228888','22','-5'])



            context['l1'] = listaf1
            context['l2'] = listaf2

            # lista=list(range(0,255,10))
            listar=list(range(0,255))
            listag=list(range(0,255))
            listab=list(range(0,255))
            context['listar'] = listar
            context['listag'] = listag
            context['listab'] = listab
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

class ColoresView(TemplateView):
    template_name = "crear/panel_ajustable.html"
    # template_name = "crear/configuracion_color.html"

    def get_context_data(self,**kwargs):
        context = super(ColoresView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)

        # Ver si esta en configuracion
        try:
            configuracion = self.request.GET['configuracion_proyecto']
            context['configuracion'] = configuracion
        except:
            context['configuracion'] = 'false'

        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            context['altoencabezado'] = str(proyecto.altofilaenizcede) + 'px'
            context['altobume'] = str(proyecto.altofilabume) + 'px'
            context['altomedio'] = str(200) + 'px'
            context['altopie'] = str(proyecto.altofilapie) + 'px'
            context['anchoencabezadoizquierda'] = proyecto.numerocolumnaenizquierda 
            context['anchologo'] = proyecto.numerocolumnalogo
            context['anchotitulo'] = proyecto.numerocolumnatitulo
            context['anchologin'] = proyecto.numerocolumnalogin
            context['anchoencabezadoderecha'] = proyecto.numerocolumnaenderecha
            context['anchobumeizquierda'] = proyecto.numerocolumnabumeizquierda
            context['anchobusqueda'] = proyecto.numerocolumnabusqueda
            context['anchomenu'] = proyecto.numerocolumnamenu
            context['anchobumederecha'] = proyecto.numerocolumnabumederecha
            context['anchomedioizquierda'] = proyecto.numerocolumnamedioizquierda
            context['anchomedicocentro'] = proyecto.numerocolumnamediocentro
            context['anchomedioderecha'] = proyecto.numerocolumnamedioderecha
            context['numerocolumnaenizquierda'] = proyecto.numerocolumnaenizquierda
            context['numerocolumnalogo'] = proyecto.numerocolumnalogo
            context['numerocolumnatitulo'] = proyecto.numerocolumnatitulo
            context['numerocolumnalogin'] = proyecto.numerocolumnalogin
            context['numerocolumnaenderecha'] = proyecto.numerocolumnaenderecha
            context['numerocolumnabumeizquierda'] = proyecto.numerocolumnabumeizquierda
            context['numerocolumnabusqueda'] = proyecto.numerocolumnabusqueda
            context['numerocolumnamenu'] = proyecto.numerocolumnamenu
            context['numerocolumnabumederecha'] = proyecto.numerocolumnabumederecha
            context['numerocolumnamedioizquierda'] = proyecto.numerocolumnamedioizquierda
            context['numerocolumnamediocentro'] = proyecto.numerocolumnamediocentro
            context['numerocolumnamedioderecha'] = proyecto.numerocolumnamedioderecha

            # colores de secciones

            try:
                # color = 'rgba(' + self.request.GET['color'] + ')'
                color = '#' + self.request.GET['color']
                div = self.request.GET['div']
                context[div] = div
                if div == 'colorfilaenizcede':
                    proyecto.colorfilaenizcede = color
                if div == 'colorcolumnaenizquierda':
                    proyecto.colorcolumnaenizquierda = color
                if div == 'colorcolumnalogo':
                    proyecto.colorcolumnalogo = color
                if div == 'colorcolumnatitulo':
                    proyecto.colorcolumnatitulo = color
                if div == 'colorcolumnalogin':
                    proyecto.colorcolumnalogin = color
                if div == 'colorcolumnaenderecha':
                    proyecto.colorcolumnaenderecha = color
                if div == 'colorfilabume':
                    proyecto.colorfilabume = color
                if div == 'colorcolumnabumeizquierda':
                    proyecto.colorcolumnabumeizquierda = color
                if div == 'colorcolumnabusqueda':
                    proyecto.colorcolumnabusqueda = color
                if div == 'colorcolumnamenu':
                    proyecto.colorcolumnamenu = color
                if div == 'colorcolumnabumederecha':
                    proyecto.colorcolumnabumederecha = color
                if div == 'colorfilamedio':
                    proyecto.colorfilamedio = color
                if div == 'colorcolumnamedioizquierda':
                    proyecto.colorcolumnamedioizquierda = color
                if div == 'colorcolumnamedioderecha':
                    proyecto.colorcolumnamedioderecha = color
                if div == 'colorcolumnamediocentro':
                    proyecto.colorcolumnamediocentro = color
                if div == 'colorfilapie':
                    proyecto.colorfilapie = color
                if div == 'colorcolumnapie':
                    proyecto.colorcolumnapie = color
                proyecto.save()
            except:
                pass        
            # Colores
            context['colorfilaenizcede'] = proyecto.colorfilaenizcede
            context['colorcolumnaenizquierda'] = proyecto.colorcolumnaenizquierda
            context['colorcolumnalogo'] = proyecto.colorcolumnalogo
            context['colorcolumnatitulo'] = proyecto.colorcolumnatitulo
            context['colorcolumnalogin'] = proyecto.colorcolumnalogin
            context['colorcolumnaenderecha'] = proyecto.colorcolumnaenderecha
            context['colorfilabume'] = proyecto.colorfilabume
            context['colorcolumnabumeizquierda'] = proyecto.colorcolumnabumeizquierda
            context['colorcolumnabusqueda'] = proyecto.colorcolumnabusqueda
            context['colorcolumnamenu'] = proyecto.colorcolumnamenu
            context['colorcolumnabumederecha'] = proyecto.colorcolumnabumederecha
            context['colorfilamedio'] = proyecto.colorfilamedio
            context['colorcolumnamedioizquierda'] = proyecto.colorcolumnamedioizquierda
            context['colorcolumnamedioderecha'] = proyecto.colorcolumnamedioderecha
            context['colorcolumnamediocentro'] = proyecto.colorcolumnamediocentro
            context['colorfilapie'] = proyecto.colorfilapie
            context['colorcolumnapie'] = proyecto.colorcolumnapie
            context['proyecto'] = proyecto
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

class OtrosView(TemplateView):
    # template_name = "crear/configurar_base.html"
    template_name = "crear/configuracion_otros.html"

    def get_context_data(self,**kwargs):
        context = super(OtrosView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)

        # Ver si esta en configuracion
        try:
            context['configuracion'] = self.request.GET['configuracion_proyecto']
        except:
            context['configuracion'] = 'false'

        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            context['altoencabezado'] = str(proyecto.altofilaenizcede) + 'px'
            context['altobume'] = str(proyecto.altofilabume) + 'px'
            context['altomedio'] = str(200) + 'px'
            context['altopie'] = str(proyecto.altofilapie) + 'px'
            context['anchoencabezadoizquierda'] = proyecto.numerocolumnaenizquierda 
            context['anchologo'] = proyecto.numerocolumnalogo
            context['anchotitulo'] = proyecto.numerocolumnatitulo
            context['anchologin'] = proyecto.numerocolumnalogin
            context['anchoencabezadoderecha'] = proyecto.numerocolumnaenderecha
            context['anchobumeizquierda'] = proyecto.numerocolumnabumeizquierda
            context['anchobusqueda'] = proyecto.numerocolumnabusqueda
            context['anchomenu'] = proyecto.numerocolumnamenu
            context['anchobumederecha'] = proyecto.numerocolumnabumederecha
            context['anchomedioizquierda'] = proyecto.numerocolumnamedioizquierda
            context['anchomedicocentro'] = proyecto.numerocolumnamediocentro
            context['anchomedioderecha'] = proyecto.numerocolumnamedioderecha
            context['numerocolumnaenizquierda'] = proyecto.numerocolumnaenizquierda
            context['numerocolumnalogo'] = proyecto.numerocolumnalogo
            context['numerocolumnatitulo'] = proyecto.numerocolumnatitulo
            context['numerocolumnalogin'] = proyecto.numerocolumnalogin
            context['numerocolumnaenderecha'] = proyecto.numerocolumnaenderecha
            context['numerocolumnabumeizquierda'] = proyecto.numerocolumnabumeizquierda
            context['numerocolumnabusqueda'] = proyecto.numerocolumnabusqueda
            context['numerocolumnamenu'] = proyecto.numerocolumnamenu
            context['numerocolumnabumederecha'] = proyecto.numerocolumnabumederecha
            context['numerocolumnamedioizquierda'] = proyecto.numerocolumnamedioizquierda
            context['numerocolumnamediocentro'] = proyecto.numerocolumnamediocentro
            context['numerocolumnamedioderecha'] = proyecto.numerocolumnamedioderecha
        
            salto = 10
            saltoy = 5
            incremento = 5

            try:
                direccion = self.request.GET['direccion']
                if direccion == 'logocentro':
                    proyecto.justificacionverticallogo = 'c'
                    proyecto.justificacionhorizontallogo = 'c'
                if direccion == 'logoabajo':
                    proyecto.justificacionverticallogo = 'i'
                if direccion == 'logoarriba':
                    proyecto.justificacionverticallogo = 's'
                if direccion == 'logoderecha':
                    proyecto.justificacionhorizontallogo = 'd'
                if direccion == 'logoizquierda':
                    proyecto.justificacionhorizontallogo = 'i'
                if direccion == 'titulocentro':
                    proyecto.justificacionverticaltitulo = 'c'
                    proyecto.justificacionhorizontaltitulo = 'c'
                if direccion == 'tituloabajo':
                    proyecto.justificacionverticaltitulo = 'i'
                if direccion == 'tituloarriba':
                    proyecto.justificacionverticaltitulo = 's'
                if direccion == 'tituloderecha':
                    proyecto.justificacionhorizontaltitulo = 'd'
                if direccion == 'tituloizquierda':
                    proyecto.justificacionhorizontaltitulo = 'i'
                # if direccion == 'logocentro':
                #     proyecto.justificacionhorizontallogo = 'c'
                #     proyecto.justificacionverticallogo = 'c'
                # if direccion == 'titulocentro':
                #     proyecto.justificacionhorizontaltitulo = 'c'
                #     proyecto.justificacionverticaltitulo = 'c'

                proyecto.save()
            except:
                pass

            try:
                direccion = self.request.GET['dimension']
                if direccion == 'logomasabajo':
                    proyecto.avatarheight = proyecto.avatarheight + incremento
                if direccion == 'logomenosarriba':
                    proyecto.avatarheight = proyecto.avatarheight - incremento
                if direccion == 'logomasderecha':
                    proyecto.avatarwidth = proyecto.avatarwidth + incremento
                if direccion == 'logomenosizquierda':
                    proyecto.avatarwidth = proyecto.avatarwidth - incremento
                if direccion == 'titulomasabajo':
                    proyecto.imagentituloheight = proyecto.imagentituloheight + incremento
                if direccion == 'titulomenosarriba':
                    proyecto.imagentituloheight = proyecto.imagentituloheight - incremento
                if direccion == 'titulomasderecha':
                    proyecto.imagentitulowidth = proyecto.imagentitulowidth + incremento
                if direccion == 'titulomenosizquierda':
                    proyecto.imagentitulowidth = proyecto.imagentitulowidth - incremento
                # if direccion == 'logocentro':
                #     proyecto.justificacionhorizontallogo = 'c'
                #     proyecto.justificacionverticallogo = 'c'
                # if direccion == 'titulocentro':
                #     proyecto.justificacionhorizontaltitulo = 'c'
                #     proyecto.justificacionverticaltitulo = 'c'

                proyecto.save()
            except  Exception as e:
                print(e)

            if proyecto.justificacionhorizontallogo == 'i':
                context['horizontallogo'] = 'justify-content-start'    
            if proyecto.justificacionhorizontallogo == 'c':
                context['horizontallogo'] = 'justify-content-center'    
            if proyecto.justificacionhorizontallogo == 'd':
                context['horizontallogo'] = 'justify-content-end'    
            if proyecto.justificacionverticallogo == 'i':
                context['verticallogo'] = 'align-items-end'    
            if proyecto.justificacionverticallogo == 'c':
                context['verticallogo'] = 'align-items-center'    
            if proyecto.justificacionverticallogo == 's':
                context['verticallogo'] = 'align-items-start'    
            if proyecto.justificacionhorizontaltitulo == 'i':
                context['horizontaltitulo'] = 'justify-content-start'    
            if proyecto.justificacionhorizontaltitulo == 'c':
                context['horizontaltitulo'] = 'justify-content-center'    
            if proyecto.justificacionhorizontaltitulo == 'd':
                context['horizontaltitulo'] = 'justify-content-end'    
            if proyecto.justificacionverticaltitulo == 'i':
                context['verticaltitulo'] = 'align-items-end'    
            if proyecto.justificacionverticaltitulo == 'c':
                context['verticaltitulo'] = 'align-items-center'    
            if proyecto.justificacionverticaltitulo == 's':
                context['verticaltitulo'] = 'align-items-start'    

            # # Alto y ancho de secciones
            # if proyecto.justificacionhorizontallogo == 'c':
            #     context['horizontallogo'] = 'justify-content-center'
            # if proyecto.justificacionhorizontallogo == 'i':
            #     context['horizontallogo'] = 'justify-content-start'
            # if proyecto.justificacionhorizontallogo == 'd':
            #     context['horizontallogo'] = 'justify-content-end'
            # if proyecto.justificacionverticallogo == 's':
            #     context['verticallogo'] = 'align-items-start'
            # if proyecto.justificacionverticallogo == 'c':
            #     context['verticallogo'] = 'align-items-center'
            # if proyecto.justificacionverticallogo == 'i':
            #     context['verticallogo'] = 'align-items-end'
            # if proyecto.justificacionhorizontaltitulo == 'c':
            #     context['horizontaltitulo'] = 'justify-content-center'
            # if proyecto.justificacionhorizontaltitulo == 'i':
            #     context['horizontaltitulo'] = 'justify-content-start'
            # if proyecto.justificacionhorizontaltitulo == 'd':
            #     context['horizontaltitulo'] = 'justify-content-end'
            # if proyecto.justificacionverticaltitulo == 's':
            #     context['verticaltitulo'] = 'align-items-start'
            # if proyecto.justificacionverticaltitulo == 'c':
            #     context['verticaltitulo'] = 'align-items-center'
            # if proyecto.justificacionverticaltitulo == 'i':
            #     context['verticaltitulo'] = 'align-items-end'
        
            # Colores

            context['altologo'] = str(proyecto.avatarheight) + 'px'
            context['anchologo'] = str(proyecto.avatarwidth) + 'px'
            context['altotitulo'] = str(proyecto.imagentituloheight) + 'px'
            context['anchotitulo'] = str(proyecto.imagentitulowidth) + 'px'

            context['proyecto'] = proyecto
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'        
        return context

def AltoNegativo(alto):
    return str(alto) + 'px' if alto >0 else str(alto*-1) + "%"

def ManejoArchivos(proyecto,directorio):

    # Crear directorios
    try:
        os.mkdir(directorio + proyecto.nombre)
    except:
        print('existe')

    # Leer archivos en bloque
    filename = '/home/alterego/Downloads/cambiotecladoubuntu'
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except:
        print('no hay archivo')

    # Leer archivos linea a linea
    filename = '/home/alterego/Downloads/cambiotecladoubuntu'
    try:
        with open(filename) as file_object:
            for line in file_object:
                pass
    except:
        print('No existe el archivo')

    # Escribir archivos
    try:
        filename = '/home/alterego/Downloads/pruebanuevo.txt'
        with open(filename, 'w') as file_object:
            file_object.write("Python, el lenguaje del futuro")
    except:
        print('No se escribe el archivo')

    # Copiar archivos
    origen = '/home/alterego/Downloads/cambiotecladoubuntu'
    destino = '/home/alterego/Downloads/nuevocambiotecladoubuntu'
    try:
        shutil.copy(origen, destino)
    except:
        print('No se copio el archivo')

    # # Mover archivos
    origen = '/home/alterego/Downloads/nuevocambiotecladoubuntu'
    destino = '/home/alterego/Documents/proyectos/Tercer proyecto/nuevocambiotecladoubuntu'
    shutil.move(origen, destino)

    # Copiar directorios
    origen = '/home/alterego/Documents/proyectos/Tercer proyecto'
    destino = '/home/alterego/Documents/proyectos/Tercer proyecto nuevo'
    try:
        shutil.copytree(origen, destino)
    except:
        print('No se movio el directorio')

    # Mover directorios
    origen = '/home/alterego/Documents/proyectos/Tercer proyecto nuevo'
    destino = '/home/alterego/Downloads/Tercer proyecto nuevo'
    try:
        shutil.move(origen, destino)
    except:
        print('No se movio el directorio')

    # Eliminar archivos
    filename = '/home/alterego/Downloads/Tercer proyecto nuevo/nuevocambiotecladoubuntu'
    try:
        os.remove(filename)
    except:
        print('No se borro')

    # Eliminar directorios
    directorio = '/home/alterego/Documents/proyectos/Tercer proyecto'
    try:
        shutil.rmtree(directorio)
    except:
        print('No se borro')

def CrearProyecto(proyecto,directorio,dt,usuario):

    etapa = "CrearProyecto"

    # Borrar los errores de generacion
    ErroresCreacion.objects.filter(proyecto=proyecto.nombre).delete()
    nombre = proyecto.nombre
    try:
        # Directorio del proyecto
        rutinas.CrearDirectorio(directorio + nombre,etapa,nombre,usuario,True)
        # Directorio media
        rutinas.CrearDirectorio(directorio + nombre + "/media",etapa,nombre,usuario,True)
        # # Directorio media por aplicacion
        # Directorio del directorio del directorio del proyecto
        rutinas.CrearDirectorio(directorio + nombre + "/" + nombre,etapa,nombre,usuario,True)
        # Archivo __init__.py debajo del directorio del directorio del proyecto
        rutinas.CopiarArchivos(dt + "__init__.py", directorio + nombre + "/" + nombre + "/__init__.py",etapa,nombre, usuario,True)
        
        # Archivo settings.py debajo del directorio del directorio del proyecto
        # stri = TextFiles.objects.get(file = "settings.py").texto
        stri = rutinas.LeerArchivo(dt + "settings.py",etapa,nombre,usuario)
        stri = stri.replace('@proyecto',nombre)

        rutinas.ProcesoPersonalizacion(proyecto,nombre,'settings.py',directorio + nombre + "/" + nombre + "/",stri,nombre,etapa,usuario)

        # Archivo urls.py debajo del directorio del directorio del proyecto
        # stri = TextFiles.objects.get(file = "core_urls.py").texto

        rutinas.CopiarArchivos(dt + "urls.py", directorio + nombre + "/" + nombre + "/urls.py",etapa,nombre, usuario,True)
        # Archivo wsgi.py debajo del directorio del directorio del proyecto
        # stri = TextFiles.objects.get(file = "wsgi.py").texto
        stri = rutinas.LeerArchivo(dt + "wsgi.py",etapa,nombre,usuario)
        stri = stri.replace('@proyecto',nombre)
        rutinas.EscribirArchivo(directorio + nombre + "/" + nombre + "/wsgi.py",etapa,nombre,stri,usuario,True)
        # Archivo manage.py debajo del directorio del proyecto
        # stri = TextFiles.objects.get(file = "manage.py").texto
        stri = rutinas.LeerArchivo(dt + "manage.py",etapa,nombre,usuario)
        stri = stri.replace('@proyecto',nombre)
        rutinas.EscribirArchivo(directorio + nombre + "/manage.py",etapa,nombre,stri,usuario,True)
    except Exception as e:
        errores = ErroresCreacion()
        errores.etapa = etapa
        errores.paso = "Crear los proyectos: "
        errores.proyecto = nombre
        errores.usuario = usuario
        errores.descripcion = e
        errores.save()    
             
def CrearAplicaciones(proyecto,directorio,dt,usuario):

    # Borrar los errores de generacion
    ErroresCreacion.objects.filter(proyecto=proyecto.nombre).delete()

    etapa = "CrearAplicaciones"
    nombre = proyecto.nombre
    
    # Crear en la base de datos la aplicacion core
    try:
        Aplicacion.objects.get(nombre='core', proyecto=proyecto)
    except:
        aplicacion = Aplicacion()
        aplicacion.proyecto = proyecto
        aplicacion.nombre = 'core'
        aplicacion.descripcion = 'Aplicacion de soporte'
        aplicacion.save()
        
    # Crear en la base de datos la aplicacion registration
    try:
        Aplicacion.objects.get(nombre='registration', proyecto=proyecto)
    except:
        aplicacion = Aplicacion()
        aplicacion.proyecto = proyecto
        aplicacion.nombre = 'registration'
        aplicacion.descripcion = 'Aplicacion de seguridad'
        aplicacion.save()

    try:
        aplicacion = Aplicacion.objects.get(nombre='seguridad', proyecto=proyecto)
    except:
        aplicacion = Aplicacion()
        aplicacion.proyecto = proyecto
        aplicacion.nombre = 'seguridad'
        aplicacion.descripcion = 'Aplicacion de seguridad con roles'
        aplicacion.textoenmenu = 'Roles'
        aplicacion.save()

    # Crear en la base de datos la aplicacion seguridad
    # rutinas.CrearEsquemaSeguridad(proyecto, aplicacion)
    
    # Variable para la lista de aplicaciones para settings.py
    strLa = ''
    strCss = ''

    for aplicacion in Aplicacion.objects.filter(proyecto=proyecto):

        try:

            # verificar si la aplicacion tiene modelos y estos tienen propiedades
            flgCrear = rutinas.AplicacionTienePropiedades(aplicacion)
            flgCrear = True
            if flgCrear or aplicacion.nombre == 'core' or aplicacion.nombre == 'registration':

                # No se incluye la aplicacion registration pues esa va primero
                if aplicacion.nombre != 'registration':
                    strLa += "\t'" + aplicacion.nombre + "'," + '\n'

                # Crear el directorio de la aplicacion
                rutinas.CrearDirectorio(directorio + nombre + "/" + aplicacion.nombre,etapa,nombre,usuario,True)
                # Crear el directorio migrations debajo del directorio de la aplicacion
                rutinas.CrearDirectorio(directorio + nombre + "/" + aplicacion.nombre + "/migrations",etapa,nombre,usuario,True)
                # Crear directorio  __pycache debajo de migrations para cada aplicacion
                rutinas.CrearDirectorio(directorio + nombre + "/" + aplicacion.nombre + "/migrations/__pycache__",etapa,nombre,usuario,True)
                # Crear el archivo __init__.py debajo de migrations
                rutinas.CopiarArchivos(dt + "__init__.py", directorio + nombre + "/" + aplicacion.nombre + "/migrations/__init__.py",etapa,nombre, usuario,True)
                # Crear directorio  templates debajo de cada aplicacion
                rutinas.CrearDirectorio(directorio + nombre + "/" + aplicacion.nombre + "/templates",etapa,nombre,usuario,True)
                # Crear directorio  con el nombre de la aplicacion debajo de templates
                rutinas.CrearDirectorio(directorio + nombre + "/" + aplicacion.nombre + "/templates/" + aplicacion.nombre,etapa,nombre,usuario,True)
                if aplicacion.nombre == 'core':
                    # Crear directorio includes debajo de la aplicacion core
                    rutinas.CrearDirectorio(directorio + nombre + "/core/templates/core/includes",etapa,nombre,usuario,True)
                    # Copiar en core/includes los dos archivos html para importar los css y js de bootstarp
                    # stri = TextFiles.objects.get(file = "css_general.html").texto
                    stri = rutinas.LeerArchivo(dt + "css_general.html",etapa,nombre,usuario)

                    rutinas.ProcesoPersonalizacion(proyecto,aplicacion.nombre,'css_general.html',directorio + nombre + "/core/templates/core/includes/",stri,nombre,etapa,usuario)

                    # stri = TextFiles.objects.get(file = "js_general.html").texto
                    stri = rutinas.LeerArchivo(dt + "js_general.html",etapa,nombre,usuario)

                    rutinas.ProcesoPersonalizacion(proyecto,aplicacion.nombre,'js_general.html',directorio + nombre + "/core/templates/core/includes/",stri,nombre,etapa,usuario)

                    # Crear directorio static debajo de la aplicacion core
                    rutinas.CrearDirectorio(directorio + nombre + "/core/static",etapa,nombre,usuario,True)
                    # Crear directorio core debajo de la static en core
                    rutinas.CrearDirectorio(directorio + nombre + "/core/static/core",etapa,nombre,usuario,True)
                    # Crear directorio css debajo de la static/core en core
                    rutinas.CrearDirectorio(directorio + nombre + "/core/static/core/css",etapa,nombre,usuario,True)
                    # Crear directorio img debajo de la static/core en core
                    rutinas.CrearDirectorio(directorio + nombre + "/core/static/core/img",etapa,nombre,usuario,True)
                    # Crear directorio js debajo de la static/core en core
                    rutinas.CrearDirectorio(directorio + nombre + "/core/static/core/js",etapa,nombre,usuario,True)
                    # Copiar los archivos css de bootstrap y animations en css de core/static/css
                    rutinas.CopiarArchivos(dt + "animation.css", directorio + nombre + "/core/static/core/css/animation.css",etapa,nombre, usuario,True)
                    rutinas.CopiarArchivos(dt + "bootstrap.css", directorio + nombre + "/core/static/core/css/bootstrap.css",etapa,nombre, usuario,True)
                    rutinas.CopiarArchivos(dt + "bootstrap.min.css", directorio + nombre + "/core/static/core/css/bootstrap.min.css",etapa,nombre, usuario,True)
                    # Copiar los archivos js de bootstrap, jquery y popper core/static/js
                    rutinas.CopiarArchivos(dt + "bootstrap.min.js", directorio + nombre + "/core/static/core/js/Bootstrap.min.js",etapa,nombre, usuario,True)
                    rutinas.CopiarArchivos(dt + "jquery-3.4.1.min.js", directorio + nombre + "/core/static/core/js/jquery-3.4.1.min.js",etapa,nombre, usuario,True)
                    rutinas.CopiarArchivos(dt + "popper.min.js", directorio + nombre + "/core/static/core/js/popper.min.js",etapa,nombre, usuario,True)
                    rutinas.CopiarArchivos(dt + "js_propios.js", directorio + nombre + "/core/static/core/js/js_propios.js",etapa,nombre, usuario,True)

            # Estilos de aplicaciones
            # Leer el archivo estilos.css
            # stri = TextFiles.objects.get(file = "estilos.css").texto
            stri = rutinas.LeerArchivoEnTexto(dt + "aplicaciones.css",etapa,nombre,usuario)
            stri = stri.replace('@aplicacion',aplicacion.nombre)
            stri = rutinas.AsignaFonts(aplicacion.fontmenu,'menu',stri)
            strCss += stri
            stri = ''


        except Exception as e:
            errores = ErroresCreacion()
            errores.etapa = etapa
            errores.paso = "Crear las aplicaciones: "
            errores.proyecto = nombre
            errores.usuario = usuario
            errores.descripcion = e
            errores.save()            

    # Graba el css de las aplicaciones
    rutinas.ProcesoPersonalizacion(proyecto,aplicacion.nombre,'aplicaciones.css',directorio + nombre + "/core/static/core/css/",strCss,nombre,etapa,usuario)

    # Leer el archivo settings.py
    # stri = TextFiles.objects.get(file = "settings.py").texto
    stri = rutinas.LeerArchivo(dt + "settings.py",etapa,nombre,usuario)
    # modificar archivo settings.py  del proyecto con la lista de los nombres de las aplicaciones
    stri = stri.replace('#@registration', "'" + 'registration' + "',")
    stri = stri.replace('#@aplicaciones', strLa)
    stri = stri.replace('@proyecto', proyecto.nombre)
    # Borrar el archivo settings del directorio proyecto del proyecto
    # Grabar el nuevo archivo settings
    rutinas.ProcesoPersonalizacion(proyecto,aplicacion.nombre,'settings.py',directorio + nombre + "/" + nombre + "/",stri,nombre,etapa,usuario)
    # rutinas.EscribirArchivo(directorio +"/" + nombre + "/" + nombre + "/settings.py",etapa,nombre,stri,usuario,True)

    # Crear archivos de aplicaciones
    for aplicacion in Aplicacion.objects.filter(proyecto=proyecto):
        # verificar si la aplicacion tiene modelos y estos tienen propiedades
        flgCrear = rutinas.AplicacionTienePropiedades(aplicacion)
        flgCrear = True
        if flgCrear or aplicacion.nombre == 'core' or aplicacion.nombre == 'registration':
            # Copiar el archivo __init__.py de text files en el directorio de la aplicacion
            rutinas.CopiarArchivos(dt + "__init__.py",directorio + nombre + "/" + aplicacion.nombre + "/__init__.py",etapa,nombre,usuario,True)

            # Copiar el archivo admin.py de text files en el directorio de la aplicacion
            # stri = TextFiles.objects.get(file = "admin.py").texto
            stri = rutinas.LeerArchivo(dt + "admin.py",etapa,nombre,usuario)

            rutinas.ProcesoPersonalizacion(proyecto,aplicacion.nombre,'admin.py',directorio + nombre + "/" + aplicacion.nombre + "/",stri,nombre,etapa,usuario)

            # Procesar apps.py
            stri = rutinas.LeerArchivo(dt + "apps.py",etapa,nombre,usuario)

            stri=stri.replace('@aplicacion',aplicacion.nombre)
            rutinas.ProcesoPersonalizacion(proyecto,aplicacion.nombre,'apps.py',directorio + nombre + "/" + aplicacion.nombre + "/",stri,nombre,etapa,usuario)

            # Copiar el archivo apps.py de text files en el directorio de la aplicacion
            # Copiar el archivo models.py de text files en el directorio de la aplicacion
            rutinas.CopiarArchivos(dt + "models.py",directorio + nombre + "/" + aplicacion.nombre + "/models.py",etapa,nombre,usuario,True)
            # Copiar el archivo test.py de text files en el directorio de la aplicacion
            rutinas.CopiarArchivos(dt + "tests.py",directorio + nombre + "/" + aplicacion.nombre + "/tests.py",etapa,nombre,usuario,True)

from django.db.models import FloatField,F

def CrearModelos(proyecto,directorio,dt,usuario):

    # Borrar los errores de generacion
    ErroresCreacion.objects.filter(proyecto=proyecto.nombre).delete()

    nombre = proyecto.nombre
    etapa = "CrearModelos"

    # leer el archivo js
    # strjs = TextFiles.objects.get(file = "js_propios.js").texto
    strjs = rutinas.LeerArchivo(dt + "js_propios.js",etapa,nombre,usuario)
    # variable para el manejo de los js
    strfjs = ''

    for aplicacion in Aplicacion.objects.filter(proyecto=proyecto).order_by('ordengeneracion'):

        # Leer archivo modelo.py de core/text_files
        # strTexto = TextFiles.objects.get(file = "modelo.py").texto
        strTexto = rutinas.LeerArchivo(dt + "modelo.py",etapa,nombre,usuario)

        # Para cada modelo crear toda su estructura
        strt = ''
        # Variable para los import de los padres de los modelos
        strmf = '' 
        for modelo in Modelo.objects.filter(padre='nada', aplicacion=aplicacion).order_by('ordengeneracion'):
            # actualiza el archivo js si el modelo tiene buscador de lista
            if modelo.buscadorlista:
                if modelo.padre == 'nada':
                    strfjs += CrearArchivoJs(modelo,aplicacion)

            strt,strmf = ConstruyePropiedades(modelo,proyecto,strt,strmf)
            lista=[]
            RecursivoCreaModelos(modelo,proyecto,lista)
            for mod in lista:
                strt,strmf = ConstruyePropiedades(mod,proyecto,strt,strmf)

        strTexto = strTexto.replace('@foraneos',  strmf)
        strTexto = strTexto.replace('@modelos', strt)

        # models_rol.py seguridad
        if proyecto.conseguridad:
            # stri = TextFiles.objects.get(file = "/registration/models.py").texto
            stri = rutinas.LeerArchivo(dt + "/registration/models_rol.py",etapa,nombre,usuario)
            rutinas.ProcesoPersonalizacion(proyecto,aplicacion.nombre,'models.py',directorio + nombre + "/seguridad/",stri,nombre,etapa,usuario)
            # rutinas.CopiarArchivos(dt + "/registration/models.py",directorio + nombre + "/registration" + "/models.py",etapa,nombre,True)        

        # Grabar el modelo si su aplicacion tiene modelos con propiedades

        if rutinas.AplicacionTienePropiedades(aplicacion):            

            rutinas.ProcesoPersonalizacion(proyecto,aplicacion.nombre,'models.py',directorio + nombre + "/" + aplicacion.nombre + "/",strTexto,nombre,etapa,usuario)

        # actualiza el archivo js
        strjs = strjs.replace('@busqueda', strfjs)

def RecursivoCreaModelos(modelo,proyecto,lista):
    for modhijo in Modelo.objects.filter(padre=modelo.nombre,proyecto=proyecto).order_by('ordengeneracion'):
        lista.append(modhijo)
        RecursivoCreaModelos(modhijo,proyecto,lista)

def ConstruyePropiedades(modelo,proyecto,strt,strmf):
    pi = ''
    strp = ''
    # ver si el modelo tiene padre
    if modelo.padre != 'nada':
        if Modelo.objects.get(nombre=modelo.padre,proyecto=proyecto).aplicacion != modelo.aplicacion:
            modelo_padre = Modelo.objects.get(nombre=modelo.padre,proyecto=proyecto)
            if strmf.find('from ' + modelo_padre.aplicacion.nombre + '.models import ' +  modelo.padre) == -1:
                strmf += 'from ' + modelo_padre.aplicacion.nombre + '.models import ' +  modelo.padre + '\n'              

    # recorrer propiedades
    # Definir el estado previo a propiedad usuario

    for propiedad in Propiedad.objects.filter(modelo=modelo):
        if propiedad.tipo == 'u':
            strp += '\t' + propiedad.nombre + ' =  models.ForeignKey(User,on_delete=models.CASCADE)' + '\n'
            modelo.crearlogin = True
            modelo.save()
            proyecto.conseguridad = True
            proyecto.save()
        if propiedad.tipo == 's':
            if propiedad.mandatoria == False:
                if propiedad.valorinicial == '':
                    pi = ',default=' + "''"
                else:
                    pi = ',default=' + "'" + propiedad.valorinicial + "'"
            else:
                pi = ''
            # strp += '\t' + propiedad.nombre + ' = ' + 'models.CharField(max_length=' + str(propiedad.largostring) + ',default=' + pi + ')' + '\n'
            strp += '\t' + propiedad.nombre + ' = ' + 'models.CharField(max_length=' + str(propiedad.largostring) + pi + ')' + '\n'
        if propiedad.tipo == 'x':
            if propiedad.mandatoria == False:
                if propiedad.valorinicial == '':
                    pi = 'default =' + "''"
                else:
                    pi = 'default=' + "'" + propiedad.valorinicial + "'"
            else:
                pi = ''
            strp += '\t' + propiedad.nombre + ' = ' + 'models.TextField(' + pi + ')' + '\n'
        if propiedad.tipo == 'm':
            if propiedad.mandatoria == False:
                if propiedad.valorinicial == '':
                    pi = 'default=' + '0'
                else:
                    pi = 'default=' + propiedad.valorinicial
            else:
                pi = ''
            strp += '\t' + propiedad.nombre + ' =  models.SmallIntegerField(' + pi  + ')' + '\n'
        if propiedad.tipo == 'i':
            if propiedad.mandatoria == False:
                if propiedad.valorinicial == '':
                    pi = 'default=' + '0'
                else:
                    pi = 'default=' + propiedad.valorinicial
            else:
                pi = ''
            strp += '\t' + propiedad.nombre + ' =  models.IntegerField(' + pi + ')' + '\n'
        if propiedad.tipo == 'l':
            if propiedad.mandatoria == False:
                if propiedad.valorinicial == '':
                    pi = 'default=' + '0'
                else:
                    pi = 'default=' + propiedad.valorinicial
            else:
                pi = ''
            strp += '\t' + propiedad.nombre + ' =  models.BigIntegerField(' + pi + ')' + '\n'
        if propiedad.tipo == 'd':
            if propiedad.mandatoria == False:
                if propiedad.valorinicial == '':
                    pi = 'default=' + '0,'
                else:
                    pi = 'default=' + propiedad.valorinicial + ','
            else:
                pi = ''
            strp += '\t' + propiedad.nombre + ' =  models.DecimalField(' + pi + 'decimal_places=2,max_digits=10)' + '\n'
        if propiedad.tipo == 'f':
            strp += '\t' + propiedad.nombre + ' =  models.ForeignKey(' +  propiedad.foranea + ', on_delete=models.CASCADE,' + ' related_name=' + "'" + '%(class)s_@related' + "'" + ')' + '\n'
            strp = strp.replace('@related', propiedad.nombre)
            # llenar la variable de modelos foraneos
            try:
                modelo_foraneo = Modelo.objects.get(nombre=propiedad.foranea , proyecto=proyecto)
                if modelo_foraneo.aplicacion != modelo.aplicacion:
                    if strmf.find('from ' + modelo_foraneo.aplicacion.nombre + '.models import ' +  propiedad.foranea) == -1:
                        strmf += 'from ' + modelo_foraneo.aplicacion.nombre + '.models import ' +  propiedad.foranea + '\n'  
            except:
                pass
        if propiedad.tipo == 't':
            if propiedad.mandatoria == False:
                if propiedad.valorinicial == '':
                    pi = 'default=' + 'timezone.now'
                else:
                    pi = 'default=' + "'" + propiedad.valorinicial + "'"
            else:
                pi = ''
            strp += '\t' + propiedad.nombre + ' =  models.DateTimeField(' + pi + ')' + '\n'
        if propiedad.tipo == 'e': #TimeField
            if propiedad.mandatoria == False:
                if propiedad.valorinicial == '':
                    pi = 'default=' + "'00:00'"
                else:
                    pi = 'default=' + "'" + propiedad.valorinicial + "'"
            else:
                pi = ''
            strp += '\t' + propiedad.nombre + ' = ' + 'models.TimeField(' + pi + ')' + '\n'
            # strp += '\t' + propiedad.nombre + ' =  models.TimeField(' + pi + ')' + '\n'
        if propiedad.tipo == 'n': #DateField
            if propiedad.mandatoria == False:
                if propiedad.valorinicial == '':
                    pi = 'default=' + 'timezone.now'
                else:
                    pi = 'default=' + "'" + propiedad.valorinicial + "'"
            else:
                pi = ''
            strp += '\t' + propiedad.nombre + ' = ' + 'models.DateField(' + pi + ')' + '\n'
            # strp += '\t' + propiedad.nombre + ' =  models.TimeField(' + pi + ')' + '\n'
        if propiedad.tipo == 'b':
            if propiedad.mandatoria == False:
                if propiedad.valorinicial == '':
                    pi = 'default=' + 'False'
                else:
                    pi = 'default=' + propiedad.valorinicial
            else:
                pi = ''
            strp += '\t' + propiedad.nombre + ' =  models.BooleanField(' + pi + ')' + '\n'
        if propiedad.tipo == 'r':
            if propiedad.mandatoria == False:
                if propiedad.valorinicial == '':
                    pi = 'default=' + "''"
                else:
                    pi = 'default=' + "'" + propiedad.valorinicial + "'"
            else:
                pi = ''
            strp += '\t' + propiedad.nombre + ' = ' + 'models.CharField(max_length=' + str(propiedad.largostring) + ',' + pi + ')' + '\n'
        if propiedad.tipo == 'a':
            if propiedad.mandatoria == False:
                if propiedad.valorinicial == '':
                    pi = 'default=' + "''"
                else:
                    pi = 'default=' + "'" + propiedad.valorinicial + "'"
            else:
                pi = ''
            strp += '\t' + propiedad.nombre + ' = ' + 'models.CharField(max_length=' + str(propiedad.largostring) + ',' + pi + ')' + '\n'
        if propiedad.tipo == 'h':
            strp += '\t' + propiedad.nombre + ' = ' + 'RichTextField()' + '\n'
        if propiedad.tipo == 'p':
            strp += '\t' + propiedad.nombre + ' = models.ImageField(upload_to=' + "'" + modelo.nombre + "'" + ',blank=True,null=True)' + '\n'



    # for propiedad in Propiedad.objects.filter(modelo=modelo):
    #     strp += rutinas.PropiedadesModelo(proyecto, modelo, propiedad)

    if strp != '':
        #ver si el modelo es dependiente
        if modelo.padre != 'nada':
            strp += '\t' + modelo.padre + ' =  models.ForeignKey(' +  modelo.padre + ', on_delete=models.CASCADE' + ')' + '\n'

        strmodelo = IdentificacionModelo(modelo, strp)

        strp = ''
        strt += strmodelo + '\n'

    return strt,strmf

def CrearVistas(proyecto,directorio,dt,usuario):

    # Borrar los errores de generacion
    ErroresCreacion.objects.filter(proyecto=proyecto.nombre).delete()

    nombre = proyecto.nombre
    etapa = "CrearVistas"

    # Para cada modelo
    # strim = ''
    # strif = ''
    strlh = ''

    for aplicacion in Aplicacion.objects.filter(proyecto=proyecto):

        if aplicacion.nombre == 'core':
            # Preparar el archivo core_view.py de text files en el directorio de la aplicacion core
            # stri = TextFiles.objects.get(file = "core_view.py").texto
            stri = rutinas.LeerArchivo(dt + 'core_view.py',etapa,nombre,usuario)
            # Ver las aplicaciones y los modelos
            strap = ''
            strArbol = ''
            for app in Aplicacion.objects.filter(proyecto = proyecto):
                if app.nombre != 'core' and app.nombre != 'registration' and app.nombre != 'seguridad':
                    strap += "if self.request.GET['aplicacion'] == '@aplicacion':" + "\n"
                    strap = strap.replace('@aplicacion', app.nombre)    
                    for modelo in Modelo.objects.filter(aplicacion = app):
                        strap += "  lista_modelos.append(" + modelo.nombre + ")" + "\n"
                        # Forma los arboles de navegacion teeview
                        if modelo.padre == 'nada':
                            if modelo.treeview:
                                strArbol += rutinas.ArbolNavegacion(modelo)
                                strArbol = strArbol.replace('@modelo',modelo.nombre)
            stri = stri.replace('@lista_modelos', strap)
            stri = stri.replace('@arbol', strArbol)
            stri = stri.replace('@listafinal', rutinas.ListaFinal())
            if proyecto.conroles:
                stroles = rutinas.LeerArchivo(dt + 'roles.py',etapa,nombre,usuario)
                stri = stri.replace('@roles', stroles)
            else:
                stri = stri.replace('@roles', '')




            rutinas.ProcesoPersonalizacion(proyecto,aplicacion.nombre,'views.py',directorio + nombre + "/" + aplicacion.nombre + "/",stri,nombre,etapa,usuario)
            
        strif = ''
        strim = ''
        strmp = ''
        strmh = ''

        # leer archivo vistas.py de core/text_files
        # stri = TextFiles.objects.get(file = "vistas.py").texto
        stri = rutinas.LeerArchivo(dt + 'vistas.py',etapa,nombre,usuario)

        strmp = 'class HomeView(TemplateView):' + '\n'
        strmp += '\ttemplate_name = ' + "'" + aplicacion.nombre + '/home.html' + "'" + '\n'
        strmp += '\n'                

        for modelo in Modelo.objects.filter(aplicacion=aplicacion,proyecto=proyecto):

            if modelo.sinbasedatos == False:

                if Propiedad.objects.filter(modelo=modelo).count() > 0:
                    # Lista de import de formularios
                    if strif.find('from .forms import ' + modelo.nombre + 'Form') == -1:
                        strif += 'from .forms import ' + modelo.nombre + 'Form' + '\n'                    #importa modelos
                    if strim.find('from ' +  Aplicacion.objects.get(id=modelo.aplicacion.id).nombre + '.models import ' + modelo.nombre) == -1:
                        strim += 'from ' +  Aplicacion.objects.get(id=modelo.aplicacion.id).nombre + '.models import ' + modelo.nombre + '\n'  

                    if modelo.padre != 'nada': 
                        
                        # Editar modelo hijo
                        strv = VistaEditarModeloHijo(proyecto,aplicacion,modelo)
                        strvt,strim = VistaCrearModeloHijo(proyecto,aplicacion,modelo,strim)
                        strv += strvt
                        strv += VistaBorrarModeloHijo(proyecto,aplicacion,modelo)

                        # Encuentra la aplicacion real
                        strv = rutinas.AplicacionReal(modelo,strv,proyecto)

                        strmh += strv + '\n'
                        strv = ''

                        #importa modelos de padres y abuelos
                        modelo_padre = Modelo.objects.get(nombre=modelo.padre , proyecto=proyecto)                       
                        if strim.find('from ' +  Aplicacion.objects.get(id=modelo_padre.aplicacion.id).nombre + '.models import ' + modelo_padre.nombre) == -1:
                            strim += 'from ' +  Aplicacion.objects.get(id=modelo_padre.aplicacion.id).nombre + '.models import ' + modelo_padre.nombre + '\n'  

                        if modelo_padre.padre != 'nada': # tiene abuelo
                            modelo_abuelo = Modelo.objects.get(nombre=modelo_padre.padre , proyecto=proyecto)
                            if strim.find('from ' +  Aplicacion.objects.get(id=modelo_abuelo.aplicacion.id).nombre + '.models import ' + modelo_abuelo.nombre) == -1:
                                strim += 'from ' +  Aplicacion.objects.get(id=modelo_abuelo.aplicacion.id).nombre + '.models import ' + modelo_abuelo.nombre + '\n'  

                        #importa modelos de hijos
                        for modelo_hijo in Modelo.objects.filter(padre=modelo.nombre , proyecto=proyecto):
                            if strim.find('from ' +  Aplicacion.objects.get(id=modelo_hijo.aplicacion.id).nombre + '.models import ' + modelo_hijo.nombre) == -1:
                                strim += 'from ' +  Aplicacion.objects.get(id=modelo_hijo.aplicacion.id).nombre + '.models import ' + modelo_hijo.nombre + '\n'  

                    else: 

                        # Importa dash forms
                        # tiene_dash = False
                        # for propiedad in Propiedad.objects.filter(modelo=modelo):
                        #     if propiedad.dashboard:
                        #         tiene_dash=True
                        #         break
                        if rutinas.TieneDash(modelo):
                            if strif.find('from .forms import Dash' + modelo.nombre + 'Form') == -1:
                                strif += 'from .forms import Dash' + modelo.nombre + 'Form' + '\n'                    #importa modelos
                        strif += 'from .forms import Fill' + modelo.nombre + 'Form' + '\n'                    #importa modelos

                        # Listar Modelos Raiz 
                        strv = VistaListarRaiz(aplicacion, modelo, proyecto)

                        # Editar Modelos Raiz
                        strv += VistaEditarRaiz(proyecto,aplicacion,modelo)

                        # Crear Modelos Raiz 
                        strv += VistaCrearRaiz(proyecto,aplicacion,modelo)

                        # Borrar Modelos Raiz 
                        strv += VistaBorrarRaiz(proyecto,aplicacion,modelo)

                        # Vistas para dashboard
                        if rutinas.TieneDash(modelo):
                            strv += rutinas.VistaDashBoard(modelo, proyecto)
                        # Vistas para fill
                        strv += rutinas.VistaFill(modelo, proyecto)

# Reporte nuevo

                        # # Reporte escalonado
                        # strr = LeerArchivo(dt + 'modelo_reporte_escalonado.py',etapa,nombre,usuario)

                        # strv += strvt

                        # strv = strv.replace('@aplicacionreal',aplicacion.nombre)
                        # strv = strv.replace('@aplicacion', aplicacion.nombre)
                        # strv = strv.replace('@modelo', modelo.nombre)

# Reporte nuevo

# Inicio Report Platypus

                        strr = rutinas.LeerArchivo(dt + 'modelo_reporte_platypus.py',etapa,nombre,usuario)

                        listaestilos = []
                        listatitulocolumnas = []
                        # maxpuntos
                        # 792,612,841,595
                        letterP = [612,792]
                        A4P = [595,841]
                        anchopagina = 0
                        altopagina = 0
                        maxpuntos = 0
                        if modelo.reportsize == 'L':
                            if modelo.reportorientation == 'P':
                                anchopagina = letterP[0]
                                altopagina = letterP[1]
                                maxpuntos = str(letterP[0])        
                            else:
                                anchopagina = letterP[1]
                                altopagina = letterP[0]
                                maxpuntos = str(letterP[1])        
                        else:
                            if modelo.reportorientation == 'P':
                                anchopagina = A4P[0]
                                altopagina = A4P[1]
                                maxpuntos = str(A4P[0])        
                            else:
                                anchopagina = A4P[1]
                                altopagina = A4P[0]
                                maxpuntos = str(A4P[1])        

                        strir = ''
                        if proyecto.avatar:
                            strir = '\tcd = os.getcwd()\n'
                            strir += '\tlogo = cd + "/core/static/core/img/logo.png"\n'
                            strir += '\tim_auto = Image(logo, width=@imagenwidth,height=@imagenheight)\n'
                            try:
                                strir = strir.replace('@imagenwidth',modelo.dimensioneslogo.split(',')[1])
                                strir = strir.replace('@imagenheight',modelo.dimensioneslogo.split(',')[0])
                            except:
                                strir = strir.replace('@imagenwidth','15')
                                strir = strir.replace('@imagenheight','15')

                        else:
                            strir = '\tim_auto = ' + "''" + '\n'

                        strv += strr


                        # reporte con zonas
                        lista = ZonaReporte.objects.filter(modeloid = modelo.id)
                        strrt = ''
                        if lista.count() > 0:
                            for reporte in lista:
                                strr = rutinas.LeerArchivo(dt + 'modelo_codigo_reporte_platypus.py',etapa,nombre,usuario)
                                strrt += VistaReportePlatypus(listaestilos,listatitulocolumnas,proyecto,aplicacion,modelo,strr,reporte,maxpuntos,'',reporte.nombre)
                            # strrt = 'def Reporte@modeloView(request):\n' + strrt
                            # strrt += '    return HttpResponseRedirect(' + "'" + '/@aplicacion/listar_@modelo' + "'" + ')'
                            # strv = strv.replace('@codigoreportes', strrt)
                            # strv = strv.replace('@modelo', modelo.nombre)
                        # reporte adhoc
                        lista = ReporteAdHocObjeto.objects.filter(modeloid = modelo.id)
                        # strrt = ''
                        if lista.count() > 0:
                            for reporte in lista:
                                # if reporte.nombre != '':
                                if reporte.nombre == 'balance':
                                    strr = rutinas.LeerArchivo(dt + 'modelo_codigo_reporte_platypus.py',etapa,nombre,usuario)
                                    strrt += VistaReportePlatypus(listaestilos,listatitulocolumnas,proyecto,aplicacion,modelo,strr,reporte,maxpuntos,'adhoc',reporte.nombre)
                        # Reportes normales
                        strr = rutinas.LeerArchivo(dt + 'modelo_codigo_reporte_platypus.py',etapa,nombre,usuario)
                        strr = VistaReportePlatypus(listaestilos,listatitulocolumnas,proyecto,aplicacion,modelo,strr,None,maxpuntos,'','')
                        strr += strrt
                        strr = 'def Reporte@modeloView(request):\n' + strr
                        strr += '    return HttpResponseRedirect(' + "'" + '/@aplicacion/listar_@modelo' + "'" + ')' + '\n\n'

                        # estilos

                        strr += 'def encabezado@modelo(canvas,document):' + '\n'
                        strr += '#@[p_encabezado_' + modelo.nombre + '_01]' + '\n' 
                        strr += '@reportelogo' + '\n'
                        strr += '\tdata = [[im_auto,@titproyecto]]' + '\n'
                        strr += "\ttblstyle = TableStyle([('LINEBELOW', (0, 0), (-1, -1), @grosorlineaencabezado, colors.black)," + '\n'
                        strr += "\t\t\t\t\t('FONT', (0, 0), (-1, -1), document.font)," + '\n'
                        strr += "\t\t\t\t\t('FONTSIZE', (0, 0), (-1, -1), document.fontSize)," + '\n'
                        strr += "\t\t\t\t\t('VALIGN',(0,0),(-1,-1),'MIDDLE')," + '\n'
                        strr += "\t\t\t\t\t('ALIGN', (0, 0), (-1, -1), 'CENTER')," + '\n'
                        strr += "\t\t\t\t\t('BOTTOMPADDING', (0, 0), (-1, -1), 15)," + '\n'
                        strr += "\t\t\t\t\t('TEXTCOLOR',(0,0),(-1,-1),@colorencabezado)," + '\n'
                        strr += '#@[p_encabezado_' + modelo.nombre + '_02]' + '\n' 
                        strr += "\t\t\t\t\t])" + '\n'
                        strr += '#@[p_encabezado_' + modelo.nombre + '_03]' + '\n' 
                        strr += '\tsuma = @suma' + '\n'
                        strr += '#@[p_encabezado_' + modelo.nombre + '_04]' + '\n' 
                        strr += '\tdocument.leftMargin = @lm' + '\n'
                        strr += '#@[p_encabezado_' + modelo.nombre + '_05]' + '\n' 
                        strr += '\tdocument.rightMargin = @rm' + '\n'
                        strr += '#@[p_encabezado_' + modelo.nombre + '_06]' + '\n' 
                        strr += '\tt = Table(data,colWidths=[@esplogo,@espproyecto])' + '\n'
                        strr += '#@[p_encabezado_' + modelo.nombre + '_07]' + '\n' 
                        strr += '\tt.setStyle(tblstyle)' + '\n'
                        strr += '#@[p_encabezado_' + modelo.nombre + '_08]' + '\n' 
                        strr += '\tt.wrapOn(canvas,@mi,@posyreporte)' + '\n'
                        strr += '#@[p_encabezado_' + modelo.nombre + '_09]' + '\n' 
                        strr += '\tt.drawOn(canvas, @mi,@posyreporte)'  + '\n'

                        for texto in listaestilos:
                            strr += texto + '\n'
                        for texto in listatitulocolumnas:
                            strr += texto + '\n'

                        if modelo.colorencabezado[0] == '#':
                            strr = strr.replace('@colorencabezado', "'" + modelo.colorencabezado + "'")
                        else:
                            strr = strr.replace('@colorencabezado', 'colors.' + modelo.colorencabezado)

                        # calcula ancho de propiedades
                        suma = 0
                        for prop in Propiedad.objects.filter(modelo=modelo):
                            if prop.enreporte:
                                suma += prop.anchoenreporte
                        strr = strr.replace('@suma', str(suma))
                        strr = strr.replace('@lm', modelo.margenes.split(',')[0])
                        strr = strr.replace('@rm', modelo.margenes.split(',')[1])
                        strr = strr.replace('@reportelogo', strir)
                        strr = strr.replace('@titproyecto', "'" + proyecto.titulo + "'")
                        strr = strr.replace('@esplogo', modelo.dimensioneslogo.split(',')[1])

                        strr = strr.replace('@espproyecto', str(anchopagina) + ' - ' + modelo.dimensioneslogo.split(',')[1] + ' - document.leftMargin - document.rightMargin' )
                        strr = strr.replace('@mi', 'document.leftMargin')
                        strr = strr.replace('@md', 'document.rightMargin')
                        strr = strr.replace('@posyreporte', str(altopagina) + ' - (document.topMargin) * 0.6')
                        strr = strr.replace('@grosorlineaencabezado', str(modelo.grosorlineaencabezado))
                        strr = strr.replace('@alturafontcolumnas', str(modelo.font_columnas.split(',')[1]))

                        strv = strv.replace('@codigoreportes', strr)
                        strv = strv.replace('@modelo', modelo.nombre)
                        strv = strv.replace('@alturafonttexto', str(modelo.font.split(',')[1]))

# Final Report Platypus

                        strv = strv.replace('@paraborrar', ParaBorrar(modelo))
                        
                        #importa modelos de hijos
                        for modelo_hijo in Modelo.objects.filter(padre=modelo.nombre , proyecto=proyecto):
                            if strim.find('from ' +  Aplicacion.objects.get(id=modelo_hijo.aplicacion.id).nombre + '.models import ' + modelo_hijo.nombre) == -1:
                                strim += 'from ' +  Aplicacion.objects.get(id=modelo_hijo.aplicacion.id).nombre + '.models import ' + modelo_hijo.nombre + '\n'  

                        # lista hijos
                        for model in Modelo.objects.filter(padre=modelo.nombre  , proyecto=proyecto):
                            strlh += '\t\t' + model.nombre + '_lista = ' + model.nombre + '.objects.filter(' + modelo.nombre + ' = ' + modelo.nombre + ')' + '\n'
                            strlh += '\t\t' + 'context[' + "'" + 'lista' + model.nombre + "'" + '] =  ' + model.nombre  + '_lista' + '\n'

                            if proyecto.conroles:
                                strlh += '\t\t# Controla si el usuario puede listar registros del modelo: ' + model.nombre +  '\n'
                                strlh += "\t\tif not roles.PuedeModelo('" + model.nombre + "',self.request.user.username,'listar'):" + '\n'
                                strlh += '#@[p_roles_' + modelo.nombre + '_01]' + '\n' 
                                strlh += '\t\t\t' + 'context[' + "'" + 'lista' + model.nombre + "'" + '] = None' + '\n'
                                for pr in Propiedad.objects.filter(modelo=model):
                                    strlh += '\t\t# Controla si el usuario puede ver el valor a la propiedad: ' + pr.nombre + ' del modelo' + '\n'
                                    strlh += '#@[p_roles_' + modelo.nombre + '_' + pr.nombre + '_01]' + '\n' 
                                    strlh += "\t\tcontext['puede_ver_" + pr.nombre + "'] = roles.Puede('" + pr.nombre + "',self.request.user.username,'puedever')" + '\n'
                                strlh += '\t\t# Controla si el usuario puede insertar registros al modelo: ' + model.nombre +  '\n'
                                strlh += '#@[p_roles_' + modelo.nombre + '_02]' + '\n' 
                                strlh += "\t\tcontext['puede_insertar_" + model.nombre + "'] = roles.PuedeModelo('" + model.nombre + "',self.request.user.username,'insertar')" + '\n'
                                strlh += '#@[p_roles_' + modelo.nombre + '_03]' + '\n' 
                                strlh += '\t\t# Controla si el usuario puede editar registros al modelo' + '\n'
                                strlh += "\t\tcontext['puede_editar_" + model.nombre + "'] = roles.PuedeModelo('" + model.nombre + "',self.request.user.username,'editar')" + '\n'
                                strlh += '#@[p_roles_' + modelo.nombre + '_04]' + '\n' 
                                strlh += '\t\t# Controla si el usuario puede borrar registros al modelo' + '\n'
                                strlh += '#@[p_roles_' + modelo.nombre + '_05]' + '\n' 
                                strlh += "\t\tcontext['puede_borrar_" + model.nombre + "'] = roles.PuedeModelo('" + model.nombre + "',self.request.user.username,'borrar')" + '\n'

                        strv = strv.replace('@listahijos', strlh)
                        strlh = ''    

                        strmp += strv + '\n'
                        strv = ''
            else:

                # Lista de import de formularios
                strif += '# Importa la libreria forms' + '\n'
                if strif.find('from .forms import ' + modelo.nombre + 'Form') == -1:
                    strif += 'from .forms import ' + modelo.nombre + 'Form' + '\n'

                strv += VistaModeloSinBase(aplicacion,modelo)

                strmp += strv + '\n'
                strv = ''
            
        # reemplazar modeloshijo y padre

        strim = '#@[p_importmodelos_01]\n\n' + strim + '\n' 
        strim = strim + '\n' + '#@[p_importmodelos_02]\n\n'
        strif = strif + '\n' + '#@[p_importforms_02]\n\n'
        strmp = strmp + '\n' + '#@[p_modelospadre_02]\n\n'
        strmh = strmh + '\n' + '#@[p_modeloshijo_02]\n\n'
        
        stri = stri.replace('@importmodelos', strim)
        stri = stri.replace('@importforms', strif)
        stri = stri.replace('@modelospadre', strmp)
        stri = stri.replace('@modeloshijo', strmh)
        stri = stri.replace('@aplicacion', aplicacion.nombre)

        # Reportes
        try:
            stri = stri.replace("@nombre",proyecto.nombre)

        except:
            pass

        strif = ''
        strmp = ''

        # Ver si se tienen roles en el proyecto
        if proyecto.conroles:
            stro = '#@[p_import_roles_01]' + '\n'
            stro += 'from core import views as roles' + '\n'
            stro += '#@[p_import_roles_02]' + '\n'
            stri = stri.replace('@importroles',stro)
        else:
            stri = stri.replace('@importroles','')

        # Grabar el modelo si su aplicacion tiene modelos con propiedades
        if rutinas.AplicacionTienePropiedades(aplicacion):

            rutinas.ProcesoPersonalizacion(proyecto,aplicacion.nombre,'views.py',directorio + nombre + "/" + aplicacion.nombre + "/",stri,nombre,etapa,usuario)

    # Manejo de las vistas de los modelos hijos que son foreign en otros modelos select
    strVista = '#@[p_load_@modelos_01]' + '\n' 
    strVista += "def load_@modelos(request):" + '\n'
    strVista += "\tidp = request.GET.get('@padre')" + '\n'
    strVista += "\tpadre = @padre.objects.get(id=idp)" + '\n'
    strVista += "\t@modelos = @modelo.objects.filter(@padre=padre).order_by('@propiedad')" + '\n'
    strVista += "\treturn render(request, '@aplicacion/load_@modelo.html', {'@modelos': @modelos})" + '\n'
    strVista += '#@[p_load_@modelos_02]' + '\n' 

    for aplicacion in Aplicacion.objects.filter(proyecto=proyecto):
        strLoadHijos = ''
        strForeign = ''
        strh = ''
        if aplicacion.nombre != 'core' and aplicacion.nombre != 'registration' and aplicacion.nombre != 'seguridad':# and aplicacion.nombre == 'generales':
            strh = rutinas.LeerArchivoEnTexto(directorio + nombre + '/' + aplicacion.nombre + '/views.py',etapa,nombre,usuario)
            for modelo in Modelo.objects.filter(aplicacion=aplicacion):
                for propiedad in Propiedad.objects.filter(modelo=modelo):
                    if propiedad.tipo == 'f':
                        modelo_foraneo = Modelo.objects.get(nombre=propiedad.foranea,proyecto=proyecto)
                        if strh.find('from ' + modelo_foraneo.aplicacion.nombre + '.models import ' + modelo_foraneo.nombre) == -1:
                            strForeign += 'from ' + modelo_foraneo.aplicacion.nombre + '.models import ' + modelo_foraneo.nombre + '\n'
                        if modelo_foraneo.padre !='nada':
                            # Ver si el padre esta en el mismo modelo
                            for modelo_padre in Modelo.objects.filter(proyecto=proyecto):
                                if modelo_padre.nombre == modelo_foraneo.padre:
                                    # Existe el modelo padre la llave foranea
                                    # Crear el url para la lista de modelos hijo
                                    strLoadHijos += strVista
                                    strLoadHijos = strLoadHijos.replace('@modelo',modelo_foraneo.nombre)
                                    strLoadHijos = strLoadHijos.replace('@padre',modelo_padre.nombre)
                                    strLoadHijos = strLoadHijos.replace('@aplicacion',modelo.aplicacion.nombre)
                                    strLoadHijos = strLoadHijos.replace('@propiedad',modelo_foraneo.nombreborrar)
                                    break
        if rutinas.AplicacionTienePropiedades(aplicacion):
            # Leer el html de insercion y update del modelo con llaves foraneas
            if strForeign != '':
                strForeign = '#@[p_import_foreign_01]' + '\n' + strForeign + '\n'
                strForeign += '#@[p_import_foreign_02]' + '\n'

            strh = strh.replace('@importforeign',strForeign)
            strh = strh.replace('@loadhijos',strLoadHijos)
            strForeign = ''
            strLoadHijos = ''
            rutinas.EscribirArchivo(directorio + nombre + "/" + aplicacion.nombre + '/views.py',etapa,nombre,strh,usuario,True)

def ParaBorrar(modelo):
    if modelo.nombreborrar != '':
        # separa los componentes
        strpb = modelo.nombreborrar.split("+ '-' + ")
        strpbt = ''
        for strc in strpb:
            if strpbt == '':
                strpbt = 'str(modelo_current.' + strc + ')'
            else:
                strpbt += '+ ' + "'" + "-" + "'" + ' + ' + 'str(modelo_current.' + strc + ')'
        # strv = strv.replace('@paraborrar', modelo_current.nombreborrar)
    else:
        for prop in Propiedad.objects.filter(modelo=modelo):
            strpbt = 'modelo_current.' + prop.nombre
            modelo.nombreborrar = prop.nombre
            modelo.save()
            break
    return strpbt

def RecursivoDash(modelo,lista):
    for prop in Propiedad.objects.filter(modelo = modelo):
        if prop.dashboard:
            lista.append()

def CrearUrls(proyecto,directorio,dt,usuario):

    # Borrar los errores de generacion
    ErroresCreacion.objects.filter(proyecto=proyecto.nombre).delete()

    nombre = proyecto.nombre
    etapa = "CrearUrls"

    # urls para el proyecto
    strlfp = ''
    strlpp = ''
    for aplicacion in Aplicacion.objects.filter(proyecto=proyecto):

        if rutinas.AplicacionTienePropiedades(aplicacion) or aplicacion.nombre == 'core':
            # Preparar los patterns para urls del proyecto
            if strlfp.find('from @aplicacion.urls import @aplicacion_patterns') == -1:
                strlfp += 'from @aplicacion.urls import @aplicacion_patterns' + '\n'
            if aplicacion.nombre == 'core':
                strlpp += '\tpath(' + "'" + "'" + ',include(@aplicacion_patterns)),' + '\n'
            else:    
                strlpp += '\tpath(' + "'" + '@aplicacion/' + "'" + ',include(@aplicacion_patterns)),' + '\n'

            strlfp = strlfp.replace('@aplicacion', aplicacion.nombre)
            strlpp = strlpp.replace('@aplicacion', aplicacion.nombre)

    # Leer el archivo urls_proyecto.py de text files
    # stri = TextFiles.objects.get(file = "urls_proyecto.py").texto
    stri = rutinas.LeerArchivo(dt + "urls_proyecto.py",etapa,nombre,usuario)

    stri = stri.replace('@listafrompatterns', strlfp)
    stri = stri.replace('@listapathpatterns', strlpp)

    rutinas.ProcesoPersonalizacion(proyecto,nombre,'urls.py',directorio + nombre + "/" + nombre + "/",stri,nombre,etapa,usuario)

    for aplicacion in Aplicacion.objects.filter(proyecto=proyecto):

        # Copiar el archivo urls.py de text files en el directorio de la aplicacion core
        if aplicacion.nombre == 'core':
            # stri = TextFiles.objects.get(file = "core_urls.py").texto
            stri = rutinas.LeerArchivo(dt + "core_urls.py",etapa,nombre,usuario)

            rutinas.ProcesoPersonalizacion(proyecto,aplicacion.nombre,'urls.py',directorio + nombre + "/" + aplicacion.nombre + "/",stri,nombre,etapa,usuario)

        # leer archivo urls.py de core/text_files
        # stri = TextFiles.objects.get(file = "urls_modelo.py").texto
        stri = rutinas.LeerArchivo(dt + "urls_modelo.py",etapa,nombre,usuario)

        # Para cada modelo
        strt = ''
        strp = ''
        strlv = ''

        if strlv.find('from .views import HomeView') == -1:
            strlv = 'from .views import HomeView' + '\n'

        strp = '\tpath(' + "''" + ',@required(HomeView.as_view()), name=' + "'" + 'home' + "'" + '),' + '\n'

        if proyecto.conseguridad:
            if aplicacion.homestaff:
                strp = strp.replace('@required', 'staff_member_required')
            elif aplicacion.homelogin:
                strp = strp.replace('@required', 'login_required')
            else:
                strp = strp.replace('@required', '')

        for modelo in Modelo.objects.filter(aplicacion=aplicacion):
            if modelo.sinbasedatos == False:
                if Propiedad.objects.filter(modelo=modelo).count() > 0:
                    # tiene_dash=False
                    if modelo.padre == 'nada':
                        if strlv.find('from .views import Listar@moduloView, Crear@moduloView, Editar@moduloView, Borrar@moduloView, Reporte@moduloView') == -1:
                            strlv += 'from .views import Listar@moduloView, Crear@moduloView, Editar@moduloView, Borrar@moduloView, Reporte@moduloView' + '\n'
                        if rutinas.TieneDash(modelo):
                            if strlv.find('from .views import Dash@moduloView') == -1:
                                strlv += 'from .views import Dash@moduloView' + '\n'
                        strlv += 'from .views import Fill@moduloView' + '\n'
                    else:
                        if strlv.find('from .views import Crear@moduloView, Editar@moduloView, Borrar@moduloView') == -1:
                            strlv += 'from .views import Crear@moduloView, Editar@moduloView, Borrar@moduloView' + '\n'

                    strlv = strlv.replace('@modulo', modelo.nombre)

                    if modelo.padre == 'nada':
                        strp += '\tpath(' + "'listar_" + '@modulom/' + "'" + ',@required(Listar@moduloView.as_view()), name=' + "'" + 'listar_@modulom' + "'" + '),' + '\n'
                        strp += '\tpath(' + "'reporte_" + '@modulom/' + "'" + ',Reporte@moduloView, name=' + "'" + 'reporte_@modulom' + "'" + '),' + '\n'
                        if rutinas.TieneDash(modelo):
                            strp += '\tpath(' + "'dash_" + '@modulom/' + "'" + ',Dash@moduloView.as_view(), name=' + "'" + 'dash_@modulom' + "'" + '),' + '\n'
                        strp += '\tpath(' + "'fill_" + '@modulom/' + "'" + ',Fill@moduloView.as_view(), name=' + "'" + 'fill_@modulom' + "'" + '),' + '\n'

                        if proyecto.conseguridad:
                            # seguridad listar
                            if modelo.listastaff:
                                strp = strp.replace('@required', 'staff_member_required')
                            elif modelo.listalogin:
                                strp = strp.replace('@required', 'login_required')
                            else:
                                strp = strp.replace('@required', '')

                    strp += '\tpath(' + "'" + 'editar_@modulom/<int:pk>/' + "'" + ',@required(Editar@moduloView.as_view()), name=' + "'" + 'editar_@modulom' + "'" +'),' + '\n'
                    # seguridad editar
                    if proyecto.conseguridad:
                        if modelo.editarstaff:
                            strp = strp.replace('@required', 'staff_required')
                        elif modelo.editarlogin:
                            strp = strp.replace('@required', 'login_required')
                        else:
                            strp = strp.replace('@required', '')

                    strp += '\tpath(' + "'" + 'crear_@modulom/' + "'" + ',@required(Crear@moduloView.as_view()), name=' + "'" + 'crear_@modulom' + "'" + '),' + '\n'
                    # seguridad crear
                    if proyecto.conseguridad:
                        if modelo.crearstaff:
                            strp = strp.replace('@required', 'staff_member_required')
                        elif modelo.crearlogin:
                            strp = strp.replace('@required', 'login_required')
                        else:
                            strp = strp.replace('@required', '')

                    strp += '\tpath(' + "'" + 'borrar_@modulom/<int:pk>/' + "'" + ',@required(Borrar@moduloView.as_view()), name=' + "'" + 'borrar_@modulom' + "'" + '),' + '\n'
                    # seguridad borarr
                    if proyecto.conseguridad:
                        if modelo.borrarstaff:
                            strp = strp.replace('@required', 'staff_member_required')
                        elif modelo.borrarlogin:
                            strp = strp.replace('@required', 'login_required')
                        else:
                            strp = strp.replace('@required', '')

                    strp = strp.replace('@required', '')
                    strp = strp.replace('@modulom', modelo.nombre)
                    strp = strp.replace('@modulo', modelo.nombre)

                    strt += strp + '\n'
                    strp = ''
            else:
                if strlv.find('from .views import @moduloView') == -1:
                    strlv += 'from .views import @moduloView' + '\n'
                strlv = strlv.replace('@modulo', modelo.nombre)
                
                strp += '\tpath(' + "'" + '@modulo/' + "'" + ',@required(@moduloView.as_view()), name=' + "'" + '@modulo' + "'" +'),' + '\n'
                strp = strp.replace('@modulo', modelo.nombre)                # seguridad listar
                if modelo.listastaff:
                    strp = strp.replace('@required', 'staff_member_required')
                elif modelo.listalogin:
                    strp = strp.replace('@required', 'login_required')
                else:
                    strp = strp.replace('@required', '')
                strt += strp + '\n'
                strp = ''

        if strt != '':
            stri = stri.replace('@aplicacion', aplicacion.nombre)
            stri = stri.replace('@listaurls', strt)
            stri = stri.replace('@listaviews', strlv)

        # strt = EscribePersonalizacion(proyecto,aplicacion,'urls.py',strt)

        # Grabar el modelo si su aplicacion tiene modelos con propiedades
        if rutinas.AplicacionTienePropiedades(aplicacion):

            rutinas.ProcesoPersonalizacion(proyecto,aplicacion.nombre,'urls.py',directorio + nombre + "/" + aplicacion.nombre + "/",stri,nombre,etapa,usuario)

    # Manejo de los urls de los modelos hijos que son foreign en otros modelos select
    for aplicacion in Aplicacion.objects.filter(proyecto=proyecto):
        strUrls = ''
        strLoad = ''

        # Copiar el archivo urls.py de text files en el directorio de la aplicacion core
        if aplicacion.nombre != 'core' and aplicacion.nombre != 'registration':    
            for modelo in Modelo.objects.filter(aplicacion=aplicacion):
                for propiedad in Propiedad.objects.filter(modelo=modelo):
                    if propiedad.tipo == 'f':
                        modelo_foraneo = Modelo.objects.get(nombre=propiedad.foranea,proyecto=proyecto)
                        if modelo_foraneo.padre !='nada':
                            # Ver si el padre esta en el mismo modelo
                            for modelo_padre in Modelo.objects.filter(proyecto=proyecto):
                                if modelo_padre.nombre == modelo_foraneo.padre:
                                    # Existe el modelo padre la llave foranea
                                    # Crear el url para la lista de modelos hijo
                                    strUrls += "\tpath('ajax/load-@modelos/', load_@modelos, name='ajax_load_@modelos')," + '\n'
                                    if strLoad.find("from .views import load_@modelos") == -1:
                                        strLoad += "from .views import load_@modelos" + '\n'
                                    strUrls = strUrls.replace('@modelo',modelo_foraneo.nombre)
                                    strLoad = strLoad.replace('@modelo',modelo_foraneo.nombre)
                                    break
        if rutinas.AplicacionTienePropiedades(aplicacion):                                    
            # Leer el html de insercion y update del modelo con llaves foraneas
            strh = rutinas.LeerArchivoEnTexto(directorio + nombre + '/' + aplicacion.nombre + '/urls.py',etapa,nombre,usuario)
            strh = strh.replace('@urlshijos',strUrls)
            strh = strh.replace('@loadhijos',strLoad)
            rutinas.EscribirArchivo(directorio + nombre + "/" + aplicacion.nombre + '/urls.py',etapa,nombre,strh,usuario,True)

def CrearTemplates(proyecto,directorio,directoriogenesis,dt,usuario):

    # Leer la aplicacion core
    appCore = Aplicacion.objects.get(proyecto=proyecto,nombre='core')

    # Actualizar las alturas del medio
    proyecto.altofilamedio = -100
    proyecto.altocolumnamedioizquierda = -100
    proyecto.altocolumnamedioderecha = -100
    proyecto.altocolumnamediocentro = -100
    proyecto.save()

    # Borrar los errores de generacion
    ErroresCreacion.objects.filter(proyecto=proyecto.nombre).delete()

    nombre = proyecto.nombre
    etapa = "CrearTemplates"
    dc = "\""

    # JS_PROPIOS
    rutinas.CrearJsPropios(proyecto,nombre,usuario,etapa,directorio, dt)

    # PAGINA PRINCIPAL
    # Leer la estructura
    stri = rutinas.CrearPaginaPrincipal(proyecto,etapa,nombre,usuario, dt, dc, directorio, directoriogenesis)
    rutinas.ProcesoPersonalizacion(proyecto,appCore.nombre,'principal.html',directorio + nombre + '/core/templates/core/',stri,nombre,etapa,usuario)

    # BASE.HTML

    stri = rutinas.LeerArchivoEnTexto(dt + "base.html",etapa,nombre,usuario)
    stri = stri.replace('@html', rutinas.LeerArchivoEnTexto(dt + "base_html.html",etapa,nombre,usuario))
    stri = stri.replace('@css', '')
    stri = rutinas.CssBaseGeneral(proyecto,stri,directorio,nombre,directoriogenesis,etapa,usuario)
    stri = rutinas.ConstruyeBaseHtmlGeneral(proyecto,directorio,nombre,dt,dc,stri,directoriogenesis,etapa,usuario)
    # Grabar el archivo base.html
    rutinas.ProcesoPersonalizacion(proyecto,appCore.nombre,'base.html',directorio + nombre + "/core/templates/core/",stri,nombre,etapa,usuario)

    # Fabricar el base.html de acuerdo a Secciones, Filas y Columnas
    # if SeccionP.objects.filter(proyecto = proyecto).count() == 0:
    #     # Crear una base estandard para el proyecto
    #     rutinas.CrearBaseProyectoEstandar(proyecto, None)
    striP = rutinas.LeerArchivoEnTexto(dt + "baseProyecto.html",etapa,nombre,usuario)
    striP = rutinas.CssBaseGeneral(proyecto,striP,directorio,nombre,directoriogenesis,etapa,usuario)
    striP = rutinas.CrearBaseProyecto(proyecto, striP, dc,directorio,directoriogenesis,nombre,etapa,usuario)
    rutinas.ProcesoPersonalizacion(proyecto,appCore.nombre,'base' + proyecto.nombre + '.html',directorio + nombre + "/core/templates/core/",striP,nombre,etapa,usuario)

    # MENUS
    strMenu = rutinas.CrearMenus(proyecto,dt,etapa,nombre,usuario,directorio,directoriogenesis)
    rutinas.ProcesoPersonalizacion(proyecto,appCore.nombre,'menu_core.html',directorio + nombre + '/core/templates/core/includes/',strMenu,nombre,etapa,usuario)

    # HOME
    stri = rutinas.CrearHome(proyecto, dt, etapa, nombre, usuario)
    rutinas.ProcesoPersonalizacion(proyecto,appCore.nombre,'home.html',directorio + nombre + "/core/templates/core/",stri,nombre,etapa,usuario)

    # CSS
    stri = rutinas.CrearEstilosCss(proyecto, directorio,nombre,etapa,usuario, dt)
    rutinas.ProcesoPersonalizacion(proyecto,appCore.nombre,'estilos.css',directorio + nombre + "/core/static/core/css/",stri,nombre,etapa,usuario)

    # TEMPLATE DE MODELOS SINBASE
    strSinBasecss = rutinas.CrearModelosSinBase(proyecto,etapa,nombre,usuario,directorio,dt)
    rutinas.ProcesoPersonalizacion(proyecto,appCore.nombre,'modelo_sinbase.css',directorio + nombre + "/core/static/core/css/",strSinBasecss,nombre,etapa,usuario)

    # LISTA DE MODELO RAIZ
    strcssTotal = rutinas.CrearModelosList(proyecto,etapa,nombre,usuario,directorio,dt)
    # Escribir el archivo css del proyecto correspondiente al modelo list
    rutinas.ProcesoPersonalizacion(proyecto,appCore.nombre,'modelo_list.css',directorio + nombre + "/core/static/core/css/",strcssTotal,nombre,etapa,usuario)

    # CREAR EL TEMPLATE DE INSERCION POR MODELOS
    strcssTotal = rutinas.CrearModelosInsercion(proyecto, etapa,nombre,usuario, directorio, dt)
    # Escribe css total
    rutinas.ProcesoPersonalizacion(proyecto,appCore.nombre,'modelo_inserta.css',directorio + nombre + "/core/static/core/css/",strcssTotal,nombre,etapa,usuario)

    # TEMPLATE PARA EL UPDATE DE LOS MODELOS\
    strcsshijototal = rutinas.CrearModelosUpdate(proyecto,etapa,nombre,usuario,directorio,appCore,dt, directoriogenesis,dc)
    # Grabar los css de los hijos
    rutinas.ProcesoPersonalizacion(proyecto,appCore.nombre,'modelo_hijo.css',directorio + nombre + "/core/static/core/css/",strcsshijototal,nombre,etapa,usuario)

    # DELETE POR CADA MODELO
    strcssTotal = rutinas.CrearModelosDelete(proyecto,nombre,etapa,directorio,usuario,dt)
    # Grabar los css para el borrado
    rutinas.ProcesoPersonalizacion(proyecto,appCore.nombre,'modelo_borra.css',directorio + nombre + "/core/static/core/css/",strcssTotal,nombre,etapa,usuario)

    # CREAR EL TEMPLATE DE DASH POR MODELOS RAIZ
    strcssTotal = rutinas.CrearModelosDash(proyecto, etapa,nombre,usuario, directorio, dt)
    # CREAR EL TEMPLATE DE FILL POR MODELOS RAIZ
    strcssTotal = rutinas.CrearModelosFill(proyecto, etapa,nombre,usuario, directorio, dt)
    # Escribe css total
    rutinas.ProcesoPersonalizacion(proyecto,appCore.nombre,'modelo_inserta.css',directorio + nombre + "/core/static/core/css/",strcssTotal,nombre,etapa,usuario)

    # MODELOS FOREIGN
    rutinas.CrearModelosForeign(proyecto, etapa,nombre,usuario, directorio, dt)

    # BASE.HTML POR CADA MODELO
    rutinas.CrearBaseHtmlModelo(proyecto,directorio,etapa,nombre,usuario,directoriogenesis,dt,dc,appCore)
    
def CrearForms(proyecto,directorio,dt,usuario):

    # Borrar los errores de generacion
    ErroresCreacion.objects.filter(proyecto=proyecto.nombre).delete()

    nombre = proyecto.nombre
    etapa = "CrearForms"

    for aplicacion in Aplicacion.objects.filter(proyecto=proyecto):

        # Leer forms.py de text files
        # stri = TextFiles.objects.get(file = "forms.py").texto
        stri = rutinas.LeerArchivo(dt + "forms.py",etapa,nombre,usuario)

        # Para cada modelo
        strt = ''
        strim = ''
        strc = ''
        strform = ''
        strcm = ''

        for modelo in Modelo.objects.filter(aplicacion=aplicacion):

            if modelo.sinbasedatos == False:
                if Propiedad.objects.filter(modelo=modelo).count() > 0:
                    if strim.find('from ' + Aplicacion.objects.get(id=modelo.aplicacion.id).nombre + ".models import " + modelo.nombre) == -1:
                        strim += 'from ' + Aplicacion.objects.get(id=modelo.aplicacion.id).nombre + ".models import " + modelo.nombre + '\n'

                # recorrer propiedades
                strw = ''
                strl = ''
                strf = ''
                strget = ''
                # variable para modelos foreaneos
                for propiedad in Propiedad.objects.filter(modelo=modelo):
                    if propiedad.noestaenformulario == False:
                        if propiedad.tipo == 's':
                            strw += "\t\t\t'" + propiedad.nombre + "'" + ': forms.TextInput(attrs={' + "'" + 'class' + "'" + ':' + "'" + 'form-control font_control_@modelo mt-1' + "'" + ', ' + "'" + 'placeholder' + "'" + ': ' + "'" + '@textoplaceholder' + "'" + '}),' + '\n'
                        if propiedad.tipo == 'x':
                            strw += "\t\t\t'" + propiedad.nombre + "'" + ': forms.Textarea(attrs={' + "'" + 'class' + "'" + ':' + "'" + 'form-control  font_control_@modelo mt-1' + "'" + ', ' + "'" + 'placeholder' + "'" + ': ' + "'" + '@textoplaceholder' + "'" + '}),' + '\n'
                        if propiedad.tipo == 'm':
                            strw += "\t\t\t'" + propiedad.nombre + "'" + ': forms.TextInput(attrs={' + "'" + 'class' + "'" + ':' + "'" + 'form-control  font_control_@modelo mt-1' + "'" + ', ' + "'" + 'placeholder' + "'" + ': ' + "'" + '@textoplaceholder' + "'" + '}),' + '\n'
                        if propiedad.tipo == 'i':
                            strw += "\t\t\t'" + propiedad.nombre + "'" + ': forms.TextInput(attrs={' + "'" + 'class' + "'" + ':' + "'" + 'form-control  font_control_@modelo mt-1' + "'" + ', ' + "'" + 'placeholder' + "'" + ': ' + "'" + '@textoplaceholder' + "'" + '}),' + '\n'
                        if propiedad.tipo == 'l':
                            strw += "\t\t\t'" + propiedad.nombre + "'" + ': forms.TextInput(attrs={' + "'" + 'class' + "'" + ':' + "'" + 'form-control  font_control_@modelo mt-1' + "'" + ', ' + "'" + 'placeholder' + "'" + ': ' + "'" + '@textoplaceholder' + "'" + '}),' + '\n'
                        if propiedad.tipo == 'd':
                            strw += "\t\t\t'" + propiedad.nombre + "'" + ': forms.TextInput(attrs={' + "'" + 'class' + "'" + ':' + "'" + 'form-control  font_control_@modelo mt-1' + "'" + ', ' + "'" + 'placeholder' + "'" + ': ' + "'" + '@textoplaceholder' + "'" + '}),' + '\n'
                        if propiedad.tipo == 'f':
                            modelo_foraneo = Modelo.objects.get(nombre=propiedad.foranea , proyecto=proyecto)
                            if strim.find('from ' + Aplicacion.objects.get(id=modelo_foraneo.aplicacion.id).nombre + '.models import ' + modelo_foraneo.nombre) == -1:
                                strim += 'from ' + Aplicacion.objects.get(id=modelo_foraneo.aplicacion.id).nombre + '.models import ' + modelo_foraneo.nombre + '\n'
                            strw += "\t\t\t'" + propiedad.nombre + "'" + ': forms.Select(attrs={' + "'" + 'class' + "'" + ':' + "'" + 'form-control  font_control_@modelo mt-1' + "'" + '},choices=' + modelo_foraneo.nombre + '.objects.all()),' + '\n'
                        if propiedad.tipo == 'e':
                            strw += "\t\t\t'" + propiedad.nombre + "'" + ': forms.TimeInput(attrs={' + "'" + 'class' + "'" + ':' + "'" + 'form-control  font_control_@modelo mt-1' + "'" + '},format="%H:%M"),' + '\n'
                        if propiedad.tipo == 'n':
                            strw += "\t\t\t'" + propiedad.nombre + "'" + ': forms.DateInput(attrs={' + "'" + 'class' + "'" + ':' + "'" + 'datepicker form-control  font_control_@modelo mt-1' + "'" + '},format="%m/%d/%Y"),' + '\n'
                        if propiedad.tipo == 't':
                            strw += "\t\t\t'" + propiedad.nombre + "'" + ': forms.DateTimeInput(attrs={' + "'" + 'class' + "'" + ':' + "'" + 'form-control  font_control_@modelo mt-1' + "'" + '},format="%m/%d/%Y %H:%M"),' + '\n'
                        if propiedad.tipo == 'b':
                            strw += "\t\t\t'" + propiedad.nombre + "'" + ': forms.CheckboxInput(attrs={' + "'" + 'class' + "'" + ':' + "'" + 'font_control_@modelo mt-1' + "'" + ', ' + "'" + 'placeholder' + "'" + ': ' + "'" + '@textoplaceholder' + "'" + '}),' + '\n'
                        if propiedad.tipo == 'p':
                            strw += "\t\t\t'" + propiedad.nombre + "'" + ': forms.ClearableFileInput(attrs={' + "'" + 'class' + "'" + ':' + "'" + 'form-control-file  font_control_@modelo mt-1' + "'" + '}),' + '\n'
                        if propiedad.tipo == 'r':
                            lista_botones = propiedad.textobotones.split(';')
                            strlb = ''
                            for texto in lista_botones:
                                lista_partes = texto.split(',')
                                strlb += '(' + "'" + lista_partes[0] + "'," + "'" + lista_partes[1] + "')" + ',' + '\n'
                            strc += propiedad.nombre + '_choices = (' + strlb + ')' + '\n'
                            strw += "\t\t\t'" + propiedad.nombre + "'" + ': forms.RadioSelect(attrs={' + "'" + 'class' + "'" + ':' + "'" + 'mt-2' + "'" + '},choices=' + propiedad.nombre + '_choices),' + '\n'
                        if propiedad.tipo == 'a':
                            lista_botones = propiedad.textobotones.split(';')
                            strlb = ''
                            for texto in lista_botones:
                                lista_partes = texto.split(',')
                                strlb += '(' + "'" + lista_partes[0] + "'," + "'" + lista_partes[1] + "')" + ',' + '\n'
                            strc += propiedad.nombre + '_choices = (' + strlb + ')' + '\n'
                            strw += "\t\t\t'" + propiedad.nombre + "'" + ': forms.Select(attrs={' + "'" + 'class' + "'" + ':' + "'" + 'form-control  font_control_@modelo mt-1' + "'" + '},choices=' + propiedad.nombre + '_choices),' + '\n'
                        if propiedad.tipo == 'h':
                            strw += "\t\t\t'" + propiedad.nombre + "'" + ': forms.Textarea(attrs={' + "'" + 'class' + "'" + ':' + "'" + 'form-control  font_control_@modelo mt-1' + "'" + ', ' + "'" + 'placeholder' + "'" + ': ' + "'" + '@textoplaceholder' + "'" + '}),' + '\n'

                        strw = strw.replace('@etiqueta', propiedad.nombre)
                        strw = strw.replace('@textoplaceholder', propiedad.textoplaceholder)
                        strw = strw.replace('@modelo', modelo.nombre)

                        if propiedad.tipo != 'u':
                            strf += "'" + propiedad.nombre + "'" + ','
                            strl += "'" + propiedad.nombre + "':" + "'" + propiedad.etiqueta + "'" + ','

                        # reglas
                        strcm = ''
                        for regla in Regla.objects.filter(propiedad=propiedad):
                            cc = ''
                            for lc in regla.codigo.split('\n'):
                                cc += '\t\t' + lc + '\n'
                            strcm += cc
                            strcm += '\t\t    raise forms.ValidationError(' + "'" + regla.mensaje + "'" + ')' + '\n'

                        if strcm != '':
                            strget = '\t\t' + propiedad.nombre + ' = self.cleaned_data[' + "'" + propiedad.nombre + "'" + ']' + '\n'
                            strget += strcm


                streg = ''
                if strget != '':
                    streg += '\tdef clean(self):' + '\n'
                    streg += strget


                if strw != '':
                    print('modelo form ',modelo)
                    strt = 'class @modeloForm(forms.ModelForm):' + '\n'
                    strt += '#@[p_Meta_@modelo_01]' + '\n'
                    strt += '\tclass Meta:' + '\n'
                    strt += '#@[p_Meta_@modelo_02]' + '\n'
                    strt += '\t\tmodel = @modelo' + '\n'
                    strt += '#@[p_Meta_@modelo_03]' + '\n'
                    strt += '#@[p_fields_@modelo_01]' + '\n'
                    strt += '\t\tfields = (@listafields)' + '\n'
                    strt += '#@[p_fields_@modelo_02]' + '\n'
                    strt += '#@[p_widgets_@modelo_01]' + '\n'
                    strt += '\t\twidgets = {' + '\n'
                    strt += '#@[p_listawidgets_@modelo_01]' + '\n'
                    strt += '@listawidgets' + '\n'
                    strt += '#@[p_listawidgets_@modelo_02]' + '\n'
                    strt += '\t\t}' + '\n'
                    strt += '#@[p_widgets_@modelo_02]' + '\n'
                    strt += '#@[p_labels_@modelo_01]' + '\n'
                    strt += '\t\tlabels = {' + '\n'
                    strt += '#@[p_listalabels_@modelo_01]' + '\n'
                    strt += '\t\t@listalabels' + '\n'
                    strt += '#@[p_listalabels_@modelo_02]' + '\n'
                    strt += '\t\t}' + '\n'
                    strt += '#@[p_labels_@modelo_02]' + '\n'
                    strt += '#@[p_reglas_@modelo_01]' + '\n'
                    strt += '@reglas' + '\n'
                    strt += '#@[p_reglas_@modelo_02]' + '\n'

                    strt = strt.replace('@listafields', strf)
                    strt = strt.replace('@listalabels', strl)
                    strt = strt.replace('@listawidgets', strw)
                    strt = strt.replace('@reglas', streg)
                    strt = strt.replace('@modelo', modelo.nombre)

                    strform += strt + '\n'

                    strf = ''
                    strl = ''
                    strw = ''    

            else:

                strg = ''
                strp = ''
                strt += '#@[p__@modeloForm_01]' + '\n'
                strt += 'class @modeloForm(forms.Form):' + '\n'
                strt += '#@[p__@modeloForm_02]' + '\n'
                strt += '@fields' + '\n'
                strt += '#@[p__@modeloForm_03]' + '\n'
                strt += '@widgets' + '\n'
                strt += '#@[p__@modeloForm_04]' + '\n'
                strt += '\tdef clean(self):' + '\n'
                strt += '#@[p__@modeloForm_05]' + '\n'
                strt += '\t\tcleaned_data = super(@modeloForm, self).clean()' + '\n'
                strt += '#@[p__@modeloForm_06]' + '\n'

                for propiedad in Propiedad.objects.filter(modelo=modelo):
                    if propiedad.noestaenformulario == False:
                        a,b,c = FormPropiedad(propiedad)
                        strp += a
                        strg += b
                        strc += c

                strt = strt.replace('@fields',strp)
                strt = strt.replace('@widgets',strg)
                strt = strt.replace('@modelo',modelo.nombre)
                strform += strt + '\n'
                strp = ''
                strg = ''

            # formulario dash
            strp = ''
            strg = ''
            if modelo.padre == 'nada':
                if rutinas.TieneDash(modelo):
                    strp += '#@[p__@DashmodeloForm_01]' + '\n'
                    strp += 'class Dash@modeloForm(forms.Form):' + '\n'
                    strp += '#@[p__@DashmodeloForm_02]' + '\n'
                    strp += '@fields' + '\n'
                    strp += '#@[p__@DashmodeloForm_03]' + '\n'
                    strp += '@widgets' + '\n'
                    strp += '#@[p__@DashmodeloForm_04]' + '\n'
                    sa = ''
                    sb = ''
                    sc=''
                    ra=[]
                    rb=[]
                    rc=[]
                    RecursivoFormPropiedad(modelo,proyecto,ra,rb,rc)
                    for r in ra:
                        sa += r
                    for r in rb:
                        sb += r
                    strp = strp.replace('@fields',sa)
                    strp = strp.replace('@widgets',sb)
                    strp = strp.replace('@modelo',modelo.nombre)
                    strform += strp + '\n'
                    strp = ''

                # Formulario fill
                strg += '#@[p__@FillmodeloForm_01]' + '\n'
                strg += 'class Fill@modeloForm(forms.Form):' + '\n'
                strg += '#@[p__@FillmodeloForm_02]' + '\n'
                strg += '\tdestruye =  forms.CharField(max_length=30)' + '\n'
                strg += '#@[p__@FillmodeloForm_03]' + '\n'
                strg = strg.replace('@modelo',modelo.nombre)
                strform += strg + '\n'
                strg = ''
                
        stri = stri.replace('@listachoices', strc)
        if strim != '':
            strim = '#@[p_import_modelos_01]' + '\n' + strim + '\n'
            strim += '#@[p_import_modelos_02]' + '\n'

        stri = stri.replace('@importmodelos', strim)
        stri = stri.replace('@forms', strform)

        # Grabar el modelo si su aplicacion tiene modelos con propiedades
        if rutinas.AplicacionTienePropiedades(aplicacion):
            rutinas.ProcesoPersonalizacion(proyecto,aplicacion.nombre,'forms.py',directorio + nombre + "/" + aplicacion.nombre + "/",stri,nombre,etapa,usuario)

def RecursivoFormPropiedad(modelo,proyecto,ra,rb,rc):
    for propiedad in Propiedad.objects.filter(modelo=modelo):
        if propiedad.dashboard:
            a,b,c=FormPropiedad(propiedad)
            ra.append(a)
            rb.append(b)
            rc.append(c)
    for mod in Modelo.objects.filter(padre=modelo.nombre,proyecto=proyecto):
        RecursivoFormPropiedad(mod,proyecto,ra,rb,rc)

def FormPropiedad(propiedad):
    strp = ''
    strg = ''
    strc= ''
    if propiedad.tipo == 't' or propiedad.tipo == 'n':
        strg += '\t' + propiedad.nombre + '.widget.attrs.update({' + "'" + 'class' + "'" + ': ' + "'" + 'datepicker form-control' + "'" + '})' + '\n'
    elif propiedad.tipo == 'b' or propiedad.tipo == 'r':
        strg += ''
    else:
        strg += '\t' + propiedad.nombre + '.widget.attrs.update({' + "'" + 'class' + "'" + ': ' + "'" + 'form-control' + "'" + '})' + '\n'
    if propiedad.tipo == 's':
        strp += '\t' + propiedad.nombre + ' = ' + 'forms.CharField(max_length=' + str(propiedad.largostring) + ')' + '\n'
    if propiedad.tipo == 'x':
        strp += '\t' + propiedad.nombre + ' = ' + 'forms.TextField('')' + '\n'
    if propiedad.tipo == 'm':
        strp += '\t' + propiedad.nombre + ' =  forms.IntegerField('')' + '\n'
    if propiedad.tipo == 'i':
        strp += '\t' + propiedad.nombre + ' =  forms.IntegerField('')' + '\n'
    if propiedad.tipo == 'l':
        strp += '\t' + propiedad.nombre + ' =  forms.IntegerField('')' + '\n'
    if propiedad.tipo == 'd':
        strp += '\t' + propiedad.nombre + ' =  forms.DecimalField(' + 'decimal_places=2,max_digits=10)' + '\n'
    if propiedad.tipo == 't':
        strp += '\t' + propiedad.nombre + ' =  forms.DateTimeField('')' + '\n'
    if propiedad.tipo == 'e': #TimeField
        strp += '\t' + propiedad.nombre + ' = ' + 'forms.TimeField('')' + '\n'
    if propiedad.tipo == 'n': #DateField
        strp += '\t' + propiedad.nombre + ' = ' + 'forms.DateField('')' + '\n'
    if propiedad.tipo == 'b':
        strp += '\t' + propiedad.nombre + ' =  forms.BooleanField('')' + '\n'
    if propiedad.tipo == 'f':
        modelo_foraneo = Modelo.objects.get(nombre=propiedad.foranea , proyecto=propiedad.modelo.proyecto)
        strp += '\t' + propiedad.nombre + ' = forms.ModelChoiceField(queryset=' + modelo_foraneo.nombre + '.objects.all())' + '\n'

    if propiedad.tipo == 'r':
        strlb = ''
        lista_botones = propiedad.textobotones.split(';')
        for texto in lista_botones:
            lista_partes = texto.split(',')
            strlb += '(' + "'" + lista_partes[0] + "'," + "'" + lista_partes[1] + "')" + ',' + '\n'
        strc += '\t' + propiedad.nombre + '_choices = (' + strlb + ')' + '\n'
        strp += '\t' + propiedad.nombre + ' = ' +  'forms.ChoiceField(choices=' + propiedad.nombre + '_choices' + ', widget=forms.RadioSelect)' + '\n'
    if propiedad.tipo == 'a':
        strlb = ''
        lista_botones = propiedad.textobotones.split(';')
        for texto in lista_botones:
            lista_partes = texto.split(',')
            strlb += '(' + "'" + lista_partes[0] + "'," + "'" + lista_partes[1] + "')" + ',' + '\n'
        strc += '\t' + propiedad.nombre + '_choices = (' + strlb + ')' + '\n'
        strp += '\t' + propiedad.nombre + ' = ' +  'forms.ChoiceField(choices=' + propiedad.nombre + '_choices' + ', widget=forms.Select)' + '\n'
    if propiedad.tipo == 'h':
        strp += '\t' + propiedad.nombre + ' = ' + 'Textarea()' + '\n'
    if propiedad.tipo == 'p':
        strp += '\t' + propiedad.nombre + ' = models.ClearableFileInput()' + '\n'

    return strp,strg,strc


# def CrearDirectorio(nombreDirectorio, etapa, nombreProyecto, usuario,borraPrevio):

#     if borraPrevio:
#         try:
#             shutil.rmtree(nombreDirectorio)
#         except:
#             pass

#     try:
#         os.mkdir(nombreDirectorio)
#     except Exception as e:
#         errores = ErroresCreacion()
#         errores.etapa = etapa
#         errores.paso = "Crear el directorio: " + nombreDirectorio
#         errores.proyecto = nombreProyecto
#         errores.usuario = usuario
#         errores.descripcion = e
#         errores.severo = True
#         errores.save()

def CrearSeguridad(proyecto,directorio,dt,usuario):

    # Borrar los errores de generacion
    ErroresCreacion.objects.filter(proyecto=proyecto.nombre).delete()
    # ErroresCreacion.objects.all().delete()

    nombre = proyecto.nombre
    etapa = "CrearSeguridad"

    # Aplicacion registration
    strApp = Aplicacion.objects.get(proyecto=proyecto,nombre='registration')
    # views.py seguridad
    if proyecto.conseguridad:
        # Copia el archivo views.py de text files en registratio
        # stri = TextFiles.objects.get(file = "/registration/views.py").texto
        stri = rutinas.LeerArchivo(dt + "/registration/views.py",etapa,nombre,usuario)
        rutinas.ProcesoPersonalizacion(proyecto,strApp.nombre,'views.py',directorio + nombre + "/registration/",stri,nombre,etapa,usuario)
        # rutinas.CopiarArchivos(dt + "/registration/views.py",directorio + nombre + "/registration" + "/views.py",etapa,nombre,True)        

    # models.py seguridad
    if proyecto.conseguridad:
        # stri = TextFiles.objects.get(file = "/registration/models.py").texto
        stri = rutinas.LeerArchivo(dt + "/registration/models.py",etapa,nombre,usuario)
        rutinas.ProcesoPersonalizacion(proyecto,strApp.nombre,'models.py',directorio + nombre + "/registration/",stri,nombre,etapa,usuario)
        # rutinas.CopiarArchivos(dt + "/registration/models.py",directorio + nombre + "/registration" + "/models.py",etapa,nombre,True)        

    # urls.py seguridad
    if proyecto.conseguridad:
        # stri = TextFiles.objects.get(file = "/registration/urls.py").texto
        stri = rutinas.LeerArchivo(dt + "/registration/urls.py",etapa,nombre,usuario)
        rutinas.ProcesoPersonalizacion(proyecto,strApp.nombre,'urls.py',directorio + nombre + "/registration/",stri,nombre,etapa,usuario)
        # rutinas.CopiarArchivos(dt + "/registration/urls.py",directorio + nombre + "/registration" + "/urls.py",etapa,nombre,True)        

    # forms.py seguridad
    if proyecto.conseguridad:
        # stri = TextFiles.objects.get(file = "/registration/forms.py").texto
        stri = rutinas.LeerArchivo(dt + "/registration/forms.py",etapa,nombre,usuario)
        rutinas.ProcesoPersonalizacion(proyecto,strApp.nombre,'forms.py',directorio + nombre + "/registration/",stri,nombre,etapa,usuario)
        # rutinas.CopiarArchivos(dt + "/registration/forms.py",directorio + nombre + "/registration" + "/forms.py",etapa,nombre,True)        

    # urls.py seguridad
    if proyecto.conseguridad:
        strlfp = 'from registration.urls import registration_patterns' + '\n'
        strlfp += 'from seguridad.urls import seguridad_patterns' + '\n'
        strlpp = '\tpath(' + "'" + 'accounts/' + "'" + ', include(' + "'" + 'django.contrib.auth.urls' + "'" + ')),' + '\n'
        strlpp += '\tpath(' + "'" + 'accounts/' + "'" + ', include(registration_patterns)),' + '\n'
        strlpp += '\tpath(' + "'" + 'seguridad/' + "'" + ', include(seguridad_patterns)),' + '\n'

        stri = rutinas.LeerArchivo(directorio + nombre + "/" + nombre + "/urls.py",etapa,nombre,usuario)
        stri = stri.replace('#@patternsseguridad', strlfp)
        stri = stri.replace('#@pathseguridad', strlpp)

        rutinas.EscribirArchivo(directorio + nombre + "/" + nombre + "/urls.py",etapa,nombre,stri,usuario,True)

    # seguridad templates
    if proyecto.conseguridad:

        CreaSeguridadHtml('login.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'registration/templates/registration')
        CreaSeguridadHtml('password_change_done.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'registration/templates/registration')
        CreaSeguridadHtml('password_change_form.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'registration/templates/registration')
        CreaSeguridadHtml('password_reset_complete.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'registration/templates/registration')
        CreaSeguridadHtml('password_reset_confirm.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'registration/templates/registration')
        CreaSeguridadHtml('password_reset_done.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'registration/templates/registration')
        CreaSeguridadHtml('password_reset_form.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'registration/templates/registration')
        CreaSeguridadHtml('profile_form.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'registration/templates/registration')
        CreaSeguridadHtml('profile_email_form.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'registration/templates/registration')
        CreaSeguridadHtml('registro.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'registration/templates/registration')

    # Aplicacion seguridad
    strApp = Aplicacion.objects.get(proyecto=proyecto,nombre='seguridad')
    # views_rol.py roles
    if proyecto.conseguridad:
        # Copia el archivo views_rol.py de text files en registratio
        # stri = TextFiles.objects.get(file = "/registration/views_rol.py").texto
        stri = rutinas.LeerArchivo(dt + "/registration/views_rol.py",etapa,nombre,usuario)
        rutinas.ProcesoPersonalizacion(proyecto,strApp.nombre,'views.py',directorio + nombre + "/seguridad/",stri,nombre,etapa,usuario)
        # rutinas.CopiarArchivos(dt + "/registration/views.py",directorio + nombre + "/registration" + "/views.py",etapa,nombre,True)        

    # # models_rol.py seguridad
    # if proyecto.conseguridad:
    #     # stri = TextFiles.objects.get(file = "/registration/models.py").texto
    #     stri = rutinas.LeerArchivo(dt + "/registration/models_rol.py",etapa,nombre,usuario)
    #     rutinas.ProcesoPersonalizacion(proyecto,strApp.nombre,'models.py',directorio + nombre + "/seguridad/",stri,nombre,etapa,usuario)
    #     # rutinas.CopiarArchivos(dt + "/registration/models.py",directorio + nombre + "/registration" + "/models.py",etapa,nombre,True)        

    # urls_rol.py seguridad
    if proyecto.conseguridad:
        # stri = TextFiles.objects.get(file = "/registration/urls.py").texto
        stri = rutinas.LeerArchivo(dt + "/registration/urls_rol.py",etapa,nombre,usuario)
        rutinas.ProcesoPersonalizacion(proyecto,strApp.nombre,'urls.py',directorio + nombre + "/seguridad/",stri,nombre,etapa,usuario)
        # rutinas.CopiarArchivos(dt + "/registration/urls.py",directorio + nombre + "/registration" + "/urls.py",etapa,nombre,True)        

    # forms_rol.py seguridad
    if proyecto.conseguridad:
        # stri = TextFiles.objects.get(file = "/registration/forms.py").texto
        stri = rutinas.LeerArchivo(dt + "/registration/forms_rol.py",etapa,nombre,usuario)
        rutinas.ProcesoPersonalizacion(proyecto,strApp.nombre,'forms.py',directorio + nombre + "/seguridad/",stri,nombre,etapa,usuario)
        # rutinas.CopiarArchivos(dt + "/registration/forms.py",directorio + nombre + "/registration" + "/forms.py",etapa,nombre,True)        

    # seguridad roles templates
    if proyecto.conseguridad:

        CreaSeguridadHtml('modelo_rol_confirm_delete.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'seguridad/templates/seguridad')
        CreaSeguridadHtml('modelo_rol_form.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'seguridad/templates/seguridad')
        CreaSeguridadHtml('modelo_rol_update_form.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'seguridad/templates/seguridad')
        CreaSeguridadHtml('propiedad_rol_confirm_delete.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'seguridad/templates/seguridad')
        CreaSeguridadHtml('propiedad_rol_form.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'seguridad/templates/seguridad')
        CreaSeguridadHtml('propiedad_rol_update_form.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'seguridad/templates/seguridad')
        CreaSeguridadHtml('rol_confirm_delete.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'seguridad/templates/seguridad')
        CreaSeguridadHtml('rol_form.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'seguridad/templates/seguridad')
        CreaSeguridadHtml('rol_list.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'seguridad/templates/seguridad')
        CreaSeguridadHtml('rol_update_form.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'seguridad/templates/seguridad')
        CreaSeguridadHtml('rolusuario_confirm_delete.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'seguridad/templates/seguridad')
        CreaSeguridadHtml('rolusuario_form.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'seguridad/templates/seguridad')
        CreaSeguridadHtml('rolusuario_update_form.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'seguridad/templates/seguridad')
        CreaSeguridadHtml('usuariorol_confirm_delete.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'seguridad/templates/seguridad')
        CreaSeguridadHtml('usuariorol_form.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'seguridad/templates/seguridad')
        CreaSeguridadHtml('usuariorol_list.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'seguridad/templates/seguridad')
        CreaSeguridadHtml('usuariorol_update_form.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'seguridad/templates/seguridad')

    # Formularios incluidos
    if proyecto.conseguridad:
        CreaSeguridadHtml('formulario_modelo_rol.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'core/templates/core/includes')
        CreaSeguridadHtml('formulario_propiedad_rol.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'core/templates/core/includes')
        CreaSeguridadHtml('formulario_rol.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'core/templates/core/includes')
        CreaSeguridadHtml('formulario_usuariorol.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'core/templates/core/includes')
        CreaSeguridadHtml('formulario_rolusuario.html',etapa,nombre,directorio,dt,strApp,proyecto,usuario,'core/templates/core/includes')

def CreaSeguridadHtml(nombre_archivo,etapa,nombre,directorio,dt,aplicacion,proyecto,usuario,donde):
    # Copia el archivo de text files registration en la aplicacion registratio
    # stri = TextFiles.objects.get(file = "/registration/" + nombre_archivo).texto
    stri = rutinas.LeerArchivo(dt + "/registration/" + nombre_archivo,etapa,nombre,usuario)
    stri = stri.replace('@proyecto',proyecto.nombre)
    rutinas.ProcesoPersonalizacion(proyecto,aplicacion.nombre,nombre_archivo,directorio + nombre + "/" + donde + "/",stri,nombre,etapa,usuario)
    # rutinas.CopiarArchivos(dt + "/registration/" + nombre_archivo,directorio + nombre + "/registration" + "/templates/registration/" + nombre_archivo,etapa,nombre,True)

def BorrarArchivo(archivo,etapa,nombreProyecto,usuario):

    try:
        os.remove(archivo)
    except Exception as e:
        errores = ErroresCreacion()
        errores.etapa = etapa
        errores.paso = "Borrar el archivo: " + archivo
        errores.proyecto = nombreProyecto
        errores.usuario = usuario
        errores.descripcion = e
        errores.severo = True
        errores.save()

# def EscribirEnArchivo(archivo,texto,etapa,nombreProyecto,usuario):

#     try:
#         with open(archivo, 'w') as file_object:
#             file_object.write(texto)
#     except Exception as e:
#         errores = ErroresCreacion()
#         errores.etapa = etapa
#         errores.paso = "No se escribio en el archivo: " + archivo
#         errores.proyecto = nombreProyecto
#         errores.usuario = usuario
#         errores.descripcion = e
#         errores.severo = True
#         errores.save()

# reemplaza en los tag del archivo el codigo de la personalizacion
def EscribePersonalizacion(proyecto, nombre_aplicacion, archivo, texto):
    strLineaNueva = ''
    # Leer todas las personalizaciones
    # Ver si cada una de ellas esta en el texto
    # Si esta entonces leer el texto con Returns hasta encontrar el tag de personalizacion
    # Reemplazar en la linea los [] por ()
    # Incorporar la linea en el texto
    # Incorporar el codigo de personalizacion de la base en el texto
    # Incorporar en el texto #@()

    lista_perso = Personaliza.objects.filter(usuario=proyecto.usuario, 
                                        proyecto=proyecto, 
                                        aplicacion=nombre_aplicacion, 
                                        archivo=archivo)
    
    for perso in lista_perso:
        if perso.tag in texto:
            lineas = texto.split('\n')
            for linea in lineas:
                if perso.tag in linea:
                    if '<!-- ' in linea:
                        # archivo html
                        strLineaNueva += '<!-- #@(' + perso.tag + ') -->' + '\n'
                    elif '/*' in linea:
                        # archivo css
                        strLineaNueva += '/* #@(' + perso.tag + ') */' + '\n'
                    else:
                        strLineaNueva += '#@(' + perso.tag + ')' + '\n'                        
                    strcodi=perso.codigo.split('\n')
                    for strCod in strcodi:
                        strLineaNueva += strCod + '\n'
                    if '<!-- ' in linea:
                        # archivo html
                        strLineaNueva += '<!-- #@() -->' + '\n'
                    elif '/*' in linea:
                        # archivo css
                        strLineaNueva += '/* #@() */' + '\n'
                    else:
                        strLineaNueva += '#@()' + '\n'
                else:
                    strLineaNueva += linea +'\n'
            texto = strLineaNueva
            strLineaNueva = ''
    return texto

def AplicacionReal(modelo,texto,proyecto):
    # Encuentra la aplicacion real
    msp = Modelo.objects.get(nombre=modelo.padre, proyecto=proyecto)
    while msp.padre != 'nada':
        msp = Modelo.objects.get(nombre=msp.padre,proyecto=proyecto)
    texto = texto.replace('@aplicacionreal', Aplicacion.objects.get(id=msp.aplicacion.id).nombre)
    return texto

def ModeloConPropiedadUsuario(modelo):
    for prop in Propiedad.objects.filter(modelo=modelo):
        if prop.tipo == 'u':
            return prop
    return None

class ConfigurarModeloView(TemplateView):
    # template_name = "crear/configurar_base.html"
    template_name = "crear/configurar_modelo_nueva.html"

    def get_context_data(self,**kwargs):
        context = super(ConfigurarModeloView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)

        # Ver si esta en configuracion
        try:
            context['configuracion'] = self.request.GET['configuracion_proyecto']
        except:
            context['configuracion'] = 'false'

        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            modelo = Modelo.objects.get(id=self.request.GET['modelo_id'])
            context['altoencabezado'] = str(proyecto.altofilaenizcede) + 'px'
            context['altobume'] = str(proyecto.altofilabume) + 'px'
            context['altomedio'] = str(200) + 'px'
            context['altopie'] = str(proyecto.altofilapie) + 'px'
            context['anchoencabezadoizquierda'] = proyecto.numerocolumnaenizquierda 
            context['anchologo'] = proyecto.numerocolumnalogo
            context['anchotitulo'] = proyecto.numerocolumnatitulo
            context['anchologin'] = proyecto.numerocolumnalogin
            context['anchoencabezadoderecha'] = proyecto.numerocolumnaenderecha
            context['anchobumeizquierda'] = proyecto.numerocolumnabumeizquierda
            context['anchobusqueda'] = proyecto.numerocolumnabusqueda
            context['anchomenu'] = proyecto.numerocolumnamenu
            context['anchobumederecha'] = proyecto.numerocolumnabumederecha
            context['anchomedioizquierda'] = proyecto.numerocolumnamedioizquierda
            context['anchomedicocentro'] = proyecto.numerocolumnamediocentro
            context['anchomedioderecha'] = proyecto.numerocolumnamedioderecha
            context['numerocolumnaenizquierda'] = proyecto.numerocolumnaenizquierda
            context['numerocolumnalogo'] = proyecto.numerocolumnalogo
            context['numerocolumnatitulo'] = proyecto.numerocolumnatitulo
            context['numerocolumnalogin'] = proyecto.numerocolumnalogin
            context['numerocolumnaenderecha'] = proyecto.numerocolumnaenderecha
            context['numerocolumnabumeizquierda'] = proyecto.numerocolumnabumeizquierda
            context['numerocolumnabusqueda'] = proyecto.numerocolumnabusqueda
            context['numerocolumnamenu'] = proyecto.numerocolumnamenu
            context['numerocolumnabumederecha'] = proyecto.numerocolumnabumederecha
            context['numerocolumnamedioizquierda'] = proyecto.numerocolumnamedioizquierda
            context['numerocolumnamediocentro'] = proyecto.numerocolumnamediocentro
            context['numerocolumnamedioderecha'] = proyecto.numerocolumnamedioderecha

            context['columnasizquierdainserta'] = modelo.numerocolumnasizquierdainserta
            context['columnasderechainserta'] = modelo.numerocolumnasderechainserta
            context['columnasmodeloinserta'] = modelo.numerocolumnasmodeloinserta

            # Alto y ancho de secciones

            try:
                flecha = self.request.GET['flecha']
                if flecha == "mi": #ancho izquierda medio
                    direccion = self.request.GET['direccion']
                    if direccion == 'menos':
                        if modelo.numerocolumnasizquierdainserta > 0:
                            modelo.numerocolumnasizquierdainserta =  modelo.numerocolumnasizquierdainserta - 1
                            context['columnasizquierdainserta'] =  modelo.numerocolumnasizquierdainserta
                            modelo.save()
                            # context['numerocolumnalogo'] = proyecto.numerocolumnalogo + 1
                    else:
                        if modelo.numerocolumnasizquierdainserta + modelo.numerocolumnasmodeloinserta + modelo.numerocolumnasderechainserta < 12:
                            modelo.numerocolumnasizquierdainserta =  modelo.numerocolumnasizquierdainserta + 1
                            context['columnasizquierdainserta'] =  modelo.numerocolumnasizquierdainserta 
                            modelo.save()
                if flecha == "mc": #ancho medio
                    direccion = self.request.GET['direccion']
                    if direccion == 'menos':
                        if modelo.numerocolumnasmodeloinserta > 0:
                            modelo.numerocolumnasmodeloinserta =  modelo.numerocolumnasmodeloinserta - 1
                            context['columnasmodeloinserta'] =  modelo.numerocolumnasmodeloinserta
                            modelo.save()
                            # context['numerocolumnalogo'] = proyecto.numerocolumnalogo + 1
                    else:
                        if modelo.numerocolumnasizquierdainserta + modelo.numerocolumnasmodeloinserta + modelo.numerocolumnasderechainserta < 12:
                            modelo.numerocolumnasmodeloinserta =  modelo.numerocolumnasmodeloinserta + 1
                            context['columnasmodeloinserta'] =  modelo.numerocolumnasmodeloinserta
                            modelo.save()
                if flecha == "md": #ancho medio
                    direccion = self.request.GET['direccion']
                    if direccion == 'menos':
                        if modelo.numerocolumnasderechainserta > 0:
                            modelo.numerocolumnasderechainserta =  modelo.numerocolumnasderechainserta - 1
                            context['columnasderechainserta'] =  modelo.numerocolumnasderechainserta
                            modelo.save()
                            # context['numerocolumnalogo'] = proyecto.numerocolumnalogo + 1
                    else:
                        if modelo.numerocolumnasizquierdainserta + modelo.numerocolumnasmodeloinserta + modelo.numerocolumnasderechainserta < 12:
                            modelo.numerocolumnasderechainserta =  modelo.numerocolumnasderechainserta + 1
                            context['columnasderechainserta'] =  modelo.numerocolumnasderechainserta
                            modelo.save()
            except:
                pass
            
            context['proyecto'] = proyecto
            context['modelo'] = modelo
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'        
        return context

class PanelAjustableModeloView(TemplateView):
    template_name = "crear/panel_ajustable_modelo.html"

    def get_context_data(self,**kwargs):
        context = super(PanelAjustableModeloView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)

        # Ver si esta en configuracion
        try:
            context['configuracion'] = self.request.GET['configuracion_proyecto']
        except:
            context['configuracion'] = 'false'

        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            modelo = Modelo.objects.get(id=self.request.GET['modelo_id'])

            context['proyecto'] = proyecto
            context['modelo'] = modelo
            try:
                name = self.request.GET['name']
                crece = self.request.GET['crece']

                if name == 'mipc':
                    if crece == 'derecha':
                        if not DoceColumnasInserta(modelo):
                            modelo.numerocolumnasizquierdainserta +=1
                        elif modelo.numerocolumnasmodeloinserta > 1:
                            modelo.numerocolumnasizquierdainserta += 1
                            modelo.numerocolumnasmodeloinserta -= 1
                if name == 'misc':
                    if crece == 'derecha':
                        if not DoceColumnasInserta(modelo):
                            modelo.numerocolumnasmodeloinserta += 1
                        elif modelo.numerocolumnasderechainserta > 1:
                            modelo.numerocolumnasmodeloinserta += 1
                            modelo.numerocolumnasderechainserta -= 1
                    if crece == 'izquierda':
                        if modelo.numerocolumnasizquierdainserta > 1:
                            # modelo.numerocolumnasmodeloinserta += 1
                            modelo.numerocolumnasizquierdainserta -= 1
                if name == 'mitc':
                    if crece == 'izquierda':
                        if modelo.numerocolumnasmodeloinserta > 1:
                            # modelo.numerocolumnasderechainserta += 1
                            modelo.numerocolumnasmodeloinserta -= 1
                    if crece == 'derecha':
                        if not DoceColumnasInserta(modelo):
                            modelo.numerocolumnasderechainserta += 1
                if name == 'mupc':
                    if crece == 'derecha':
                        if not DoceColumnasUpdate(modelo,modelo.hijoscontiguos):
                            modelo.numerocolumnasizquierdaupdate += 1
                        if modelo.numerocolumnasmodeloupdate > 1:
                            modelo.numerocolumnasizquierdaupdate += 1
                            modelo.numerocolumnasmodeloupdate -= 1
                if name == 'musc':
                    if crece == 'derecha':
                        if not DoceColumnasUpdate(modelo, modelo.hijoscontiguos):
                            modelo.numerocolumnasmodeloupdate += 1
                        elif modelo.numerocolumnasderechaupdate > 1:
                            modelo.numerocolumnasmodeloupdate += 1
                            modelo.numerocolumnasderechaupdate -= 1
                    if crece == 'izquierda':
                        if modelo.numerocolumnasizquierdaupdate > 1:
                            # modelo.numerocolumnasmodeloupdate += 1
                            modelo.numerocolumnasizquierdaupdate -= 1
                if name == 'mutc':
                    if crece == 'izquierda':
                        if modelo.numerocolumnasmodeloupdate > 1:
                            # modelo.numerocolumnasderechaupdate += 1
                            modelo.numerocolumnasmodeloupdate -= 1
                    if crece == 'derecha':
                        if not DoceColumnasUpdate(modelo, modelo.hijoscontiguos):
                            modelo.numerocolumnasderechaupdate +=1
                        elif modelo.hijoscontiguos > 1:
                                modelo.numerocolumnashijosupdate -= 1
                                modelo.numerocolumnasderechaupdate += 1
                if name == 'mucc':
                    if crece == 'izquierda':
                        if modelo.numerocolumnasderechaupdate > 1:
                            # modelo.numerocolumnashijosupdate += 1
                            modelo.numerocolumnasderechaupdate -= 1
                    if crece == 'derecha':
                        if not DoceColumnasUpdate(modelo, modelo.hijoscontiguos):
                            modelo.numerocolumnashijosupdate +=1
                if name == 'mdpc':
                    if crece == 'derecha':
                        if not DoceColumnasBorra(modelo):
                            modelo.numerocolumnasizquierdaborra +=1
                        elif modelo.numerocolumnasmodeloborra > 1:
                            modelo.numerocolumnasizquierdaborra += 1
                            modelo.numerocolumnasmodeloborra -= 1
                if name == 'mdsc':
                    if crece == 'derecha':
                        if not DoceColumnasBorra(modelo):
                            modelo.numerocolumnasmodeloborra += 1
                        elif modelo.numerocolumnasderechaborra > 1:
                            modelo.numerocolumnasmodeloborra += 1
                            modelo.numerocolumnasderechaborra -= 1
                    if crece == 'izquierda':
                        if modelo.numerocolumnasizquierdaborra > 1:
                            # modelo.numerocolumnasmodeloinserta += 1
                            modelo.numerocolumnasizquierdaborra -= 1
                if name == 'mdtc':
                    if crece == 'izquierda':
                        if modelo.numerocolumnasmodeloborra > 1:
                            # modelo.numerocolumnasderechainserta += 1
                            modelo.numerocolumnasmodeloborra -= 1
                    if crece == 'derecha':

                        if not DoceColumnasBorra(modelo):
                            modelo.numerocolumnasderechaborra += 1
                modelo.save()
                # if seccion == 'izquierdainserta':
                #     modelo.numerocolumnasizquierdainserta = int(self.request.GET['valor'])
                #     context['izquierdainserta'] = modelo.numerocolumnasizquierdainserta
                #     modelo.save()
                # if seccion == 'modeloinserta':
                #     modelo.numerocolumnasmodeloinserta = int(self.request.GET['valor'])
                #     context['modeloinserta'] = modelo.numerocolumnasmodeloinserta
                #     modelo.save()
                # if seccion == 'derechainserta':
                #     modelo.numerocolumnasderechainserta = int(self.request.GET['valor'])
                #     context['derechainserta'] = modelo.numerocolumnasderechainserta
                #     modelo.save()

                # if seccion == 'izquierdaupdatecontiguo':
                #     modelo.numerocolumnasizquierdaupdate = int(self.request.GET['valor'])
                #     context['izquierdaupdatecontiguo'] = modelo.numerocolumnasizquierdaupdate
                #     modelo.save()
                # if seccion == 'modeloupdatecontiguo':
                #     modelo.numerocolumnasmodeloupdate = int(self.request.GET['valor'])
                #     context['modeloupdatecontiguo'] = modelo.numerocolumnasmodeloupdate
                #     modelo.save()
                # if seccion == 'derechaupdatecontiguo':
                #     modelo.numerocolumnasderechaupdate = int(self.request.GET['valor'])
                #     context['derechaupdatecontiguo'] = modelo.numerocolumnasderechaupdate
                #     modelo.save()
                # if seccion == 'hijosupdatecontiguo':
                #     modelo.numerocolumnashijosupdate = int(self.request.GET['valor'])
                #     context['hijosupdatecontiguo'] = modelo.numerocolumnashijosupdate
                #     modelo.save()

                # if seccion == 'izquierdaupdate':
                #     modelo.numerocolumnasizquierdaupdate = int(self.request.GET['valor'])
                #     context['izquierdaupdate'] = modelo.numerocolumnasizquierdaupdate
                #     proyecto.save()
                # if seccion == 'modeloupdate':
                #     modelo.numerocolumnasmodeloupdate = int(self.request.GET['valor'])
                #     context['modeloupdate'] = modelo.numerocolumnasmodeloupdate
                #     modelo.save()
                # if seccion == 'derechaupdate':
                #     modelo.numerocolumnasderechaupdate = int(self.request.GET['valor'])
                #     context['derechaupdate'] = modelo.numerocolumnasderechaupdate
                #     modelo.save()

                # if seccion == 'izquierdaborra':
                #     modelo.numerocolumnasizquierdaborra = int(self.request.GET['valor'])
                #     context['izquierdaborra'] = modelo.numerocolumnasizquierdaborra
                #     modelo.save()
                # if seccion == 'modeloborra':
                #     modelo.numerocolumnasmodeloborra = int(self.request.GET['valor'])
                #     context['modeloborra'] = modelo.numerocolumnasmodeloborra
                #     modelo.save()
                # if seccion == 'derechaborra':
                #     modelo.numerocolumnasderechaborra = int(self.request.GET['valor'])
                #     context['derechaborra'] = modelo.numerocolumnasderechaborra
                #     modelo.save()
            except:
                pass
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

def DoceColumnasInserta(modelo):
    if modelo.numerocolumnasizquierdainserta + \
        modelo.numerocolumnasmodeloinserta + \
        modelo.numerocolumnasderechainserta < 12:
        return False
    return True

def DoceColumnasUpdate(modelo, contiguo):
    if contiguo:
        if modelo.numerocolumnasizquierdaupdate + \
            modelo.numerocolumnasmodeloupdate + \
            modelo.numerocolumnasderechaupdate + \
            modelo.numerocolumnashijosupdate < 12:
            return False
        return True
    else:
        if modelo.numerocolumnasizquierdaupdate + \
            modelo.numerocolumnasmodeloupdate + \
            modelo.numerocolumnasderechaupdate < 12:
            return False
        return True

def DoceColumnasBorra(modelo):
    if modelo.numerocolumnasizquierdaborra + \
        modelo.numerocolumnasmodeloborra + \
        modelo.numerocolumnasderechaborra < 12:
        return False
    return True

class ConfigurarModeloNuevaView(TemplateView):
    template_name = "crear/configurar_modelo_nueva.html"

    def get_context_data(self,**kwargs):
        context = super(ConfigurarModeloNuevaView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)

        # Ver si esta en configuracion
        try:
            context['configuracion'] = self.request.GET['configuracion_proyecto']
        except:
            context['configuracion'] = 'false'

        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            modelo = Modelo.objects.get(id=self.request.GET['modelo_id'])
            context['anchomedioizquierda'] = proyecto.numerocolumnamedioizquierda
            context['anchomediocentro'] = proyecto.numerocolumnamediocentro
            context['anchomedioderecha'] = proyecto.numerocolumnamedioderecha
            context['izquierdainserta'] = modelo.numerocolumnasizquierdainserta
            context['modeloinserta'] = modelo.numerocolumnasmodeloinserta
            context['derechainserta'] = modelo.numerocolumnasderechainserta
            context['izquierdaupdatecontiguo'] = modelo.numerocolumnasizquierdaupdate
            context['modeloupdatecontiguo'] = modelo.numerocolumnasmodeloupdate
            context['derechaupdatecontiguo'] = modelo.numerocolumnasderechaupdate
            context['hijosupdatecontiguo'] = modelo.numerocolumnashijosupdate
            context['izquierdaupdate'] = modelo.numerocolumnasizquierdaupdate
            context['modeloupdate'] = modelo.numerocolumnasmodeloupdate
            context['derechaupdate'] = modelo.numerocolumnasderechaupdate
            context['izquierdaborra'] = modelo.numerocolumnasizquierdaborra
            context['modeloborra'] = modelo.numerocolumnasmodeloborra
            context['derechaborra'] = modelo.numerocolumnasderechaborra

            context['proyecto'] = proyecto
            context['modelo'] = modelo
            try:
                seccion = self.request.GET['seccion']
                if seccion == 'izquierdainserta':
                    modelo.numerocolumnasizquierdainserta = int(self.request.GET['valor'])
                    context['izquierdainserta'] = modelo.numerocolumnasizquierdainserta
                    modelo.save()
                if seccion == 'modeloinserta':
                    modelo.numerocolumnasmodeloinserta = int(self.request.GET['valor'])
                    context['modeloinserta'] = modelo.numerocolumnasmodeloinserta
                    modelo.save()
                if seccion == 'derechainserta':
                    modelo.numerocolumnasderechainserta = int(self.request.GET['valor'])
                    context['derechainserta'] = modelo.numerocolumnasderechainserta
                    modelo.save()

                if seccion == 'izquierdaupdatecontiguo':
                    modelo.numerocolumnasizquierdaupdate = int(self.request.GET['valor'])
                    context['izquierdaupdatecontiguo'] = modelo.numerocolumnasizquierdaupdate
                    modelo.save()
                if seccion == 'modeloupdatecontiguo':
                    modelo.numerocolumnasmodeloupdate = int(self.request.GET['valor'])
                    context['modeloupdatecontiguo'] = modelo.numerocolumnasmodeloupdate
                    modelo.save()
                if seccion == 'derechaupdatecontiguo':
                    modelo.numerocolumnasderechaupdate = int(self.request.GET['valor'])
                    context['derechaupdatecontiguo'] = modelo.numerocolumnasderechaupdate
                    modelo.save()
                if seccion == 'hijosupdatecontiguo':
                    modelo.numerocolumnashijosupdate = int(self.request.GET['valor'])
                    context['hijosupdatecontiguo'] = modelo.numerocolumnashijosupdate
                    modelo.save()

                if seccion == 'izquierdaupdate':
                    modelo.numerocolumnasizquierdaupdate = int(self.request.GET['valor'])
                    context['izquierdaupdate'] = modelo.numerocolumnasizquierdaupdate
                    proyecto.save()
                if seccion == 'modeloupdate':
                    modelo.numerocolumnasmodeloupdate = int(self.request.GET['valor'])
                    context['modeloupdate'] = modelo.numerocolumnasmodeloupdate
                    modelo.save()
                if seccion == 'derechaupdate':
                    modelo.numerocolumnasderechaupdate = int(self.request.GET['valor'])
                    context['derechaupdate'] = modelo.numerocolumnasderechaupdate
                    modelo.save()

                if seccion == 'izquierdaborra':
                    modelo.numerocolumnasizquierdaborra = int(self.request.GET['valor'])
                    context['izquierdaborra'] = modelo.numerocolumnasizquierdaborra
                    modelo.save()
                if seccion == 'modeloborra':
                    modelo.numerocolumnasmodeloborra = int(self.request.GET['valor'])
                    context['modeloborra'] = modelo.numerocolumnasmodeloborra
                    modelo.save()
                if seccion == 'derechaborra':
                    modelo.numerocolumnasderechaborra = int(self.request.GET['valor'])
                    context['derechaborra'] = modelo.numerocolumnasderechaborra
                    modelo.save()
            except:
                pass
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

class ConfigurarUpdateContiguoView(TemplateView):
    # template_name = "crear/configurar_base.html"
    template_name = "crear/configurar_update_contiguo.html"

    def get_context_data(self,**kwargs):
        context = super(ConfigurarUpdateContiguoView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)

        # Ver si esta en configuracion
        try:
            context['configuracion'] = self.request.GET['configuracion_proyecto']
        except:
            context['configuracion'] = 'false'

        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            modelo = Modelo.objects.get(id=self.request.GET['modelo_id'])
            context['altoencabezado'] = str(proyecto.altofilaenizcede) + 'px'
            context['altobume'] = str(proyecto.altofilabume) + 'px'
            context['altomedio'] = str(200) + 'px'
            context['altopie'] = str(proyecto.altofilapie) + 'px'
            context['anchoencabezadoizquierda'] = proyecto.numerocolumnaenizquierda 
            context['anchologo'] = proyecto.numerocolumnalogo
            context['anchotitulo'] = proyecto.numerocolumnatitulo
            context['anchologin'] = proyecto.numerocolumnalogin
            context['anchoencabezadoderecha'] = proyecto.numerocolumnaenderecha
            context['anchobumeizquierda'] = proyecto.numerocolumnabumeizquierda
            context['anchobusqueda'] = proyecto.numerocolumnabusqueda
            context['anchomenu'] = proyecto.numerocolumnamenu
            context['anchobumederecha'] = proyecto.numerocolumnabumederecha
            context['anchomedioizquierda'] = proyecto.numerocolumnamedioizquierda
            context['anchomedicocentro'] = proyecto.numerocolumnamediocentro
            context['anchomedioderecha'] = proyecto.numerocolumnamedioderecha
            context['numerocolumnaenizquierda'] = proyecto.numerocolumnaenizquierda
            context['numerocolumnalogo'] = proyecto.numerocolumnalogo
            context['numerocolumnatitulo'] = proyecto.numerocolumnatitulo
            context['numerocolumnalogin'] = proyecto.numerocolumnalogin
            context['numerocolumnaenderecha'] = proyecto.numerocolumnaenderecha
            context['numerocolumnabumeizquierda'] = proyecto.numerocolumnabumeizquierda
            context['numerocolumnabusqueda'] = proyecto.numerocolumnabusqueda
            context['numerocolumnamenu'] = proyecto.numerocolumnamenu
            context['numerocolumnabumederecha'] = proyecto.numerocolumnabumederecha
            context['numerocolumnamedioizquierda'] = proyecto.numerocolumnamedioizquierda
            context['numerocolumnamediocentro'] = proyecto.numerocolumnamediocentro
            context['numerocolumnamedioderecha'] = proyecto.numerocolumnamedioderecha

            context['columnasizquierdaupdate'] = modelo.numerocolumnasizquierdaupdate
            context['columnasderechaupdate'] = modelo.numerocolumnasderechaupdate
            context['columnasmodeloupdate'] = modelo.numerocolumnasmodeloupdate
            context['columnashijosupdate'] = modelo.numerocolumnashijosupdate

            # Alto y ancho de secciones

            try:
                flecha = self.request.GET['flecha']
                if flecha == "mi": #ancho izquierda medio
                    direccion = self.request.GET['direccion']
                    if direccion == 'menos':
                        if modelo.numerocolumnasizquierdaupdate > 0:
                            modelo.numerocolumnasizquierdaupdate =  modelo.numerocolumnasizquierdaupdate - 1
                            context['columnasizquierdaupdate'] =  modelo.numerocolumnasizquierdaupdate
                            modelo.save()
                            # context['numerocolumnalogo'] = proyecto.numerocolumnalogo + 1
                    else:
                        if modelo.numerocolumnasizquierdaupdate + modelo.numerocolumnasmodeloupdate + modelo.numerocolumnasderechaupdate  + modelo.numerocolumnashijosupdate < 12:
                            modelo.numerocolumnasizquierdaupdate =  modelo.numerocolumnasizquierdaupdate + 1
                            context['columnasizquierdaupdate'] =  modelo.numerocolumnasizquierdaupdate 
                            modelo.save()
                if flecha == "mc": #ancho medio
                    direccion = self.request.GET['direccion']
                    if direccion == 'menos':
                        if modelo.numerocolumnasmodeloupdate > 0:
                            modelo.numerocolumnasmodeloupdate =  modelo.numerocolumnasmodeloupdate - 1
                            context['columnasmodeloupdate'] =  modelo.numerocolumnasmodeloupdate
                            modelo.save()
                            # context['numerocolumnalogo'] = proyecto.numerocolumnalogo + 1
                    else:
                        if modelo.numerocolumnasizquierdaupdate + modelo.numerocolumnasmodeloupdate + modelo.numerocolumnasderechaupdate  + modelo.numerocolumnashijosupdate < 12:
                            modelo.numerocolumnasmodeloupdate =  modelo.numerocolumnasmodeloupdate + 1
                            context['columnasmodeloupdate'] =  modelo.numerocolumnasmodeloupdate
                            modelo.save()
                if flecha == "md": #ancho medio
                    direccion = self.request.GET['direccion']
                    if direccion == 'menos':
                        if modelo.numerocolumnasderechaupdate > 0:
                            modelo.numerocolumnasderechaupdate =  modelo.numerocolumnasderechaupdate - 1
                            context['columnasderechaupdate'] =  modelo.numerocolumnasderechaupdate
                            modelo.save()
                            # context['numerocolumnalogo'] = proyecto.numerocolumnalogo + 1
                    else:
                        if modelo.numerocolumnasizquierdaupdate + modelo.numerocolumnasmodeloupdate + modelo.numerocolumnasderechaupdate  + modelo.numerocolumnashijosupdate < 12:
                            modelo.numerocolumnasderechaupdate =  modelo.numerocolumnasderechaupdate + 1
                            context['columnasderechaupdate'] =  modelo.numerocolumnasderechaupdate
                            modelo.save()
                if flecha == "mh": #ancho medio
                    direccion = self.request.GET['direccion']
                    if direccion == 'menos':
                        if modelo.numerocolumnashijosupdate > 0:
                            modelo.numerocolumnashijosupdate =  modelo.numerocolumnashijosupdate - 1
                            context['columnashijosupdate'] =  modelo.numerocolumnashijosupdate
                            modelo.save()
                            # context['numerocolumnalogo'] = proyecto.numerocolumnalogo + 1
                    else:
                        if modelo.numerocolumnasizquierdaupdate + modelo.numerocolumnasmodeloupdate + modelo.numerocolumnasderechaupdate  + modelo.numerocolumnashijosupdate < 12:
                            modelo.numerocolumnashijosupdate =  modelo.numerocolumnashijosupdate + 1
                            context['columnashijosupdate'] =  modelo.numerocolumnashijosupdate
                            modelo.save()
            except:
                pass
            
            context['proyecto'] = proyecto
            context['modelo'] = modelo
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'        

        return context        

class ConfigurarUpdateAbajoView(TemplateView):
    # template_name = "crear/configurar_base.html"
    template_name = "crear/configurar_update_abajo.html"

    def get_context_data(self,**kwargs):
        context = super(ConfigurarUpdateAbajoView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)

        # Ver si esta en configuracion
        try:
            context['configuracion'] = self.request.GET['configuracion_proyecto']
        except:
            context['configuracion'] = 'false'

        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            modelo = Modelo.objects.get(id=self.request.GET['modelo_id'])
            context['altoencabezado'] = str(proyecto.altofilaenizcede) + 'px'
            context['altobume'] = str(proyecto.altofilabume) + 'px'
            context['altomedio'] = str(200) + 'px'
            context['altopie'] = str(proyecto.altofilapie) + 'px'
            context['anchoencabezadoizquierda'] = proyecto.numerocolumnaenizquierda 
            context['anchologo'] = proyecto.numerocolumnalogo
            context['anchotitulo'] = proyecto.numerocolumnatitulo
            context['anchologin'] = proyecto.numerocolumnalogin
            context['anchoencabezadoderecha'] = proyecto.numerocolumnaenderecha
            context['anchobumeizquierda'] = proyecto.numerocolumnabumeizquierda
            context['anchobusqueda'] = proyecto.numerocolumnabusqueda
            context['anchomenu'] = proyecto.numerocolumnamenu
            context['anchobumederecha'] = proyecto.numerocolumnabumederecha
            context['anchomedioizquierda'] = proyecto.numerocolumnamedioizquierda
            context['anchomedicocentro'] = proyecto.numerocolumnamediocentro
            context['anchomedioderecha'] = proyecto.numerocolumnamedioderecha
            context['numerocolumnaenizquierda'] = proyecto.numerocolumnaenizquierda
            context['numerocolumnalogo'] = proyecto.numerocolumnalogo
            context['numerocolumnatitulo'] = proyecto.numerocolumnatitulo
            context['numerocolumnalogin'] = proyecto.numerocolumnalogin
            context['numerocolumnaenderecha'] = proyecto.numerocolumnaenderecha
            context['numerocolumnabumeizquierda'] = proyecto.numerocolumnabumeizquierda
            context['numerocolumnabusqueda'] = proyecto.numerocolumnabusqueda
            context['numerocolumnamenu'] = proyecto.numerocolumnamenu
            context['numerocolumnabumederecha'] = proyecto.numerocolumnabumederecha
            context['numerocolumnamedioizquierda'] = proyecto.numerocolumnamedioizquierda
            context['numerocolumnamediocentro'] = proyecto.numerocolumnamediocentro
            context['numerocolumnamedioderecha'] = proyecto.numerocolumnamedioderecha

            context['columnasizquierdaupdate'] = modelo.numerocolumnasizquierdaupdate
            context['columnasderechaupdate'] = modelo.numerocolumnasderechaupdate
            context['columnasmodeloupdate'] = modelo.numerocolumnasmodeloupdate

            # Alto y ancho de secciones

            try:
                flecha = self.request.GET['flecha']
                if flecha == "mi": #ancho izquierda medio
                    direccion = self.request.GET['direccion']
                    if direccion == 'menos':
                        if modelo.numerocolumnasizquierdaupdate > 0:
                            modelo.numerocolumnasizquierdaupdate =  modelo.numerocolumnasizquierdaupdate - 1
                            context['columnasizquierdaupdate'] =  modelo.numerocolumnasizquierdaupdate
                            modelo.save()
                            # context['numerocolumnalogo'] = proyecto.numerocolumnalogo + 1
                    else:
                        if modelo.numerocolumnasizquierdaupdate + modelo.numerocolumnasmodeloupdate + modelo.numerocolumnasderechaupdate  < 12:
                            modelo.numerocolumnasizquierdaupdate =  modelo.numerocolumnasizquierdaupdate + 1
                            context['columnasizquierdaupdate'] =  modelo.numerocolumnasizquierdaupdate 
                            modelo.save()
                if flecha == "mc": #ancho medio
                    direccion = self.request.GET['direccion']
                    if direccion == 'menos':
                        if modelo.numerocolumnasmodeloupdate > 0:
                            modelo.numerocolumnasmodeloupdate =  modelo.numerocolumnasmodeloupdate - 1
                            context['columnasmodeloupdate'] =  modelo.numerocolumnasmodeloupdate
                            modelo.save()
                            # context['numerocolumnalogo'] = proyecto.numerocolumnalogo + 1
                    else:
                        if modelo.numerocolumnasizquierdaupdate + modelo.numerocolumnasmodeloupdate + modelo.numerocolumnasderechaupdate  < 12:
                            modelo.numerocolumnasmodeloupdate =  modelo.numerocolumnasmodeloupdate + 1
                            context['columnasmodeloupdate'] =  modelo.numerocolumnasmodeloupdate
                            modelo.save()
                if flecha == "md": #ancho medio
                    direccion = self.request.GET['direccion']
                    if direccion == 'menos':
                        if modelo.numerocolumnasderechaupdate > 0:
                            modelo.numerocolumnasderechaupdate =  modelo.numerocolumnasderechaupdate - 1
                            context['columnasderechaupdate'] =  modelo.numerocolumnasderechaupdate
                            modelo.save()
                            # context['numerocolumnalogo'] = proyecto.numerocolumnalogo + 1
                    else:
                        if modelo.numerocolumnasizquierdaupdate + modelo.numerocolumnasmodeloupdate + modelo.numerocolumnasderechaupdate  < 12:
                            modelo.numerocolumnasderechaupdate =  modelo.numerocolumnasderechaupdate + 1
                            context['columnasderechaupdate'] =  modelo.numerocolumnasderechaupdate
                            modelo.save()
            except:
                pass
            
            context['proyecto'] = proyecto
            context['modelo'] = modelo
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'        
        return context                

class ConfigurarBorraView(TemplateView):
    # template_name = "crear/configurar_base.html"
    template_name = "crear/configurar_update_borra.html"

    def get_context_data(self,**kwargs):
        context = super(ConfigurarBorraView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)

        # Ver si esta en configuracion
        try:
            context['configuracion'] = self.request.GET['configuracion_proyecto']
        except:
            context['configuracion'] = 'false'

        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            modelo = Modelo.objects.get(id=self.request.GET['modelo_id'])
            context['altoencabezado'] = str(proyecto.altofilaenizcede) + 'px'
            context['altobume'] = str(proyecto.altofilabume) + 'px'
            context['altomedio'] = str(200) + 'px'
            context['altopie'] = str(proyecto.altofilapie) + 'px'
            context['anchoencabezadoizquierda'] = proyecto.numerocolumnaenizquierda 
            context['anchologo'] = proyecto.numerocolumnalogo
            context['anchotitulo'] = proyecto.numerocolumnatitulo
            context['anchologin'] = proyecto.numerocolumnalogin
            context['anchoencabezadoderecha'] = proyecto.numerocolumnaenderecha
            context['anchobumeizquierda'] = proyecto.numerocolumnabumeizquierda
            context['anchobusqueda'] = proyecto.numerocolumnabusqueda
            context['anchomenu'] = proyecto.numerocolumnamenu
            context['anchobumederecha'] = proyecto.numerocolumnabumederecha
            context['anchomedioizquierda'] = proyecto.numerocolumnamedioizquierda
            context['anchomedicocentro'] = proyecto.numerocolumnamediocentro
            context['anchomedioderecha'] = proyecto.numerocolumnamedioderecha
            context['numerocolumnaenizquierda'] = proyecto.numerocolumnaenizquierda
            context['numerocolumnalogo'] = proyecto.numerocolumnalogo
            context['numerocolumnatitulo'] = proyecto.numerocolumnatitulo
            context['numerocolumnalogin'] = proyecto.numerocolumnalogin
            context['numerocolumnaenderecha'] = proyecto.numerocolumnaenderecha
            context['numerocolumnabumeizquierda'] = proyecto.numerocolumnabumeizquierda
            context['numerocolumnabusqueda'] = proyecto.numerocolumnabusqueda
            context['numerocolumnamenu'] = proyecto.numerocolumnamenu
            context['numerocolumnabumederecha'] = proyecto.numerocolumnabumederecha
            context['numerocolumnamedioizquierda'] = proyecto.numerocolumnamedioizquierda
            context['numerocolumnamediocentro'] = proyecto.numerocolumnamediocentro
            context['numerocolumnamedioderecha'] = proyecto.numerocolumnamedioderecha

            context['columnasizquierdaborra'] = modelo.numerocolumnasizquierdaborra
            context['columnasderechaborra'] = modelo.numerocolumnasderechaborra
            context['columnasmodeloborra'] = modelo.numerocolumnasmodeloborra

            # Alto y ancho de secciones

            try:
                flecha = self.request.GET['flecha']
                if flecha == "mi": #ancho izquierda medio
                    direccion = self.request.GET['direccion']
                    if direccion == 'menos':
                        if modelo.numerocolumnasizquierdaborra > 0:
                            modelo.numerocolumnasizquierdaborra =  modelo.numerocolumnasizquierdaborra - 1
                            context['columnasizquierdaborra'] =  modelo.numerocolumnasizquierdaborra
                            modelo.save()
                            # context['numerocolumnalogo'] = proyecto.numerocolumnalogo + 1
                    else:
                        if modelo.numerocolumnasizquierdaborra + modelo.numerocolumnasmodeloborra + modelo.numerocolumnasderechaborra  < 12:
                            modelo.numerocolumnasizquierdaborra =  modelo.numerocolumnasizquierdaborra + 1
                            context['columnasizquierdaborrra'] =  modelo.numerocolumnasizquierdaborra 
                            modelo.save()
                if flecha == "mc": #ancho medio
                    direccion = self.request.GET['direccion']
                    if direccion == 'menos':
                        if modelo.numerocolumnasmodeloborra > 0:
                            modelo.numerocolumnasmodeloborra =  modelo.numerocolumnasmodeloborra - 1
                            context['columnasmodeloborra'] =  modelo.numerocolumnasmodeloborra
                            modelo.save()
                            # context['numerocolumnalogo'] = proyecto.numerocolumnalogo + 1
                    else:
                        if modelo.numerocolumnasizquierdaborra + modelo.numerocolumnasmodeloborra + modelo.numerocolumnasderechaborra  < 12:
                            modelo.numerocolumnasmodeloborra =  modelo.numerocolumnasmodeloborra + 1
                            context['columnasmodeloborra'] =  modelo.numerocolumnasmodeloborra
                            modelo.save()
                if flecha == "md": #ancho medio
                    direccion = self.request.GET['direccion']
                    if direccion == 'menos':
                        if modelo.numerocolumnasderechaborra > 0:
                            modelo.numerocolumnasderechaborra =  modelo.numerocolumnasderechaborra - 1
                            context['columnasderechaborra'] =  modelo.numerocolumnasderechaborra
                            modelo.save()
                            # context['numerocolumnalogo'] = proyecto.numerocolumnalogo + 1
                    else:
                        if modelo.numerocolumnasizquierdaborra + modelo.numerocolumnasmodeloborra + modelo.numerocolumnasderechaborra  < 12:
                            modelo.numerocolumnasderechaborra =  modelo.numerocolumnasderechaborra + 1
                            context['columnasderechaborra'] =  modelo.numerocolumnasderechaborra
                            modelo.save()
            except:
                pass
            
            context['proyecto'] = proyecto
            context['modelo'] = modelo
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'        
        return context                        

class CrearPasosView(TemplateView):
    template_name = "crear/crear_pasos.html"

    def get_context_data(self,**kwargs):
        context = super(CrearPasosView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            proyecto = Proyecto.objects.get(id = self.request.GET['proyecto_id'],usuario=self.request.user)
            context['error'] = ''
            paso = self.request.GET['paso']
            context['paso'] = paso
            lista = []
            if paso == '1':
                lista.append(['Crea el directorio',proyecto.nombre,2,9,1])
                lista.append(['Crea el directorio',proyecto.nombre + '/media',2,9,2])
                lista.append(['Crea el directorio',proyecto.nombre + '/' + proyecto.nombre,2,9,3])
                lista.append(['Crea el archivo',proyecto.nombre + '/' + proyecto.nombre + '/_init_.py',2,9,4])
                lista.append(['Crea el archivo',proyecto.nombre + '/' + proyecto.nombre + '/settings.py (p)',2,9,5])
                lista.append(['Crea el archivo',proyecto.nombre + '/' + proyecto.nombre + '/urls.py',2,9,6])
                lista.append(['Crea el archivo',proyecto.nombre + '/' + proyecto.nombre + '/wsgi.py',2,9,7])
                lista.append(['Crea el archivo',proyecto.nombre + '/manage.py',2,9,8])
            if paso == '2':
                num = 1
                for ap in Aplicacion.objects.filter(proyecto=proyecto):
                    lista.append(['Crea el directorio',proyecto.nombre + '/' + ap.nombre,2,9,num])
                    num += 1
                for ap in Aplicacion.objects.filter(proyecto=proyecto):
                    lista.append(['Crea el directorio',proyecto.nombre + '/' + ap.nombre + '/migrations' ,2,9,num])
                    num += 1
                for ap in Aplicacion.objects.filter(proyecto=proyecto):
                    lista.append(['Crea el directorio',proyecto.nombre + '/' + ap.nombre + '/migrations/_init_.py' ,2,9,num])
                    num += 1
                for ap in Aplicacion.objects.filter(proyecto=proyecto):
                    lista.append(['Crea el directorio',proyecto.nombre + '/' + ap.nombre + '/migrations/_pycache_' ,2,9,num])
                    num += 1
                for ap in Aplicacion.objects.filter(proyecto=proyecto):
                    lista.append(['Crea el directorio',proyecto.nombre + '/' + ap.nombre + '/templates' ,2,9,num])
                    num += 1
                for ap in Aplicacion.objects.filter(proyecto=proyecto):
                    lista.append(['Crea el directorio',proyecto.nombre + '/' + ap.nombre + '/templates/' ,2,9,num])
                    num += 1
                for ap in Aplicacion.objects.filter(proyecto=proyecto):
                    lista.append(['Crea el archivo',proyecto.nombre + '/' + ap.nombre + '/_init_.py' ,2,9,num])
                    num += 1
                for ap in Aplicacion.objects.filter(proyecto=proyecto):
                    lista.append(['Crea el archivo',proyecto.nombre + '/' + ap.nombre + '/admin.py' ,2,9,num])
                    num += 1
                for ap in Aplicacion.objects.filter(proyecto=proyecto):
                    lista.append(['Crea el archivo',proyecto.nombre + '/' + ap.nombre + '/apps.py' ,2,9,num])
                    num += 1
                for ap in Aplicacion.objects.filter(proyecto=proyecto):
                    lista.append(['Crea el archivo',proyecto.nombre + '/' + ap.nombre + '/models.py' ,2,9,num])
                    num += 1
                for ap in Aplicacion.objects.filter(proyecto=proyecto):
                    lista.append(['Crea el archivo',proyecto.nombre + '/' + ap.nombre + '/tests.py' ,2,9,num])
                    num += 1
                lista.append(['Crea el directorio',proyecto.nombre + '/core/templates/core/includes',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/core/templates/core/includes/css_general.html (p)',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/core/templates/core/includes/js_general.html (p)',2,9,num])
                num += 1
                lista.append(['Crea el directorio',proyecto.nombre + '/core/static',2,9,num])
                num += 1
                lista.append(['Crea el directorio',proyecto.nombre + '/core/static/core',2,9,num])
                num += 1
                lista.append(['Crea el directorio',proyecto.nombre + '/core/static/core/css',2,9,num])
                num += 1
                lista.append(['Crea el directorio',proyecto.nombre + '/core/static/core/js',2,9,num])
                num += 1
                lista.append(['Crea el directorio',proyecto.nombre + '/core/static/core/img',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/core/static/core/css/animation.css',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/core/static/core/css/bootstrap.css',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/core/static/core/css/bootstrap.min.css',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/core/static/core/js/Bootstrap.min.js',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/core/static/core/js/jquery_3.4.1.min.js',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/core/static/core/js/popper.min.js',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/core/static/core/js/js_propios.js',2,9,num])
                num += 1
                lista.append(['Actualizar el archivo',proyecto.nombre + '/' + proyecto.nombre + '/settings.py',2,9,num])
                num += 1
            if paso == '3':
                num = 1
                for ap in Aplicacion.objects.filter(proyecto=proyecto):
                    lista.append(['Actualiza el archivo',proyecto.nombre + '/' + ap.nombre + '/models.py (p)' ,2,9,num])
                    num += 1
            if paso == '4':
                num = 1
                for ap in Aplicacion.objects.filter(proyecto=proyecto):
                    lista.append(['Crear las vistas',proyecto.nombre + '/' + ap.nombre + '/views.py (p)' ,2,9,num])
                    num += 1
            if paso == '5':
                num = 1
                for ap in Aplicacion.objects.filter(proyecto=proyecto):
                    lista.append(['Crear las urls',proyecto.nombre + '/' + ap.nombre + '/urls.py (p)' ,2,9,num])
                    num += 1
            if paso == '6':
                num = 1
                for ap in Aplicacion.objects.filter(proyecto=proyecto):
                    lista.append(['Crear los formularios',proyecto.nombre + '/' + ap.nombre + '/forms.py (p)' ,2,9,num])
                    num += 1
            if paso == '7':
                num = 1
                lista.append(['Crea el archivo',proyecto.nombre + '/core/templates/core/base.html (p)',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/core/templates/core/home.html (p)',2,9,num])
                num += 1
                for ap in Aplicacion.objects.filter(proyecto=proyecto):
                    if ap.nombre != 'registration':
                        lista.append(['Crea el archivo',proyecto.nombre + '/core/templates/core/includes/menu_' + ap.nombre + '.html (p)',2,9,num])
                        num += 1
                for md in Modelo.objects.filter(proyecto=proyecto):
                    if md.padre == 'nada':
                        lista.append(['Crea el archivo',proyecto.nombre + '/' + md.aplicacion.nombre + '/templates/' + md.aplicacion.nombre + '/' + md.nombre + '_list.html (p)',2,9,num])
                        num += 1
                    lista.append(['Crea el archivo',proyecto.nombre + '/' + md.aplicacion.nombre + '/templates/' + md.aplicacion.nombre + '/' + md.nombre + '_form.html (p)',2,9,num])
                    num += 1
                    lista.append(['Crea el archivo',proyecto.nombre + '/' + md.aplicacion.nombre + '/templates/' + md.aplicacion.nombre + '/' + md.nombre + '_update_form.html (p)',2,9,num])
                    num += 1
                    lista.append(['Crea el archivo',proyecto.nombre + '/' + md.aplicacion.nombre + '/templates/' + md.aplicacion.nombre + '/' + md.nombre + '_confirm_delete.html (p)',2,9,num])
                    num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/core/static/core/css/estilos.css (p)',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/core/static/core/css/modelo_borra.css (p)',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/core/static/core/css/modelo_hijo.css (p)',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/core/static/core/css/modelo_inserta.css (p)',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/core/static/core/css/modelo_list.css (p)',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/core/static/core/css/modelo_update.css (p)',2,9,num])
                num += 1
            if paso == '8':
                num = 1
                lista.append(['Crea el archivo',proyecto.nombre + '/registration/views.py (p)',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/registration/models.py (p)',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/registration/urls.py (p)',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/registration/forms.py (p)',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/registration/views.py (p)',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/registration/templates/registration/login.html (p)',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/registration/templates/registration/password_change_done.html (p)',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/registration/templates/registration/password_change_forms.html (p)',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/registration/templates/registration/password_reset_complete.html (p)',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/registration/templates/registration/password_reset_confirm.html (p)',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/registration/templates/registration/password_reset_done.html (p)',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/registration/templates/registration/password_reset_form.html (p)',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/registration/templates/registration/profile_form.html (p)',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/registration/templates/registration/profile_email_form.html (p)',2,9,num])
                num += 1
                lista.append(['Crea el archivo',proyecto.nombre + '/registration/templates/registration/registro.html (p)',2,9,num])
                num += 1

            context['lista'] = lista
            context['proyecto'] = proyecto
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

class EditarReporteView(UpdateView):
    model = ReporteNuevo
    form_class = ReporteForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('proyectos:arbol') + '?proyecto_id=' + self.request.GET['proyecto_id'] + '&ok'
        # return reverse_lazy('proyectos:arbol') + '?ok'

    def get_context_data(self,**kwargs):
        context = super(EditarReporteView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'])   
            context['size'] = 'A4'            
            if self.request.GET['size'] == 'L':         
                context['size'] = 'Letter'            
            context['orientacion'] = 'Landscape'            
            if self.request.GET['orientacion'] == 'P':         
                context['orientacion'] = 'Portrait'            
            context['proyecto'] = proyecto
            context['proyecto_id'] = proyecto.id
            context['reporte'] = ReporteNuevo.objects.get(reportesize=self.request.GET['size'],orientacion=self.request.GET['orientacion'])
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

from proyectos.models import Proyecto
from .forms import Conf_11Form
from .forms import Conf_12Form
from .forms import Conf_13Form
from .forms import Conf_14Form
from .forms import Conf_15Form
from .forms import Conf_21Form
from .forms import Conf_22Form
from .forms import Conf_23Form
from .forms import Conf_24Form
from .forms import Conf_31Form
from .forms import Conf_32Form
from .forms import Conf_33Form
from django.shortcuts import render
from django.http import HttpResponse


class ConfiguraProyectoView(TemplateView):
    template_name =  'crear/template_proyecto.html'

    def get_context_data(self,**kwargs):
        context = super(ConfiguraProyectoView, self).get_context_data(**kwargs)
        proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'])
        context['proyecto'] = proyecto
        return context

class Conf_11(UpdateView):
    model = Proyecto    
    template_name =  'crear/conf_11.html'
    form_class = Conf_11Form

    def get_context_data(self, ** kwargs):
        context = super(Conf_11, self).get_context_data(**kwargs)
        # proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'])
        context['proyecto'] = self.object
        return context

    def post(self,request,*args,**kwargs):
        form = self.get_form()
        proyecto = Proyecto.objects.get(id=self.request.POST['proyecto_id'])
        if form.is_valid():
            Datos = form.save(commit=False)
            proyecto.altofilaenizcede = Datos.altofilaenizcede
            proyecto.altocolumnaenizquierda = Datos.altocolumnaenizquierda
            proyecto.colorfilaenizcede = Datos.colorfilaenizcede
            proyecto.colorcolumnaenizquierda = Datos.colorcolumnaenizquierda
            proyecto.enborde = Datos.enborde
            proyecto.enanchoborde = Datos.enanchoborde
            proyecto.encolorborde = Datos.encolorborde
            # Control de secciones
            if Datos.numerocolumnaenizquierda >= 0:
                proyecto.numerocolumnaenizquierda = Datos.numerocolumnaenizquierda
            proyecto.save()
        return render(request, 'crear/template_proyecto.html', {'proyecto':proyecto})

class Conf_12(UpdateView):
    model = Proyecto    
    template_name =  'crear/conf_12.html'
    form_class = Conf_12Form

    def get_context_data(self, ** kwargs):
        context = super(Conf_12, self).get_context_data(**kwargs)
        # proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'])
        context['proyecto'] = self.object
        return context

    def post(self,request,*args,**kwargs):
        form = self.get_form()
        proyecto = Proyecto.objects.get(id=self.request.POST['proyecto_id'])
        if form.is_valid():
            Datos = form.save(commit=False)
            proyecto.altocolumnalogo = Datos.altocolumnalogo
            proyecto.colorcolumnalogo = Datos.colorcolumnalogo
            proyecto.numerocolumnalogo = Datos.numerocolumnalogo
            proyecto.justificacionhorizontallogo = Datos.justificacionhorizontallogo
            proyecto.justificacionverticallogo = Datos.justificacionverticallogo
            proyecto.avatarheight = Datos.avatarheight
            proyecto.avatarwidth = Datos.avatarwidth
            proyecto.save()
        return render(request, 'crear/template_proyecto.html', {'proyecto':proyecto})        

class Conf_13(UpdateView):
    model = Proyecto    
    template_name =  'crear/conf_13.html'
    form_class = Conf_13Form

    def get_context_data(self, ** kwargs):
        context = super(Conf_13, self).get_context_data(**kwargs)
        # proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'])
        context['proyecto'] = self.object
        return context

    def post(self,request,*args,**kwargs):
        form = self.get_form()
        proyecto = Proyecto.objects.get(id=self.request.POST['proyecto_id'])
        if form.is_valid():
            Datos = form.save(commit=False)
            proyecto.altocolumnatitulo = Datos.altocolumnatitulo
            proyecto.colorcolumnatitulo = Datos.colorcolumnatitulo
            proyecto.numerocolumnatitulo = Datos.numerocolumnatitulo
            proyecto.justificacionhorizontaltitulo = Datos.justificacionhorizontaltitulo
            proyecto.justificacionverticaltitulo = Datos.justificacionverticaltitulo
            proyecto.imagentitulowidth = Datos.imagentitulowidth
            proyecto.imagentituloheight = Datos.imagentituloheight
            proyecto.save()
        return render(request, 'crear/template_proyecto.html', {'proyecto':proyecto})                

class Conf_14(UpdateView):
    model = Proyecto    
    template_name =  'crear/conf_14.html'
    form_class = Conf_14Form

    def get_context_data(self, ** kwargs):
        context = super(Conf_14, self).get_context_data(**kwargs)
        # proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'])
        context['proyecto'] = self.object
        return context

    def post(self,request,*args,**kwargs):
        form = self.get_form()
        proyecto = Proyecto.objects.get(id=self.request.POST['proyecto_id'])
        if form.is_valid():
            Datos = form.save(commit=False)
            proyecto.altocolumnalogin = Datos.altocolumnalogin
            proyecto.colorcolumnalogin = Datos.colorcolumnalogin
            proyecto.numerocolumnalogin = Datos.numerocolumnalogin
            proyecto.save()
        return render(request, 'crear/template_proyecto.html', {'proyecto':proyecto})

class Conf_15(UpdateView):
    model = Proyecto    
    template_name =  'crear/conf_15.html'
    form_class = Conf_15Form

    def get_context_data(self, ** kwargs):
        context = super(Conf_15, self).get_context_data(**kwargs)
        # proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'])
        context['proyecto'] = self.object
        return context

    def post(self,request,*args,**kwargs):
        form = self.get_form()
        proyecto = Proyecto.objects.get(id=self.request.POST['proyecto_id'])
        if form.is_valid():
            Datos = form.save(commit=False)
            proyecto.altocolumnaenderecha = Datos.altocolumnaenderecha
            proyecto.colorcolumnaenderecha = Datos.colorcolumnaenderecha
            proyecto.numerocolumnaenderecha = Datos.numerocolumnaenderecha
            proyecto.save()
        return render(request, 'crear/template_proyecto.html', {'proyecto':proyecto})

class Conf_21(UpdateView):
    model = Proyecto    
    template_name =  'crear/conf_21.html'
    form_class = Conf_21Form

    def get_context_data(self, ** kwargs):
        context = super(Conf_21, self).get_context_data(**kwargs)
        # proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'])
        context['proyecto'] = self.object
        return context

    def post(self,request,*args,**kwargs):
        form = self.get_form()
        proyecto = Proyecto.objects.get(id=self.request.POST['proyecto_id'])
        if form.is_valid():
            Datos = form.save(commit=False)
            proyecto.altofilabume = Datos.altofilabume
            proyecto.altocolumnabumeizquierda = Datos.altocolumnabumeizquierda
            proyecto.colorfilabume = Datos.colorfilabume
            proyecto.colorcolumnabumeizquierda = Datos.colorcolumnabumeizquierda
            proyecto.bumeborde = Datos.bumeborde
            proyecto.bumeanchoborde = Datos.bumeanchoborde
            proyecto.bumecolorborde = Datos.bumecolorborde
            # Control de secciones
            if Datos.numerocolumnabumeizquierda >= 0:
                proyecto.numerocolumnabumeizquierda = Datos.numerocolumnabumeizquierda
            proyecto.save()
        return render(request, 'crear/template_proyecto.html', {'proyecto':proyecto})

class Conf_22(UpdateView):
    model = Proyecto    
    template_name =  'crear/conf_22.html'
    form_class = Conf_22Form

    def get_context_data(self, ** kwargs):
        context = super(Conf_22, self).get_context_data(**kwargs)
        # proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'])
        context['proyecto'] = self.object
        return context

    def post(self,request,*args,**kwargs):
        form = self.get_form()
        proyecto = Proyecto.objects.get(id=self.request.POST['proyecto_id'])
        if form.is_valid():
            Datos = form.save(commit=False)
            proyecto.altocolumnabusqueda = Datos.altocolumnabusqueda
            proyecto.colorcolumnabusqueda = Datos.colorcolumnabusqueda
            # Control de secciones
            if Datos.numerocolumnabusqueda >= 0:
                proyecto.numerocolumnabusqueda = Datos.numerocolumnabusqueda
            proyecto.save()
        return render(request, 'crear/template_proyecto.html', {'proyecto':proyecto})

class Conf_23(UpdateView):
    model = Proyecto    
    template_name =  'crear/conf_23.html'
    form_class = Conf_23Form

    def get_context_data(self, ** kwargs):
        context = super(Conf_23, self).get_context_data(**kwargs)
        # proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'])
        context['proyecto'] = self.object
        return context

    def post(self,request,*args,**kwargs):
        form = self.get_form()
        proyecto = Proyecto.objects.get(id=self.request.POST['proyecto_id'])
        if form.is_valid():
            Datos = form.save(commit=False)
            proyecto.altocolumnamenu = Datos.altocolumnamenu
            proyecto.colorcolumnamenu = Datos.colorcolumnamenu
            # Control de secciones
            if Datos.numerocolumnamenu >= 0:
                proyecto.numerocolumnamenu = Datos.numerocolumnamenu
            proyecto.save()
        return render(request, 'crear/template_proyecto.html', {'proyecto':proyecto})

class Conf_24(UpdateView):
    model = Proyecto    
    template_name =  'crear/conf_24.html'
    form_class = Conf_24Form

    def get_context_data(self, ** kwargs):
        context = super(Conf_24, self).get_context_data(**kwargs)
        # proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'])
        context['proyecto'] = self.object
        return context

    def post(self,request,*args,**kwargs):
        form = self.get_form()
        proyecto = Proyecto.objects.get(id=self.request.POST['proyecto_id'])
        if form.is_valid():
            Datos = form.save(commit=False)
            proyecto.altocolumnabumederecha = Datos.altocolumnabumederecha
            proyecto.colorcolumnabumederecha = Datos.colorcolumnabumederecha
            # Control de secciones
            if Datos.numerocolumnabumederecha >= 0:
                proyecto.numerocolumnabumederecha = Datos.numerocolumnabumederecha
            proyecto.save()
        return render(request, 'crear/template_proyecto.html', {'proyecto':proyecto})

class Conf_31(UpdateView):
    model = Proyecto    
    template_name =  'crear/conf_31.html'
    form_class = Conf_31Form

    def get_context_data(self, ** kwargs):
        context = super(Conf_31, self).get_context_data(**kwargs)
        # proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'])
        context['proyecto'] = self.object
        return context

    def post(self,request,*args,**kwargs):
        form = self.get_form()
        proyecto = Proyecto.objects.get(id=self.request.POST['proyecto_id'])
        if form.is_valid():
            Datos = form.save(commit=False)
            proyecto.altofilamedio = Datos.altofilamedio
            proyecto.altocolumnamedioizquierda = Datos.altocolumnamedioizquierda
            proyecto.colorfilamedio = Datos.colorfilamedio
            proyecto.colorcolumnamedioizquierda = Datos.colorcolumnamedioizquierda
            proyecto.cenborde = Datos.cenborde
            proyecto.cenanchoborde = Datos.cenanchoborde
            proyecto.cencolorborde = Datos.cencolorborde
            # Control de secciones
            if Datos.numerocolumnamedioizquierda >= 0:
                proyecto.numerocolumnamedioizquierda = Datos.numerocolumnamedioizquierda
            proyecto.save()
        return render(request, 'crear/template_proyecto.html', {'proyecto':proyecto})

class Conf_32(UpdateView):
    model = Proyecto    
    template_name =  'crear/conf_32.html'
    form_class = Conf_32Form

    def get_context_data(self, ** kwargs):
        context = super(Conf_32, self).get_context_data(**kwargs)
        # proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'])
        context['proyecto'] = self.object
        return context

    def post(self,request,*args,**kwargs):
        form = self.get_form()
        proyecto = Proyecto.objects.get(id=self.request.POST['proyecto_id'])
        if form.is_valid():
            Datos = form.save(commit=False)
            proyecto.altocolumnamediocentro = Datos.altocolumnamediocentro
            proyecto.colorcolumnamediocentro = Datos.colorcolumnamediocentro
            # Control de secciones
            if Datos.numerocolumnamediocentro >= 0:
                proyecto.numerocolumnamediocentro = Datos.numerocolumnamediocentro
            proyecto.save()
        return render(request, 'crear/template_proyecto.html', {'proyecto':proyecto})

class Conf_33(UpdateView):
    model = Proyecto    
    template_name =  'crear/conf_33.html'
    form_class = Conf_33Form

    def get_context_data(self, ** kwargs):
        context = super(Conf_33, self).get_context_data(**kwargs)
        # proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'])
        context['proyecto'] = self.object
        return context

    def post(self,request,*args,**kwargs):
        form = self.get_form()
        proyecto = Proyecto.objects.get(id=self.request.POST['proyecto_id'])
        if form.is_valid():
            Datos = form.save(commit=False)
            proyecto.altocolumnamedioderecha = Datos.altocolumnamedioderecha
            proyecto.colorcolumnamedioderecha = Datos.colorcolumnamedioderecha
            # Control de secciones
            if Datos.numerocolumnamedioderecha >= 0:
                proyecto.numerocolumnamedioderecha = Datos.numerocolumnamedioderecha
            proyecto.save()
        return render(request, 'crear/template_proyecto.html', {'proyecto':proyecto})

class PanelAjustableView(TemplateView):
    template_name = 'crear/panel_ajustable.html'

    def get_context_data(self,**kwargs):
        context = super(PanelAjustableView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)

        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            context['proyecto'] = proyecto
            try:
                name = self.request.GET['name']
                crece = self.request.GET['crece']
                if name == 'pfpc':
                    if crece == 'abajo':
                        proyecto.altofilaenizcede += 1
                    if crece == 'derecha':
                        if not PfDoceColumnas(proyecto):
                            proyecto.numerocolumnaenizquierda += 1
                        elif proyecto.numerocolumnalogo > 1:
                            proyecto.numerocolumnalogo -= 1
                            proyecto.numerocolumnaenizquierda += 1
                if name == 'pfsc':
                    if crece == 'izquierda':
                        if proyecto.numerocolumnaenizquierda > 1:
                            # proyecto.numerocolumnalogo += 1
                            proyecto.numerocolumnaenizquierda -= 1
                    if crece == 'derecha':
                        if not PfDoceColumnas(proyecto):
                            proyecto.numerocolumnalogo += 1
                        elif proyecto.numerocolumnatitulo > 1:
                            proyecto.numerocolumnatitulo -= 1
                            proyecto.numerocolumnalogo += 1
                if name == 'pftc':
                    if crece == 'izquierda':
                        if proyecto.numerocolumnalogo > 1:
                            # proyecto.numerocolumnatitulo += 1
                            proyecto.numerocolumnalogo -= 1
                    if crece == 'derecha':
                        if not PfDoceColumnas(proyecto):
                            proyecto.numerocolumnatitulo += 1
                        elif proyecto.numerocolumnalogin > 1:
                            proyecto.numerocolumnalogin -= 1
                            proyecto.numerocolumnatitulo += 1
                if name == 'pfcc':
                    if crece == 'izquierda':
                        if proyecto.numerocolumnatitulo > 1:
                            # proyecto.numerocolumnalogin += 1
                            proyecto.numerocolumnatitulo -= 1
                    if crece == 'derecha':
                        if not PfDoceColumnas(proyecto):
                            proyecto.numerocolumnalogin += 1
                        elif proyecto.numerocolumnaenderecha > 1:
                            proyecto.numerocolumnalogin += 1
                            proyecto.numerocolumnaenderecha -= 1
                if name == 'pfqc':
                    if crece == 'izquierda':
                        if proyecto.numerocolumnalogin > 1:
                            # proyecto.numerocolumnaenderecha += 1
                            proyecto.numerocolumnalogin -= 1
                    if crece == 'derecha':
                        if not PfDoceColumnas(proyecto):
                            # proyecto.numerocolumnaenderecha += 1
                            proyecto.numerocolumnaenderecha += 1
                if name == 'sfpc':
                    if crece == 'abajo':
                        proyecto.altofilabume += 1
                    if crece == 'arriba':
                        proyecto.altofilaenizcede -= 1
                    if crece == 'derecha':
                        if not SfDoceColumnas(proyecto):
                            proyecto.numerocolumnabumeizquierda +=1
                        elif proyecto.numerocolumnabusqueda > 1:
                            proyecto.numerocolumnabusqueda -= 1
                            proyecto.numerocolumnabumeizquierda += 1
                if name == 'sfsc':
                    if crece == 'derecha':
                        if not SfDoceColumnas(proyecto):
                            proyecto.numerocolumnabusqueda+1
                        if proyecto.numerocolumnamenu > 1:
                            proyecto.numerocolumnabusqueda += 1
                            proyecto.numerocolumnamenu -= 1
                    if crece == 'izquierda':
                        if proyecto.numerocolumnabumeizquierda > 1:
                            # proyecto.numerocolumnabusqueda += 1
                            proyecto.numerocolumnabumeizquierda -= 1
                if name == 'sftc':
                    if crece == 'derecha':
                        if not SfDoceColumnas(proyecto):
                            proyecto.numerocolumnamenu +=1
                        elif proyecto.numerocolumnabumederecha > 1:
                            proyecto.numerocolumnamenu += 1
                            proyecto.numerocolumnabumederecha -= 1
                    if crece == 'izquierda':
                        if proyecto.numerocolumnabusqueda > 1:
                            # proyecto.numerocolumnamenu += 1
                            proyecto.numerocolumnabusqueda -= 1
                if name == 'sfcc':
                    if crece == 'izquierda':
                        if proyecto.numerocolumnamenu > 1:
                            proyecto.numerocolumnamenu -= 1
                            # proyecto.numerocolumnabumederecha += 1
                    if crece == 'derecha':
                        if not SfDoceColumnas(proyecto):
                            # proyecto.numerocolumnaenderecha += 1
                            proyecto.numerocolumnabumederecha += 1
                if name == 'tfpc':
                    if crece == 'arriba':
                        proyecto.altofilabume -= 1
                    if crece == 'derecha':
                        if not TfDoceColumnas(proyecto):
                            proyecto.numerocolumnamedioizquierda += 1
                        elif proyecto.numerocolumnamediocentro > 1:
                            proyecto.numerocolumnamedioizquierda += 1
                            proyecto.numerocolumnamediocentro -= 1
                if name == 'tfsc':
                    if crece == 'derecha':
                        if not TfDoceColumnas(proyecto):
                            proyecto.numerocolumnamediocentro += 1
                        elif proyecto.numerocolumnamedioderecha > 1:
                            proyecto.numerocolumnamedioderecha -= 1
                            proyecto.numerocolumnamediocentro += 1
                    if crece == 'izquierda':
                        if proyecto.numerocolumnamedioizquierda > 1:
                            proyecto.numerocolumnamedioizquierda -= 1
                            # proyecto.numerocolumnamediocentro += 1
                if name == 'tftc':
                    if crece == 'izquierda':
                        if proyecto.numerocolumnamediocentro > 1:
                            # proyecto.numerocolumnamedioderecha += 1
                            proyecto.numerocolumnamediocentro -= 1
                    if crece == 'derecha':
                        if not TfDoceColumnas(proyecto):
                            # proyecto.numerocolumnaenderecha += 1
                            proyecto.numerocolumnamedioderecha += 1
                if name == 'cfpc':
                    if crece == 'arriba':
                        proyecto.altofilapie -= 1
                    if crece == 'abajo':
                        proyecto.altofilapie += 1
                proyecto.save()
                context['proyecto'] = proyecto
            except:
                pass
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

def PfDoceColumnas(proyecto):
    if proyecto.numerocolumnaenizquierda + \
        proyecto.numerocolumnalogo + \
        proyecto.numerocolumnatitulo + \
        proyecto.numerocolumnalogin + \
        proyecto.numerocolumnaenderecha >= 12:
        return True
    return False

def SfDoceColumnas(proyecto):
    if proyecto.numerocolumnabumeizquierda + \
        proyecto.numerocolumnabusqueda + \
        proyecto.numerocolumnamenu + \
        proyecto.numerocolumnabumederecha >= 12:
        return True
    return False

def TfDoceColumnas(proyecto):
    if proyecto.numerocolumnamedioizquierda + \
        proyecto.numerocolumnamediocentro + \
        proyecto.numerocolumnamedioderecha >= 12:
        return True
    return False

from .forms import WizzardForm

class WizzardView(FormView):
    template_name = "crear/wizzard.html"
    form_class = WizzardForm

    def post(self, request, *args, **kwargs):
        operacion = self.request.POST['operacion']
        if operacion == 'insertar_proyecto':
            proyecto = Proyecto()
            nombre = self.request.POST['nombre']
            descripcion = self.request.POST['descripcion']
            proyecto.save()
        elif operacion == 'editar_proyecto':
            proyecto = Proyecto.objects.get(id=self.request.POST['codigo_id'])
            nombre = self.request.POST['nombre']
            descripcion = self.request.POST['descripcion']
            proyecto.save()
        elif operacion == 'borrar_proyecto':
            proyecto = Proyecto.objects.get(id=self.request.POST['codigo_id'])
            proyecto.delete()
        elif operacion == 'insertar_aplicacion':
            proyecto = Proyecto.objects.get(id=self.request.POST['codigo_id'])
            aplicacion = Aplicacion()
            nombre = self.request.POST['nombre']
            descripcion = self.request.POST['descripcion']
            aplicacion.nombre = nombre
            aplicacion.descripcion = descripcion
            aplicacion.proyecto = proyecto
            aplicacion.save()
        elif operacion == 'editar_aplicacion':
            aplicacion = Aplicacion.objects.get(id=self.request.POST['codigo_id'])
            nombre = self.request.POST['nombre']
            descripcion = self.request.POST['descripcion']
            aplicacion.save()
        elif operacion == 'borrar_aplicacion':
            aplicacion = Aplicacion.objects.get(id=self.request.POST['codigo_id'])
            aplicacion.delete()        
        elif operacion == 'insertar_modelo':
            aplicacion = Aplicacion.objects.get(id=self.request.POST['codigo_id'])
            modelo = Modelo()
            nombre = self.request.POST['nombre']
            descripcion = self.request.POST['descripcion']
            nombreself = self.request.POST['nombreself']
            nombreborrar = self.request.POST['nombreborrar']
            modelo.nombre = nombre
            modelo.descripcion = descripcion
            modelo.descripcion = descripcion
            modelo.nombreself = nombreself
            modelo. nombreborrar = nombreborrar
            modelo.proyecto = aplicacion.proyecto
            modelo.aplicacion = aplicacion
            modelo.save()
        elif operacion == 'editar_modelo':
            modelo = Modelo.objects.get(id=self.request.POST['codigo_id'])
            nombre = self.request.POST['nombre']
            descripcion = self.request.POST['descripcion']
            nombreself = self.request.POST['nombreself']
            nombreborrar = self.request.POST['nombreborrar']
            modelo.nombre = nombre
            modelo.descripcion = descripcion
            modelo.descripcion = descripcion
            modelo.nombreself = nombreself
            modelo. nombreborrar = nombreborrar
            modelo.save()
        elif operacion == 'borrar_modelo':
            modelo = Modelo.objects.get(id=self.request.POST['codigo_id'])
            modelo.delete()
        elif operacion == 'insertar_propiedad':
            modelo = Modelo.objects.get(id=self.request.POST['codigo_id'])
            nombre = self.request.POST['nombre']
            descripcion = self.request.POST['descripcion']
            foranea = self.request.POST['foranea']
            textobotones = self.request.POST['textobotones']
            tipo = self.request.POST['tipo']
            propiedad = Propiedad()
            propiedad.nombre = nombre
            propiedad.descripcion = descripcion
            propiedad.textobotones = textobotones
            propiedad.tipo = tipo
            propiedad.foranea = foranea
            propiedad.modelo = modelo
            propiedad.save()
        elif operacion == 'editar_propiedad':
            propiedad = Propiedad.objects.get(id=self.request.POST['codigo_id'])
            nombre = self.request.POST['nombre']
            descripcion = self.request.POST['descripcion']
            foranea = self.request.POST['foranea']
            textobotones = self.request.POST['textobotones']
            tipo = self.request.POST['tipo']
            propiedad.nombre = nombre
            propiedad.descripcion = descripcion
            propiedad.textobotones = textobotones
            propiedad.tipo = tipo
            propiedad.foranea = foranea
            propiedad.save()
        elif operacion == 'borrar_propiedad':
            propiedad = Propiedad.objects.get(id=self.request.POST['codigo_id'])
            propiedad.delete()
        elif operacion == 'insertar_regla':
            propiedad = Propiedad.objects.get(id=self.request.POST['codigo_id'])
            mensaje = self.request.POST['mensaje']
            codigo = self.request.POST['codigo']
            regla = Regla()
            regla.mensaje = mensaje
            regla.codigo = codigo
            regla.propiedad = propiedad
            regla.save() 
        elif operacion == 'editar_regla':
            regla = Regla.objects.get(id=self.request.POST['codigo_id'])
            mensaje = self.request.POST['mensaje']
            codigo = self.request.POST['codigo']
            regla.mensaje = mensaje
            regla.codigo = codigo
            regla.save() 
        elif operacion == 'borrar_regla':
            regla = Regla.objects.get(id=self.request.POST['codigo_id'])
            regla.delete()

        return self.get(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = super(WizzardView,self).get_form()
        return form
        
    def get_context_data(self,**kwargs):
        context = super(WizzardView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['error'] = ''

        try:
            if self.request.GET['proyecto_id'] == '':
                # Se ingresa un proyecto
                context['operacion'] = 'insertar_proyecto'
                pass
            else:
                # Se edita un proyecto
                proyecto = Proyecto.objects.get(usuario = self.request.user, id = self.request.GET['proyecto_id'])
                # Ve si se ingresa una nueva aplicacion
                context['operacion'] = 'editar_proyecto'
                     
        except:
            # context['error'] = e
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context