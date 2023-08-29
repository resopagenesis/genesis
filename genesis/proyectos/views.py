from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
# from django.shortcuts import render_to_response
from .models import Proyecto,Crear,LicenciaUso, ProyectoTexto, ProyectoJson, ProyectoObjeto
from principal.models import Seccion, Fila, Columna
from modelos.models import Seccion as Sec, Fila as Fil, Columna as Col
from .models import Seccion as Secp, Fila as Filp, Columna as Colp
from personalizacion.models import Personaliza
from modelos.models import ZonaReporte
from aplicaciones.models import Aplicacion
from crear.models import ErroresCreacion, ReporteNuevo
from .forms import ProyectoForm, ProyectoTextoForm, ProyectoObjetoForm
from core.models import Genesis, Precio
from crear import views
import crear.rutinas as rutinas
from django.utils import timezone
import datetime
from registration.views import VerificaVigenciaUsuario
import json, pickle
from .forms import SeccionForm, FilaForm, ColumnaForm
import time
import random
from django.core.serializers import serialize, deserialize

# Create your views here.
class ListaProyectosView(ListView):
    model = Proyecto
    # def get(self, request, *args, **kwargs):
    #     context = self.get_context_data()
    #     try:
    #         lista = ListaProyectos(self.request.GET['textob'], request.user)
    #     except:
    #         lista = ListaProyectos(None, request.user)

    #     context['lista_proyectos'] = lista
    #     return render_to_response('proyectos/proyecto_list.html', context) 

    def get_context_data(self, **kwargs):
        context = super(ListaProyectosView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['lista_proyectos'] = ListaProyectos(self.request.GET['criterio'],self.request.user)
        context['criterio'] = self.request.GET['criterio']
        if self.request.GET['duplica'] == '1':
            proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'])
            # DUPLICO EL PROYECTO
            pd = copy.deepcopy(proyecto)
            pd.id = None
            pd.save()
            # DUPLICA APLICACIONES
            for aplicacion in Aplicacion.objects.filter(proyecto=proyecto):
                apn = copy.deepcopy(aplicacion)
                apn.proyecto = pd
                apn.id = None
                apn.save()
                for modelo in Modelo.objects.filter(proyecto=proyecto,aplicacion=aplicacion):
                    mon = copy.deepcopy(modelo)
                    mon.proyecto = pd
                    mon.aplicacion = apn
                    mon.id = None
                    mon.save()
                    for propiedad in Propiedad.objects.filter(modelo=modelo):
                        prn = copy.deepcopy(propiedad)
                        prn.modelo = mon
                        prn.id = None
                        prn.save()
                        for regla in Regla.objects.filter(propiedad=propiedad):
                            rgn = copy.deepcopy(regla)
                            rgn.propiedad = prn
                            rgn.id = None
                            rgn.save()



        # lista =[]
        # tel = Proyecto.objects.filter(usuario=self.request.user)
        # for te in tel:
        #     lista.append([te.topico.upper(),te.descripcion,str(te.correlativo) + '.',te.diagrama,'e',te.id])
        #     tdl = TutorialDetalle.objects.filter(tutorialencabezado = te)
        #     for td in tdl:
        #         lista.append([string.capwords(td.topico.lower()),td.descripcion,str(te.correlativo) + '.' + str(td.correlativo) + '.',td.diagrama,'d',td.id])
        # context['lista'] = lista
        # tutorial = self.request.GET['video']
        # if tutorial != '':
        #     context['video'] = 'video.mp4'
        # return context              
        # context['lista_proyectos'] = lista_proyectos
        return context

    # def get_success_url(self):
    #     return reverse_lazy('proyectos:lista') + '?criterio=' + self.request.POST['textob']

    # def post(self,request,*args,**kwargs):
    #     return HttpResponseRedirect(self.get_success_url())

# Devuelve la lista de proyectos despues de analizar criterio
import copy

class ArbolProyectoView(ListView):
    model = Proyecto
    inicio = time.time()
    template_name = 'proyectos/arbol_proyecto.html'
    fin = time.time()
    # template_name = 'proyectos/arbol_drag_drop.html'

    def get_context_data(self, **kwargs):
        context = super(ArbolProyectoView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        numre = 0
        try:
            if self.request.GET['despliegueexpedito'] == '1':
                proyecto = Proyecto.objects.get(usuario = self.request.user, id = self.request.GET['proyecto_id'])
                self.request.session[str(proyecto.id)] = True
        except:
            pass
        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(usuario = self.request.user, id = self.request.GET['proyecto_id'])
            # Recibe datos del reporte de un modelo
            # try:
            #     proyecto_json = self.request.GET['json']
            #     modeloid = self.request.GET['modelo_id']
            #     user = self.request.user
            #     if self.request.GET['nuevo'] == "1":
            #         modelo = ZonaReporte()
            #         modelo.texto =  proyecto_json
            #         modelo.modeloid = modeloid
            #         modelo.save()
            #     if self.request.GET['nuevo'] == "0":
            #         modelo = ZonaReporte.objects.get(modeloid=modeloid)
            #         modelo.texto =  proyecto_json
            #         # texto_json = json.loads(texto_procesar.texto)['propiedades']
            #         modelo.save()            
            # except Exception as e:
            #     print(str(e))
            # Maneja arriba abajo
            try:
                if self.request.GET['modeloarriba'] == '1':
                    # recuperar el modelo a mover
                    modelo = Modelo.objects.get(id=self.request.GET['modelo_id'])
                    # leer los modelos en orden inverso
                    lista = Modelo.objects.filter(proyecto=proyecto,padre='nada').order_by('ordengeneracion')
                    # construir una lista con los campos ordengeneracion
                    i = 0
                    for it in lista:
                        if it.id == modelo.id:
                            ma = Modelo.objects.get(id=it.id)
                            mp = Modelo.objects.get(id=lista[i-1].id)
                            tp = mp.ordengeneracion
                            up = mp.ultimoregistro
                            ta = ma.ordengeneracion
                            ua = ma.ultimoregistro
                            ma.ordengeneracion = tp
                            ma.ultimoregistro = up
                            ma.save()
                            mp.ultimoregistro = ua
                            mp.ordengeneracion = ta
                            mp.save()
                        i+=1   
                    rutinas.CambiaOrdenGeneracion(proyecto)                         
                    rutinas.DesplegarArbol(True,proyecto.id,self.request)
            except:
                pass

            try:
                if self.request.GET['modeloabajo'] == '1':
                    # recuperar el modelo a mover
                    modelo = Modelo.objects.get(id=self.request.GET['modelo_id'])
                    # leer los modelos en orden inverso
                    lista = Modelo.objects.filter(proyecto=proyecto,padre='nada').order_by('ordengeneracion')
                    # construir una lista con los campos ordengeneracion
                    i = 0
                    for it in lista:
                        if it.id == modelo.id:
                            ma = Modelo.objects.get(id=it.id)
                            mp = Modelo.objects.get(id=lista[i+1].id)
                            tp = mp.ordengeneracion
                            up = mp.ultimoregistro
                            ta = ma.ordengeneracion
                            ua = ma.ultimoregistro
                            ma.ordengeneracion = tp
                            ma.ultimoregistro = up
                            ma.save()
                            mp.ordengeneracion = ta
                            mp.ultimoregistro = ua
                            mp.save()
                        i+=1                            
                    rutinas.CambiaOrdenGeneracion(proyecto)                         
                    rutinas.DesplegarArbol(True,proyecto.id,self.request)
            except:
                pass

            context['proyecto'] = proyecto
            context['proyecto_id'] = proyecto.id
            context['lista_aplicaciones'] = Aplicacion.objects.filter(proyecto = proyecto).order_by('ordengeneracion')
            context['lista_reportes'] = ReporteNuevo.objects.all()
            try:
                if self.request.GET['haciatexto'] == '1':
                    # Procesa hacia texto
                    # Borrar el anterior
                    ProyectoTexto.objects.filter(proyecto=proyecto.id).delete()
                    # Comienza con el proyecto
                    size  = 12
                    sizetexto = 14
                    sizetitulo = 18
                    ident = 20
                    ident_aplicacion = 30
                    ident_modelo = 40
                    ident_propiedad = 50
                    ident_regla = 60
                    texto = '<p style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetitulo) + 'px"><strong><u>Nombre del proyecto:</u></strong></span></p>'
                    texto += '<p style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">[npr ' + proyecto.nombre + ']</span></p>'
                    texto += '<p style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px"><strong><u>Descripcion:</u></strong></span></p>'
                    texto += '<p style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">[dpr ' + proyecto.descripcion + ']</span></p>'
                    numre=1
                    # Seguridad, personalizacion, busqueda
                    texto += '<p style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px"><strong><u>Seguridad, Personalizacion, Busqueda</u></strong></span></p>'
                    textov = 'Este proyecto @seguridad definida la opcion de seguridad @pcs, @personaliza las etiquetas de personalizacion @pce, @busqueda una opcion de busqueda general @pcb.' 

                    if proyecto.conseguridad:
                        textov = textov.replace('@seguridad','tiene')
                        textov = textov.replace('@pcs','[pcs]')
                    else:
                        textov = textov.replace('@seguridad','no tiene')
                        textov = textov.replace('@pcs','')

                    if proyecto.conetiquetaspersonalizacion:
                        textov = textov.replace('@personaliza','incluye')
                        textov = textov.replace('@pce','[pce]')
                    else:
                        textov = textov.replace('@personaliza','no incluye')
                        textov = textov.replace('@pce','')

                    if proyecto.conbusqueda:
                        textov = textov.replace('@busqueda','tiene')
                        textov = textov.replace('@pcb','[pcb]')
                    else:
                        textov = textov.replace('@busqueda','no tiene')
                        textov = textov.replace('@pcb','')
                    numre=2

                    texto += '<p style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + textov + '</span></p>'

                    # Caracteristicas graficas
                    texto += '<p style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px"><strong><u>Caracteristicas graficas</u></strong></span></p>'
                    texto += '<ul>'
                    texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">El proyecto tienen una separacion entre seciones de ' + '[ses ' + str(proyecto.separacionsecciones) + '] en formato Bootstrap</span></li>'

                    # Texto del titulo
                    if proyecto.titulo != '':
                        textov = 'El proyecto esta identificado en la pagina por el texto del titulo [tit ' + proyecto.titulo + '] cuyo color es: [cti ' + proyecto.colortitulo +']. El font del titulo es: [fti ' + proyecto.fonttitulo + '] y se encuentra alineado horizontalmente @horizontal [jht ' + proyecto.justificacionhorizontaltitulo +'] y verticalmente en la parte @vertical [jvt ' + proyecto.justificacionverticaltitulo +']'
                        
                        if proyecto.justificacionhorizontaltitulo == 'i':
                            textov = textov.replace('@horizontal', 'a la izquierda')
                        elif proyecto.justificacionhorizontaltitulo == 'd':
                            textov = textov.replace('@horizontal', 'a la derecha')
                        else:
                            textov = textov.replace('@horizontal', 'al centro')

                        if proyecto.justificacionverticaltitulo == 's':
                            textov = textov.replace('@vertical', 'superior')
                        elif proyecto.justificacionhorizontaltitulo == 'i':
                            textov = textov.replace('@vertical', 'inferior')
                        else:
                            textov = textov.replace('@vertical', 'central')

                        texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + textov + '</span></li>'

                    # Imagen de titulo
                    textov ='Si el proyecto tuviera una imagen que estuviera en lugar del titulo, esta tendria [itw ' + str(proyecto.imagentitulowidth) + '] pixels en su dimension horizontal y [ith ' + str(proyecto.imagentituloheight) + '] pixels en su dimension vertical y estaria alineado horizontalmente @horizontal [jht ' + proyecto.justificacionhorizontaltitulo + '] y verticalmente en la parte @vertical [jvt ' + proyecto.justificacionverticaltitulo +'].'

                    if proyecto.justificacionhorizontaltitulo == 'i':
                        textov = textov.replace('@horizontal', 'a la izquierda')
                    elif proyecto.justificacionhorizontaltitulo == 'd':
                        textov = textov.replace('@horizontal', 'a la derecha')
                    else:
                        textov = textov.replace('@horizontal', 'al centro')
                    numre=3

                    if proyecto.justificacionverticaltitulo == 's':
                        textov = textov.replace('@vertical', 'superior')
                    elif proyecto.justificacionhorizontaltitulo == 'i':
                        textov = textov.replace('@vertical', 'inferior')
                    else:
                        textov = textov.replace('@vertical', 'central')
                    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">' + textov + '</span></li>'

                    # Logo del proyecto
                    textov = 'Si se define un logo para el proyecto tendria [avw ' + str(proyecto.avatarwidth) +'] pixels en su dimension vertical y [avh ' + str(proyecto.avatarheight) +'] pixels en su dimension horizontal y se colocaria @horizontal [jhl ' + proyecto.justificacionhorizontallogo + '] horizontalmente y en la parte @vertical [jvl ' + proyecto.justificacionverticallogo + '] verticalmente.'
                    if proyecto.justificacionhorizontallogo == 'i':
                        textov = textov.replace('@horizontal', 'a la izquierda')
                    elif proyecto.justificacionhorizontallogo == 'd':
                        textov = textov.replace('@horizontal', 'a la derecha')
                    else:
                        textov = textov.replace('@horizontal', 'al centro')
                    if proyecto.justificacionverticallogo == 's':
                        textov = textov.replace('@vertical', 'superior')
                    elif proyecto.justificacionverticallogo == 'i':
                        textov = textov.replace('@vertical', 'inferior')
                    else:
                        textov = textov.replace('@vertical', 'central')
                    texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + textov + '</span></li>'
                    numre=4

                    # menu
                    textov = 'El menu del proyecto tiene un font [fme ' + proyecto.fontmenu + '] con un color [cme ' + proyecto.colormenu + '] y esta ubicado horizontalmente @horizontal [jum ' + proyecto.justificacionmenu +']'
                    if proyecto.justificacionmenu == 'i':
                        textov = textov.replace('@horizontal', 'a la izquierda')
                    elif proyecto.justificacionmenu == 'd':
                        textov = textov.replace('@horizontal', 'a la derecha')
                    else:
                        textov = textov.replace('@horizontal', 'al centro')
                    numre=41

                    texto += '<li style="margin-left:' + str(ident) + 'px""><span style="font-size:' + str(sizetexto) + 'px">' + textov + '</span></li>'

                    # Volver
                    textov = 'El menu del proyecto tiene un font [ftxv ' + proyecto.fonttextovolver + '] para la opcion volver,  con un color [ctxv ' + proyecto.colortextovolver + '] y el texto es [txv ' + proyecto.textovolver +']'
                    texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + textov + '</span></li>'

                    texto += '</ul>'
                    numre=51

                    if 1 == 2:
                        # Personalizacion
                        texto += '<p style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px"><strong><u>PERSONALIZACION</u></strong></span></p>'
                        for perso in Personaliza.objects.filter(proyecto=proyecto):
                            texto += '<ul style="margin-left:' + str(ident) + 'px">'
                            texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + str(perso.usuario.id) + '</span></li>'
                            texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + str(perso.proyecto.id) + '</span></li>'
                            texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + perso.aplicacion + '</span></li>'
                            texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + perso.archivo + '</span></li>'
                            texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + perso.tag + '</span></li>'
                            texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + perso.archivo + '</span></li>'
                            texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + perso.codigo + '</span></li>'
                            texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + str(perso.modificatags) + '</span></li>'
                            texto += '</ul style="margin-left:' + str(ident) + 'px">'

                    # Secciones
                    numre=5
                    if 1 == 2:
                        for seccion in Seccion.objects.filter(proyecto=proyecto):
                            texto += '<p style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px"><strong><u>SECCION</u></strong></span></p>'
                            texto += '<ul style="margin-left:' + str(ident) + 'px">'
                            texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + seccion.nombre + '</span></li>'
                            texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + str(seccion.proyecto.id) + '</span></li>'
                            texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + seccion.color1 + '</span></li>'
                            texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + seccion.color2 + '</span></li>'
                            texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + seccion.degradado + '</span></li>'
                            texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + str(seccion.borde) + '</span></li>'
                            texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + str(seccion.altura) + '</span></li>'
                            texto += '</ul style="margin-left:' + str(ident) + 'px">'
                            for fila in Fila.objects.filter(seccion=seccion):
                                texto += '<p style="margin-left:' + str(ident+10) + 'px"><span style="font-size:' + str(sizetexto) + 'px"><strong><u>FILA</u></strong></span></p>'
                                texto += '<ul style="margin-left:' + str(ident+10) + 'px">'
                                texto += '<li style="margin-left:' + str(ident+10) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + fila.nombre + '</span></li>'
                                texto += '<li style="margin-left:' + str(ident+10) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + str(fila.seccion.id) + '</span></li>'
                                texto += '<li style="margin-left:' + str(ident+10) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + str(fila.altura) + '</span></li>'
                                texto += '<li style="margin-left:' + str(ident+10) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + fila.color1 + '</span></li>'
                                texto += '<li style="margin-left:' + str(ident+10) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + fila.color2 + '</span></li>'
                                texto += '<li style="margin-left:' + str(ident+10) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + fila.degradado + '</span></li>'
                                texto += '<li style="margin-left:' + str(ident+10) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + str(fila.borde) + '</span></li>'
                                texto += '</ul style="margin-left:' + str(ident+10) + 'px">'

                                for columna in Columna.objects.filter(fila=fila):
                                    texto += '<p style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px"><strong><u>COLUMNA</u></strong></span></p>'
                                    texto += '<ul style="margin-left:' + str(ident+20) + 'px">'
                                    texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + columna.nombre + '</span></li>'
                                    texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + str(columna.fila.id) + '</span></li>'
                                    texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + columna.color1 + '</span></li>'
                                    texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + columna.color2 + '</span></li>'
                                    texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + columna.degradado + '</span></li>'
                                    if columna.imagen:
                                        texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + columna.imagen.url + '</span></li>'
                                    else:
                                        texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + '' + '</span></li>'
                                    texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + str(columna.secciones) + '</span></li>'
                                    texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + columna.textocolumna + '</span></li>'
                                    texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + columna.fonttexto + '</span></li>'
                                    texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + columna.colortexto + '</span></li>'
                                    texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + columna.justificacionhorizontaltexto + '</span></li>'
                                    texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + columna.justificacionverticaltexto + '</span></li>'
                                    texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + str(columna.borde) + '</span></li>'
                                    texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + str(columna.ingresosistema) + '</span></li>'
                                    texto += '</ul style="margin-left:' + str(ident+20) + 'px">'
                    ident += 10
                    numre=55

                    if Aplicacion.objects.filter(proyecto=proyecto).count() > 0:
                        texto += '<p style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetitulo-1) + 'px"><strong><u>APLICACIONES DEL PROYECTO</u></strong></span></p>'
                        # Recorre la aplicaciones
                        for app in Aplicacion.objects.filter(proyecto=proyecto):
                            if app.nombre != 'registration' and app.nombre != 'core':
                                texto += '<p style="margin-left:' + str(ident_aplicacion) + 'px"><span style="font-size:' + str(sizetexto) + 'px"><strong><u>Nombre de la aplicacion:</u></strong></span></p>'
                                texto += '<p style="margin-left:' + str(ident_aplicacion) + 'px"><span style="font-size:' + str(sizetexto) + 'px">[nap ' + app.nombre + ']</span></p>'
                                texto += '<p style="margin-left:' + str(ident_aplicacion) + 'px"><span style="font-size:' + str(sizetexto) + 'px"><strong><u>Descripcion:</u></strong></span></p>'
                                texto += '<p style="margin-left:' + str(ident_aplicacion) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + '[dap ' + app.descripcion + ']</span></p>'
                                numre=111

                                texto += '<p style="margin-left:' + str(ident_aplicacion) + 'px"><span style="font-size:' + str(sizetexto) + 'px"><strong><u>Caracteristicas graficas:</u></strong></span></p>'
                                texto += '<ul style="margin-left:' + str(ident_aplicacion) + 'px">'
                                texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">La aplicacion tiene el texto [txma @textomenu] para la opcion del menu</span></li>'
                                texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">La aplicacion despliega el tooltip [tta ' + app.tooltip + '] en la opcion del menu</span></li>'
                                texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">La aplicacion se genera en el orden [oga ' + str(app.ordengeneracion) + ']</span></li>'
                                texto += '</ul>'
                                numre=1111
                                if app.textoenmenu != '':
                                    texto = texto.replace('@textomenu',str(app.textoenmenu))
                                else:
                                    texto = texto.replace('@textomenu',app.nombre)
                                lista_modelos = Modelo.objects.filter(aplicacion = app, padre='nada').order_by('ordengeneracion') 
                                if lista_modelos.count() > 0:
                                    texto += '<p style="margin-left:' + str(ident_modelo) + 'px"><span style="font-size:' + str(sizetitulo-2) + 'px"><u><strong>MODELOS DE LA APLICACION : </strong>' + app.nombre + '</u></span></p>'
                                    for modelo_lista in lista_modelos:
                                        texto += '<p style="margin-left:' + str(ident_modelo) + 'px"><span style="font-size:' + str(sizetexto) + 'px"><strong><u>Nombre del modelo:</u></strong></span></p>'
                                        texto += '<p style="margin-left:' + str(ident_modelo) + 'px"><span style="font-size:' + str(sizetexto) + 'px">[nmo ' + modelo_lista.nombre + ']</span></p>'
                                        texto += '<p style="margin-left:' + str(ident_modelo) + 'px"><span style="font-size:' + str(sizetexto) + 'px"><strong><u>Descripcion:</u></strong></span></p>'
                                        texto += '<p style="margin-left:' + str(ident_modelo) + 'px"><span style="font-size:' + str(sizetexto) + 'px"><em>[dmo ' + modelo_lista.descripcion + ']</em></span></p>'                                      
                                        texto = CaracteristicasModelo(modelo_lista,texto,sizetexto,ident_modelo)
                                        lista_texto = []
                                        ReglasPropiedades(modelo_lista,lista_texto,ident_propiedad,sizetexto,sizetitulo-3)
                                        HaciaTextoRecursiva(proyecto,modelo_lista,lista_texto,sizetexto,ident_propiedad,sizetitulo-2)
                                        for strTexto in lista_texto:
                                            texto += strTexto
                    numre=66

                    proyecto_texto = ProyectoTexto()
                    proyecto_texto.usuario = self.request.user
                    proyecto_texto.titulo = proyecto.nombre
                    proyecto_texto.texto = texto
                    proyecto_texto.proyecto = proyecto.id
                    proyecto_texto.save()
                
            except Exception as e:     
                print('error ',str(numre) + str(e))
                # if not rutinas.CreaListaDespliegaArbol(proyecto.id,self.request):
                #     context['lista_crear'] = Crear.objects.filter(proyectoid=proyecto.id)
                # else:
                #     inicio = time.time()
                #     fi = time.strftime("%c")
                #     numer=1
                #     context['lista_crear'] = ListaCrear(proyecto.id,self.request)
                #     numer=2
                #     ff = time.strftime("%c")
                #     print('tiempo real ' ,time.time() - inicio,fi,ff)
                # Verifica si se despliegan datos del modelo

            try:
                if self.request.GET['abremodelo'] != '':
                    context['lista_crear'] = ListaCrear(proyecto.id,self.request,self.request.GET['abremodelo'])
                pass
            except:
                context['lista_crear'] = ListaCrear(proyecto.id,self.request,'0')
            context['tiene_errores'] = ErroresCreacion.objects.filter(proyecto = proyecto).count() >0
        except Exception as e:
            # context['error'] = e
            context['error'] = '!!! No eres el propietario del proyecto aun !!!' + str(e)
        
        return context

def CaracteristicasModelo(modelo,texto,sizetexto,ident):
    texto += '<p style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px"><strong><u>Caracteristicas de funcionamiento:</u></strong></span></p>'
    texto += '<ul style="margin-left:' + str(ident) + 'px">'
    if modelo.padre != 'nada':
        texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El modelo tiene como padre a: [pmo @padre]</span></li>'
        texto = texto.replace('@padre',modelo.padre)
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El modelo es identificado por: [pmo ' + modelo.nombreself + ']</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El registro de borrado es identificado por: [pmo ' + modelo.nombreborrar + ']</span></li>'
    texto += '</ul>'
    texto += '<p style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px"><strong><u>Caracteristicas graficas</u></strong></span></p>'
    texto += '<ul style="margin-left:' + str(ident) + 'px">'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El texto para la opcion del menu es: [tom ' + modelo.textoopcionmenu + ']</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El tooltip de la opcion del menu es: [ttm ' + modelo.tooltip + ']</span></li>'
    texto += '</ul>'

    # CARACTERISTICAS GENERALES
    texto += '<p style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px"><strong><u>Caracteristicas generales</u></strong></span></p>'
    texto += '<ul style="margin-left:' + str(ident) + 'px">'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El font de las etiquetas es: [flm ' + modelo.fontlabelmodelo + '], el color de las etiquetas es: [clm ' + modelo.colorlabelmodelo + ']</span></li>'
    if modelo.controlesautomaticos:
        texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">Los controles de los formularios se crean de forma automatica [cau]</span></li>'
    if modelo.registrounico:
        texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El modelo es de registro unico [rgu]</span></li>'
    if modelo.treeview:
        texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El modelo se edita en un TreeView [tvw]</span></li>'
        texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El color de fondo del TreeView es: [cftw]</span></li>'
        texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El color de listado del TreeView es: [cltw]</span></li>'
    if modelo.editarenlista:
        texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">la opcion editar aparece en la lista [opel]</span></li>'
    texto += '</ul>'

    # LISTA DE REGISTROS
    texto += '<p style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px"><strong><u>Caracteristicas de la lista de registros</u></strong></span></p>'
    texto += '<ul style="margin-left:' + str(ident) + 'px">'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El titulo de la lista de registros es: [tli ' + modelo.titulolista + '], tiene un font: [ftli ' + modelo.fonttitulolista + '], el color del titulo es: [ctli ' + modelo.colortitulolista + '] y tiene un fondo de color: [cftl ' + modelo.colorfondotitulolista + ']</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">La altura en (px) del titulo de la lista es: [atli ' + str(modelo.altotitulolista) + ']</span></li>'
    if modelo.mayusculastitulolista:
        texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El titulo de la lista esta en mayusculas [mtli]</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El titulo de la lista esta justificado verticalmente [jvtl ' + modelo.justificacionverticaltitulolista + ']</span></li>'
    if modelo.justificacionverticaltitulolista == 's':
        texto = texto.replace('@justv', 'arriba')
    if modelo.justificacionverticaltitulolista == 'i':
        texto = texto.replace('@justv', 'abajo')
    if modelo.justificacionverticaltitulolista == 'c':
        texto = texto.replace('@justv', 'al centro')
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El titulo de la lista esta justificado horizontalmente [jhtl ' + modelo.justificacionhorizontaltitulolista + ']</span></li>'
    if modelo.justificacionhorizontaltitulolista == 'i':
        texto = texto.replace('@justh', 'a la izquierda')
    if modelo.justificacionhorizontaltitulolista == 'd':
        texto = texto.replace('@justh', 'a la derecha')
    if modelo.justificacionhorizontaltitulolista == 'c':
        texto = texto.replace('@justh', 'al centro')
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El comentario del formulario de lista es: [cmli ' + modelo.comentariolista + '], tiene un font: [fcli ' + modelo.fontcomentariolista + '], el color del comentario es: [ccmli ' + modelo.colorcomentariolista + '] y tiene un fondo de color: [cfcml ' + modelo.colorfondocomentariolista + ']</span></li>'
    if modelo.mayusculascolumnas:
        texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">Las columnas de la lista estan en mayusculas [mco]</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">La altura en (px) de las columnas de la lista es: [aco ' + str(modelo.altocolumnas) + ']</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El texto de las columnas tiene un font: [ftli ' + modelo.fontcolumnaslista + '], el color del texto de las columnas es: [ccli ' + modelo.colorcolumnaslista + '] y tiene un fondo de color: [cfcl ' + modelo.colorfondocolumnaslista + ']</span></li>'
    if modelo.columnaslistaconborde:
        texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">Las columnas de la lista tienen borde [clcb]</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El texto del contenido de la lista tiene un font: [ftxl ' + modelo.fonttextolista + '], el color del fondo del texto de lalista es: [ctxl ' + modelo.colortextolista + '] y tiene un fondo de color: [cftxc ' + modelo.colorfondotextolista + ']</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El texto de las columnas para editar y borrar es: [teb ' + modelo.textoeditarborrar + '], tiene un font: [feb ' + modelo.fonteditarborrar + '], el color del texto es: [ceb ' + modelo.coloreditarborrar + ']</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El color para el link de nuevo modelo es: [clnm ' + modelo.colorbotonlinknuevomodelo + ']</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El texto para el link de nuevo modelo es: [tlnm ' + modelo.textolinknuevomodelo + ']</span></li>'
    texto += '</ul>'

    # MODELO NUEVO
    texto += '<p style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px"><strong><u>Caracteristicas del formulario de Modelo nuevo</u></strong></span></p>'
    texto += '<ul style="margin-left:' + str(ident) + 'px">'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El titulo del formulario de Modelo nuevo es: [tin ' + modelo.tituloinserta + '], tiene un font: [ftin ' + modelo.fonttituloinserta + '], el color del titulo es: [ctin ' + modelo.colortituloinserta + '], tiene un fondo de color: [cfti ' + modelo.colorfondotituloinserta + '] y tiene un fondo de color de la fila del titulo: [cffti ' + modelo.colorfondofilatituloinserta + ']</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">La altura en (px) del titulo del formulario Nuevo modelo es: [afti ' + str(modelo.altofilatituloinserta) + ']</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El titulo del formulario de Nuevo modelo esta justificado verticalmente [jvti @justv]</span></li>'
    if modelo.justificacionverticaltituloinserta == 's':
        texto = texto.replace('@justv', 'arriba')
    if modelo.justificacionverticaltituloinserta == 'i':
        texto = texto.replace('@justv', 'abajo')
    if modelo.justificacionverticaltituloinserta == 'c':
        texto = texto.replace('@justv', 'al centro')
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El titulo del formulario de Nuevo modelo esta justificado horizontalmente [jhti @justh]</span></li>'
    if modelo.justificacionhorizontaltituloinserta == 'i':
        texto = texto.replace('@justh', 'a la izquierda')
    if modelo.justificacionhorizontaltituloinserta == 'd':
        texto = texto.replace('@justh', 'a la derecha')
    if modelo.justificacionhorizontaltituloinserta == 'c':
        texto = texto.replace('@justh', 'al centro')
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El comentario del formulario de Nuevo modelo es: [cin ' + modelo.comentarioinserta + '], tiene un font: [fcin ' + modelo.fontcomentarioinserta + '], el color del comentario es: [ccin ' + modelo.colorcomentarioinserta + '] y tiene un fondo de color: [cfci ' + modelo.colorfondocomentarioinserta + ']</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">Numero de secciones del margen izquierdo: [ncii ' + str(modelo.numerocolumnasizquierdainserta) + ']</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">Numero de secciones del sector central: [ncmi ' + str(modelo.numerocolumnasmodeloinserta) + ']</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">Numero de secciones del margen derecho: [ncdi ' + str(modelo.numerocolumnasderechainserta) + ']</span></li>'
    texto += '</ul>'

    # EDITAR MODELO
    texto += '<p style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px"><strong><u>Caracteristicas del formulario de Edicion de modelo</u></strong></span></p>'
    texto += '<ul style="margin-left:' + str(ident) + 'px">'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El titulo del formulario de Edicion de modelo es: [tup ' + modelo.tituloupdate + '], tiene un font: [ftup ' + modelo.fonttituloupdate + '], el color del titulo es: [ctup ' + modelo.colortituloupdate + '], tiene un fondo de color: [cftu ' + modelo.colorfondotituloupdate + '] y tiene un fondo de color de la fila del titulo: [cfftu ' + modelo.colorfondofilatituloupdate + ']</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">La altura en (px) del titulo del formulario Edicion de modelo es: [aftu ' + str(modelo.altofilatituloupdate) + ']</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El titulo del formulario de Edicion de modelo esta justificado verticalmente [jvtu @justv]</span></li>'
    if modelo.justificacionverticaltituloupdate == 's':
        texto = texto.replace('@justv', 'arriba')
    if modelo.justificacionverticaltituloupdate == 'i':
        texto = texto.replace('@justv', 'abajo')
    if modelo.justificacionverticaltituloupdate == 'c':
        texto = texto.replace('@justv', 'al centro')
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El titulo del formulario de Edicion de modelo esta justificado horizontalmente [jhtu @justh]</span></li>'
    if modelo.justificacionhorizontaltituloupdate == 'i':
        texto = texto.replace('@justh', 'a la izquierda')
    if modelo.justificacionhorizontaltituloupdate == 'd':
        texto = texto.replace('@justh', 'a la derecha')
    if modelo.justificacionhorizontaltituloupdate == 'c':
        texto = texto.replace('@justh', 'al centro')
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El comentario del formulario de Edicion de modelo es: [cup ' + modelo.comentarioupdate + '], tiene un font: [fcup ' + modelo.fontcomentarioupdate + '], el color del comentario es: [ccup ' + modelo.colorcomentarioupdate + '] y tiene un fondo de color: [cfcu ' + modelo.colorfondocomentarioupdate + ']</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">Numero de secciones del margen izquierdo: [nciu ' + str(modelo.numerocolumnasizquierdaupdate) + ']</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">Numero de secciones del sector central: [ncmu ' + str(modelo.numerocolumnasmodeloupdate) + ']</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">Numero de secciones del margen derecho: [ncdu ' + str(modelo.numerocolumnasderechaupdate) + ']</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">Numero de secciones de edicion de hijos en caso de hijos contiguos: [nchu ' + str(modelo.numerocolumnashijosupdate) + ']</span></li>'
    if modelo.hijoscontiguos:
        texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">Los hijos del modelo son contiguos [hco]</span></li>'
    texto += '</ul>'

    # BORRAR MODELO
    texto += '<p style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px"><strong><u>Caracteristicas del formulario de Borrado de modelo</u></strong></span></p>'
    texto += '<ul style="margin-left:' + str(ident) + 'px">'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El titulo del formulario de Borrado de modelo es: [tbo ' + modelo.tituloborra + '], tiene un font: [ftbo ' + modelo.fonttituloborra + '], el color del titulo es: [ctb ' + modelo.colortituloborra + '], tiene un fondo de color: [cftb ' + modelo.colorfondotituloborra + '] y tiene un fondo de color de la fila del titulo: [cfftb ' + modelo.colorfondofilatituloborra + ']</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">La altura en (px) del titulo del formulario Borrado de modelo es: [aftb ' + str(modelo.altofilatituloborra) + ']</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El titulo del formulario de Borrado de modelo esta justificado verticalmente [jvtb @justv]</span></li>'
    if modelo.justificacionverticaltituloborra == 's':
        texto = texto.replace('@justv', 'arriba')
    if modelo.justificacionverticaltituloborra == 'i':
        texto = texto.replace('@justv', 'abajo')
    if modelo.justificacionverticaltituloborra == 'c':
        texto = texto.replace('@justv', 'al centro')
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El titulo del formulario de Borrado de modelo esta justificado horizontalmente [jhtb @justh]</span></li>'
    if modelo.justificacionhorizontaltituloborra == 'i':
        texto = texto.replace('@justh', 'a la izquierda')
    if modelo.justificacionhorizontaltituloborra == 'd':
        texto = texto.replace('@justh', 'a la derecha')
    if modelo.justificacionhorizontaltituloborra == 'c':
        texto = texto.replace('@justh', 'al centro')
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El comentario del formulario de Borrado de modelo es: [cbo ' + modelo.comentarioborra + '], tiene un font: [fcbo ' + modelo.fontcomentarioborra + '], el color del comentario es: [ccbo ' + modelo.colorcomentarioborra + '] y tiene un fondo de color: [cfcb ' + modelo.colorfondocomentarioborra + ']</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El texto para el borrado del modelo es: [txbo ' + modelo.textoborra + '], tiene un font: [ftxb ' + modelo.fonttextoborra + '], el color del texto para borrar es: [ctxb ' + modelo.colortextoborra + '] y tiene un fondo de color: [cftxb ' + modelo.colorfondotextoborra + ']</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">El texto para el boton de borrado es: [txbb ' + modelo.textobotonborra + ']</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">Numero de secciones del margen izquierdo: [ncib ' + str(modelo.numerocolumnasizquierdaborra) + ']</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">Numero de secciones del sector central: [ncmb ' + str(modelo.numerocolumnasmodeloborra) + ']</span></li>'
    texto += '<li style="margin-left: 20px;"><span style="font-size:' + str(sizetexto) + 'px">Numero de secciones del margen derecho: [ncdb ' + str(modelo.numerocolumnasderechaborra) + ']</span></li>'
    texto += '</ul>'

    if 1 == 2:
        # Secciones, filas, columnas
        for seccion in Sec.objects.filter(modelo=modelo):
            texto += '<p style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px"><strong><u>SECCION</u></strong></span></p>'
            texto += '<ul style="margin-left:' + str(ident) + 'px">'
            texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + seccion.nombre + '</span></li>'
            texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + str(seccion.modelo.id) + '</span></li>'
            texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + seccion.color1 + '</span></li>'
            texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + seccion.color2 + '</span></li>'
            texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + seccion.degradado + '</span></li>'
            texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + str(seccion.borde) + '</span></li>'
            texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + str(seccion.altura) + '</span></li>'
            if seccion.imagen:
                texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + seccion.imagen.url + '</span></li>'
            else:
                texto += '<li style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + '' + '</span></li>'
            texto += '</ul style="margin-left:' + str(ident) + 'px">'
            for fila in Fil.objects.filter(seccion=seccion):
                texto += '<p style="margin-left:' + str(ident+10) + 'px"><span style="font-size:' + str(sizetexto) + 'px"><strong><u>FILA</u></strong></span></p>'
                texto += '<ul style="margin-left:' + str(ident+10) + 'px">'
                texto += '<li style="margin-left:' + str(ident+10) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + fila.nombre + '</span></li>'
                texto += '<li style="margin-left:' + str(ident+10) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + str(fila.seccion.id) + '</span></li>'
                texto += '<li style="margin-left:' + str(ident+10) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + str(fila.altura) + '</span></li>'
                texto += '<li style="margin-left:' + str(ident+10) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + fila.color1 + '</span></li>'
                texto += '<li style="margin-left:' + str(ident+10) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + fila.color2 + '</span></li>'
                texto += '<li style="margin-left:' + str(ident+10) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + fila.degradado + '</span></li>'
                texto += '<li style="margin-left:' + str(ident+10) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + str(fila.borde) + '</span></li>'
                texto += '</ul style="margin-left:' + str(ident+10) + 'px">'
                for columna in Col.objects.filter(fila=fila):
                    texto += '<p style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px"><strong><u>COLUMNA</u></strong></span></p>'
                    texto += '<ul style="margin-left:' + str(ident+20) + 'px">'
                    texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + columna.nombre + '</span></li>'
                    texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + str(columna.fila.id) + '</span></li>'
                    texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + columna.color1 + '</span></li>'
                    texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + columna.color2 + '</span></li>'
                    texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + columna.degradado + '</span></li>'
                    if columna.imagen:
                        texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + columna.imagen.url + '</span></li>'
                    else:
                        texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + '' + '</span></li>'
                    texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + str(columna.secciones) + '</span></li>'
                    texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + columna.textocolumna + '</span></li>'
                    texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + columna.fonttexto + '</span></li>'
                    texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + columna.colortexto + '</span></li>'
                    texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + columna.justificacionhorizontaltexto + '</span></li>'
                    texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + columna.justificacionverticaltexto + '</span></li>'
                    texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + str(columna.borde) + '</span></li>'
                    texto += '<li style="margin-left:' + str(ident+20) + 'px"><span style="font-size:' + str(sizetexto) + 'px">' + columna.funcion + '</span></li>'
                    texto += '</ul style="margin-left:' + str(ident+20) + 'px">'

    return texto

def HaciaTextoRecursiva(proyecto,modelo,lista_texto,size,ident,sizetitulo):
    texto = ''
#     lista_texto.append('<p span style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(size) + 'px"><span style="color:#9b59b6"><strong>[nmo ' + modelo.nombre + ']</strong></span></p>')
#     lista_texto.append('<p span style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(size) + 'px"><strong>Descripcion: </strong>' + '<em>[dmo ' + modelo.descripcion + ']</em></span></p>')
#     modelos_modelo = Modelo.objects.filter(padre = modelo.nombre)
#     # Ve si tiene propiedades
#     propiedades_modelo = Propiedad.objects.filter(modelo=modelo)
#     if propiedades_modelo.count() > 0:
#         ident += 10
#         lista_texto.append('<p span style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(size) + 'px"><strong>Propiedades del Modelo :</strong>' + modelo.nombre + '</span></p>')
#         for propiedad_modelo in propiedades_modelo:
#             # size -= 1
#             lista_texto.append('<p span style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(size) + 'px"><strong>Nombre:</strong>[npro ' + propiedad_modelo.nombre + ']</span></p>')
#             lista_texto.append('<p span style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(size) + 'px"><strong>Descripcion:</strong>' + '<em>[dpro ' + propiedad_modelo.descripcion + ']</em></span></p>')

#             # Ve si tiene reglas
#             reglas_propiedad = Regla.objects.filter(propiedad=propiedad_modelo)
#             if reglas_propiedad.count() > 0:
#                 ident += 10
#                 lista_texto.append('<p><span style="font-size:' + str(size) + 'px"><strong>Reglas de la Propiedad : ' + propiedad_modelo.nombre + '</strong></span></p>')
#                 for regla_propiedad in reglas_propiedad:
#                     # size -= 1
#                     lista_texto.append('<p span style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(size) + 'px"><strong>Mensaje:</strong><em>' + regla_propiedad.mensaje + '</em></span></p>')
#                     lista_texto.append('<p span style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(size) + 'px"><strong>Codigo: </strong><em>[dpro ' + regla_propiedad.codigo + ']</em></span></p>')

# # if modelos_modelo.count() > 0:
# #     ident += 10
# #     lista_texto.append('<p span style="margin-left:' + str(ident) + 'px"><span style="font-size:16px"><strong>Modelos del Modelo: '+ modelo.nombre + '</strong></span></p>')

    for modelo_modelo in Modelo.objects.filter(padre = modelo.nombre):
        lista_texto.append('<p style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(size) + 'px"><strong><u>Modelo hijo de:' + modelo.nombre + '</u></strong></span></p>')
        lista_texto.append('<p style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(size) + 'px"><strong><u>Nombre del modelo:</u></strong></span></p>')
        lista_texto.append('<p span style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(size) + 'px"><strong>[nmo ' + modelo_modelo.nombre + ']</strong></span></p>')
        lista_texto.append('<p style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(size) + 'px"><strong><u>Descripcion:</u></strong></span></p>')
        lista_texto.append('<p span style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(size) + 'px"><strong>Descripcion: </strong>' + '<em>[dmo ' + modelo_modelo.descripcion + ']</em></span></p>')
        texto = ''
        texto = CaracteristicasModelo(modelo_modelo,texto,size,ident)        
        lista_texto.append(texto)
        ReglasPropiedades(modelo_modelo,lista_texto,ident+10,size,sizetitulo-1)
        HaciaTextoRecursiva(proyecto,modelo_modelo,lista_texto,size,ident,sizetitulo)

def ReglasPropiedades(modelo,lista_texto,ident,size,sizetitulo):
    propiedades_modelo = Propiedad.objects.filter(modelo=modelo)
    if propiedades_modelo.count() > 0:
        ident += 10
        lista_texto.append('<p span style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(sizetitulo) + 'px"><u><strong>PROPIEDADES DEL MODELO:</strong>' + modelo.nombre + '</u></span></p>')
        for propiedad_modelo in propiedades_modelo:
            # size -= 1
            lista_texto.append('<p style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(size) + 'px"><u><strong>Nombre de la propiedad:</strong></u></span></p>')
            lista_texto.append('<p style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(size) + 'px">[npro ' + propiedad_modelo.nombre + ']</span></p>')
            lista_texto.append('<p style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(size) + 'px"><u><strong>Descripcion:</strong></u></span></p>')
            lista_texto.append('<p style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(size) + 'px"><em>[dpro ' + propiedad_modelo.descripcion + ']</em></span></p>')

            lista_texto.append('<p style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(size) + 'px"><strong><u>Caracteristicas</u></strong></span></p>')
            lista_texto.append('<ul style="margin-left:' + str(ident) + 'px">')
            texto = '<li style="margin-left:' + str(ident) + 'px;"><span style="font-size:' + str(size) + 'px">La propiedad es de tipo: [tpro @tipo]</span></li>'
            if propiedad_modelo.tipo == 's':
                texto = texto.replace('@tipo','string')                
                lista_texto.append(texto)
                lista_texto.append('<li style="margin-left: 20px;"><span style="font-size:' + str(size) + 'px">La propiedad tiene una longitud de: [lst ' + str(propiedad_modelo.largostring) + '] caracteres</span></li>')
            if propiedad_modelo.tipo == 'x':
                texto = texto.replace('@tipo','Textfield')                
                lista_texto.append(texto)
            if propiedad_modelo.tipo == 'h':
                texto = texto.replace('@tipo','RichText')                
                lista_texto.append(texto)
            if propiedad_modelo.tipo == 'm':
                texto = texto.replace('@tipo','smallint')                
                lista_texto.append(texto)
            if propiedad_modelo.tipo == 'i':
                texto = texto.replace('@tipo','Integer')                
                lista_texto.append(texto)
            if propiedad_modelo.tipo == 'l':
                texto = texto.replace('@tipo','longinteger')                
                lista_texto.append(texto)
            if propiedad_modelo.tipo == 'd':
                texto = texto.replace('@tipo','decimal')                
                lista_texto.append(texto)
            if propiedad_modelo.tipo == 'f':
                texto = texto.replace('@tipo','foranea')                
                lista_texto.append(texto)
            if propiedad_modelo.tipo == 'n':
                texto = texto.replace('@tipo','date')                
                lista_texto.append('<li style="margin-left: 20px;"><span style="font-size:' + str(size) + 'px">El formato para despliegue de la propiedad es: [ffch ' + propiedad_modelo.formatofecha + ']</span></li>')
            if propiedad_modelo.tipo == 't':
                texto = texto.replace('@tipo','datetime')                
                lista_texto.append('<li style="margin-left: 20px;"><span style="font-size:' + str(size) + 'px">El formato para despliegue de la propiedad es: [ffch ' + propiedad_modelo.formatofecha + ']</span></li>')
            if propiedad_modelo.tipo == 'e':
                texto = texto.replace('@tipo','time')                
                lista_texto.append('<li style="margin-left: 20px;"><span style="font-size:' + str(size) + 'px">El formato para despliegue de la propiedad es: [ffch ' + propiedad_modelo.formatofecha + ']</span></li>')
            if propiedad_modelo.tipo == 'b':
                texto = texto.replace('@tipo','boolean')                
                lista_texto.append(texto)
                lista_texto.append('<li style="margin-left: 20px;"><span style="font-size:' + str(size) + 'px">El texto para los botones es: [txb ' + propiedad_modelo.textobotones + ']</span></li>')
            if propiedad_modelo.tipo == 'r':
                texto = texto.replace('@tipo','radiobutton')                
                lista_texto.append(texto)
            if propiedad_modelo.tipo == 'p':
                texto = texto.replace('@tipo','image')                
                lista_texto.append(texto)
            if propiedad_modelo.tipo == 'u':
                texto = texto.replace('@tipo','user')                
                lista_texto.append(texto)
            lista_texto.append('<li style="margin-left: 20px;"><span style="font-size:' + str(size) + 'px">El valor por default de la propiedad es: [vdf ' + propiedad_modelo.valorinicial + ']</span></li>')
            lista_texto.append('<li style="margin-left: 20px;"><span style="font-size:' + str(size) + 'px">El texto del placeholder es: [tph ' + propiedad_modelo.textoplaceholder + ']</span></li>')
            lista_texto.append('<li style="margin-left: 20px;"><span style="font-size:' + str(size) + 'px">La etiqueta en el formulario es: [epro ' + propiedad_modelo.etiqueta + ']</span></li>')
            if propiedad_modelo.enlista:
                lista_texto.append('<li style="margin-left: 20px;"><span style="font-size:' + str(size) + 'px">La propiedad se despliega en la lista [enl]</span></li>')
            if propiedad_modelo.enmobile:
                lista_texto.append('<li style="margin-left: 20px;"><span style="font-size:' + str(size) + 'px">La propiedad se adapta a mobiles [emb]</span></li>')
            lista_texto.append('<li style="margin-left: 20px;"><span style="font-size:' + str(size) + 'px">Numero de secciones de la propiedad en la columna: [ncl ' + str(propiedad_modelo.numerocolumnas) + ']</span></li>')
            lista_texto.append('<li style="margin-left: 20px;"><span style="font-size:' + str(size) + 'px">Texto de la columna en la lista del modelo: [txc ' + propiedad_modelo.textocolumna + ']</span></li>')
            texto = '<li style="margin-left: 20px;"><span style="font-size:' + str(size) + 'px">El texto en la columna de la lista esta justificado horizontalmente [jtxc @justv]</span></li>'
            if propiedad_modelo.justificaciontextocolumna == 'i':
                texto = texto.replace('@justh', 'a la izquierda')
                lista_texto.append(texto)
            if propiedad_modelo.justificaciontextocolumna == 'd':
                texto = texto.replace('@justh', 'a la derecha')
                lista_texto.append(texto)
            if propiedad_modelo.justificaciontextocolumna == 'c':
                texto = texto.replace('@justh', 'al centro')
                lista_texto.append(texto)
            if propiedad_modelo.etiquetaarriba:
                lista_texto.append('<li style="margin-left: 20px;"><span style="font-size:' + str(size) + 'px">La etiqueta se coloca arriba del control en el formulario [ear]</span></li>')
            if propiedad_modelo.noestaenformulario:
                lista_texto.append('<li style="margin-left: 20px;"><span style="font-size:' + str(size) + 'px">La propiedad no se despliega en el formulario [nef]</span></li>')
            if propiedad_modelo.participabusquedalista:
                lista_texto.append('<li style="margin-left: 20px;"><span style="font-size:' + str(size) + 'px">La propiedad participa en el criterio de busqueda de la lista [pbl]</span></li>')
            if propiedad_modelo.totaliza:
                lista_texto.append('<li style="margin-left: 20px;"><span style="font-size:' + str(size) + 'px">La propiedad se totaliza en la lista [tlz]</span></li>')
            if propiedad_modelo.enreporte:
                lista_texto.append('<li style="margin-left: 20px;"><span style="font-size:' + str(size) + 'px">La propiedad aparece en el reporte [enr]</span></li>')
                lista_texto.append('<li style="margin-left: 20px;"><span style="font-size:' + str(size) + 'px">El ancho en el reporte es: [anre ' + str(propiedad_modelo.anchoenreporte) + ']</span></li>')
            lista_texto.append('</ul>')

            # Ve si tiene reglas
            reglas_propiedad = Regla.objects.filter(propiedad=propiedad_modelo)
            if reglas_propiedad.count() > 0:
                ident += 10
                lista_texto.append('<p><span style="font-size:' + str(size) + 'px"><strong>Reglas de la Propiedad : ' + propiedad_modelo.nombre + '</strong></span></p>')
                for regla_propiedad in reglas_propiedad:
                    # size -= 1
                    lista_texto.append('<p span style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(size) + 'px"><strong>Mensaje:</strong><em>' + regla_propiedad.mensaje + '</em></span></p>')
                    lista_texto.append('<p span style="margin-left:' + str(ident) + 'px"><span style="font-size:' + str(size) + 'px"><strong>Codigo: </strong><em>[dpro ' + regla_propiedad.codigo + ']</em></span></p>')

class WizzardArbolProyectoView(ListView):
    model = Proyecto
    inicio = time.time()
    template_name = 'proyectos/wizzardarbol_proyecto.html'

    def get_context_data(self, **kwargs):
        context = super(WizzardArbolProyectoView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        num=0
        try:
            context['error'] = ''
            num=1
            proyecto = Proyecto.objects.get(usuario = self.request.user, id = self.request.GET['proyecto_id'])
            # Maneja arriba abajo
            try:
                if self.request.GET['modeloarriba'] == '1':
                    ArribaAbajo(True,self.request.GET['modelo_id'],proyecto)
            except:
                pass

            try:
                if self.request.GET['modeloabajo'] == '1':
                    ArribaAbajo(False,self.request.GET['modelo_id'],proyecto)
            except:
                pass

            context['proyecto'] = proyecto
            context['proyecto_id'] = proyecto.id
            context['lista_aplicaciones'] = Aplicacion.objects.filter(proyecto = proyecto).order_by('ordengeneracion')
            context['lista_reportes'] = ReporteNuevo.objects.all()
            # Ver si se hizo click en una aplicacion
            try:
                self.request.session['aplicacionid'] = self.request.GET['aplicacion_id']
                context['aplicacionid'] = int(self.request.GET['aplicacion_id'])
            except:
                self.request.session['aplicacionid'] = 0
                context['aplicacionid'] = 0
            num=5
            # Ver si se hizo click en un modelo
            try:
                self.request.session['modeloid'] = self.request.GET['modelo_id']
                context['modeloid'] = int(self.request.GET['modelo_id'])
            except:
                self.request.session['modeloid'] = 0
                context['modeloid'] = 0
            # Ver si debe recalcular la lista
            if not rutinas.CreaListaDespliegaArbol(proyecto.id):
                context['lista_crear'] = Crear.objects.filter(proyectoid=proyecto.id)
            else:
                context['lista_crear'] = ListaCrear(proyecto.id,self.request,'')
            try:
                if self.request.GET['nueva'] == 'nueva_aplicacion':
                    # Crear el random para la aplicacion
                    igual = True
                    while igual:
                        num = random.randint(1, 1000)
                        if Aplicacion.objects.filter(nombre='aplicacion_'+str(num),proyecto=proyecto).count() == 0:
                            igual=False

                    # insertar una nueva aplicacion
                    aplicacion = Aplicacion()
                    aplicacion.nombre = 'aplicacion_' + str(num)
                    aplicacion.proyecto = proyecto
                    aplicacion.save() 
                    rutinas.DesplegarArbol(True, proyecto.id,self.request)
            except:
                pass
            num=4
            try:
                if self.request.GET['nueva'] == 'nuevo_modelo':
                    if int(self.request.session.get('aplicacionid')) > 0:
                        # ver si se eligio una aplicacion
                        app=None
                        app = Aplicacion.objects.get(id=self.request.session.get('aplicacionid'))
                        # Crear el random para el modelo
                        igual = True
                        while igual:
                            num = random.randint(1, 1000)
                            if Modelo.objects.filter(nombre='modelo_'+str(num),proyecto=proyecto).count() == 0:
                                igual=False
                        # insertar un nuevo modelo
                        modelo = Modelo()
                        modelo.nombre = 'modelo_' + str(num)
                        modelo.proyecto = proyecto
                        modelo.aplicacion = app
                        modelo.save()
                        rutinas.DesplegarArbol(True, proyecto.id,self.request,self.request)
            except:
                pass

            try:
                if self.request.GET['nueva'] == 'nueva_propiedad':
                    if self.request.session.get('modeloid') > 0:
                        # identificar el modelo
                        modelo = Modelo.objects.get(id=self.request.get('modeloid'))
                        # extraer el ultimo numero correlativo
                        igual = True
                        while igual:
                            num = random.randint(1, 1000)
                            if Propiedad.objects.filter(nombre='propiedad_'+str(num),modelo=modelo).count() == 0:
                                igual=False
                        propiedad = Propiedad()
                        propiedad.nombre = 'propiedad_' + str(num)
                        # insertar una nueva propiedad
                        if self.request.GET['string']:
                            propiedad.tipo = 's'
                        if self.request.GET['boolean']:
                            propiedad.tipo = 'b'
                        if self.request.GET['decimal']:
                            propiedad.tipo = 'd'
                        if self.request.GET['hora']:
                            propiedad.tipo = 'e'
                        if self.request.GET['foranea']:
                            propiedad.tipo = 'f'
                            if self.request.GET['foranea'] != '':
                                propiedad.foranea = self.request.GET['foranea']
                            else:
                                propiedad.tipo = 's'
                        if self.request.GET['richtext']:
                            propiedad.tipo = 'h'
                        if self.request.GET['entero']:
                            propiedad.tipo = 'i'
                        if self.request.GET['enterolargo']:
                            propiedad.tipo = 'l'
                        if self.request.GET['fecha']:
                            propiedad.tipo = 'n'
                        if self.request.GET['imagen']:
                            propiedad.tipo = 'p'
                        if self.request.GET['radiobutton']:
                            propiedad.tipo = 'r'
                            propiedad.textobotones = 'o1,opcion 1;o2,opcion 2'
                        if self.request.GET['horafecha']:
                            propiedad.tipo = 't'
                        if self.request.GET['usuario']:
                            propiedad.tipo = 'u'
                        if self.request.GET['textfield']:
                            propiedad.tipo = 'x'
                        propiedad.save()
                        rutinas.DesplegarArbol(True, proyecto.id,self.request)
            except:
                pass
            
        except Exception as e:
            # context['error'] = e
            context['error'] = '!!! No eres el propietario del proyecto !!!' + str(e) + str(num)
        return context

def ArribaAbajo(arriba,id,proyecto):
    if arriba:
        # recuperar el modelo a mover
        modelo = Modelo.objects.get(id=id)
        # leer los modelos en orden inverso
        lista = Modelo.objects.filter(proyecto=proyecto,padre='nada').order_by('ordengeneracion')
        # construir una lista con los campos ordengeneracion
        i = 0
        for it in lista:
            if it.id == modelo.id:
                ma = Modelo.objects.get(id=it.id)
                mp = Modelo.objects.get(id=lista[i-1].id)
                tp = mp.ordengeneracion
                ta = ma.ordengeneracion
                ma.ordengeneracion = tp
                ma.save()
                mp.ordengeneracion = ta
                mp.save()
            i+=1                            
    else:
        # recuperar el modelo a mover
        modelo = Modelo.objects.get(id=id)
        # leer los modelos en orden inverso
        lista = Modelo.objects.filter(proyecto=proyecto,padre='nada').order_by('ordengeneracion')
        # construir una lista con los campos ordengeneracion
        i = 0
        for it in lista:
            if it.id == modelo.id:
                ma = Modelo.objects.get(id=it.id)
                mp = Modelo.objects.get(id=lista[i+1].id)
                tp = mp.ordengeneracion
                ta = ma.ordengeneracion
                ma.ordengeneracion = tp
                ma.save()
                mp.ordengeneracion = ta
                mp.save()
            i+=1                            

class CrearProyectoView(CreateView):
    model = Proyecto
    form_class = ProyectoForm

    def get_success_url(self):
        # return reverse_lazy('proyectos:home')
        return reverse_lazy('proyectos:lista') + '?criterio=' + '&duplica=0'

    def get_context_data(self,**kwargs):
        context = super(CrearProyectoView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['criterio'] = self.request.GET['criterio']
        context['error'] = ''
        # rutinas.DesplegarArbol(False, self.object.id )
        return context

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST,request.FILES)
        user = request.user
        if user.id == None:
            return render(request, 'proyectos/proyecto_form.html', {'form': form})
        else:
            if form.is_valid():
                proyecto = form.save(commit=False)
                proyecto.usuario = user
                proyecto.save()
                rutinas.CrearSeccionPrincipal(proyecto)
                rutinas.CrearSeccionProyecto(None,proyecto)
                rutinas.CambiaOrdenGeneracion(proyecto)
                rutinas.DesplegarArbol(True, proyecto.id,request)
                return HttpResponseRedirect(self.get_success_url())
            return render(request, 'proyectos/proyecto_form.html', {'form': form})

class EditarProyectoView(UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        # proyecto = self.object
        # proyecto.save()
        try:
            if self.request.GET['wizzard'] == '1':
                return reverse_lazy('proyectos:wizzard_arbol') + '?ok&proyecto_id=' + str(self.object.id)
        except:
            return reverse_lazy('proyectos:editar', args=[self.object.id]) + '?ok'

    def get_context_data(self,**kwargs):
        context = super(EditarProyectoView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        num=1
        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(id=self.object.id,usuario=self.request.user)
            context['proyecto'] = proyecto
            num=2
            # Datos para los fonts
            try:
                context['font_titulo'] = [proyecto.fonttitulo.split(',')[0],proyecto.fonttitulo.split(',')[1],proyecto.fonttitulo.split(',')[2]]
            except:
                context['font_titulo'] = ['Arial',10,500]
            num=3
        except Exception as e:
            context['error'] = str(e) + str(num)
            # context['error'] = "!! No eres el propietario del proyecto !!!"
        # rutinas.DesplegarArbol(False, self.object.id )
        return context

    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        form = self.get_form()
        form.save()
        rutinas.DesplegarArbol(True, self.object.id,request)
        return HttpResponseRedirect(self.get_success_url())

def RecursivoReporte(lista,modelo,nivel,proyecto,pospadre,strpp='',strsp='',strh = ''):
    strpp = 'primera parte ' + modelo.nombre
    lista.append(strpp)
    for mod in Modelo.objects.filter(padre=modelo,proyecto=proyecto):
        RecursivoReporte(lista,mod,nivel+1,proyecto,pospadre,strpp,strsp,strh)
    strsp = 'segunda parte ' + modelo.nombre
    lista.append(strsp)

class BorrarProyectoView(DeleteView):
    model = Proyecto
    # success_url = reverse_lazy('proyectos:lista')

    def get_success_url(self):
        try:
            if self.request.GET['borra'] == '0':
                rutinas.DesplegarArbol(False, self.object.id,self.request )
        except:
            rutinas.CambiaOrdenGeneracion(self.object)
            rutinas.DesplegarArbol(True, self.object.id,self.request )
        return reverse_lazy('proyectos:lista') + '?criterio=' + self.request.GET['criterio'] + '&duplica=0'

    def get_context_data(self,**kwargs):
        context = super(BorrarProyectoView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            obj = Proyecto.objects.get(id=self.object.id,usuario=self.request.user)
            context['nombre'] = obj.nombre
            context['criterio'] = self.request.GET['criterio']
            context['error'] = ''
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        # rutinas.DesplegarArbol(False, self.object.id )
        return context


# RUTINAS
# Devuelve la lista de proyectos despues de analizar criterio
def ListaProyectos(criterio,usuario):
    if criterio == None:
        return Proyecto.objects.all()
    else:
        return Proyecto.objects.filter(usuario=usuario, nombre__icontains = criterio)

from modelos.models import Modelo
from propiedades.models import Propiedad
from reglas.models import Regla

def ListaRecursiva(index,strTexto,nombre,proyecto,i,lis):
    for li in Modelo.objects.filter(padre=nombre,proyecto=proyecto):
        li.ordengeneracion = i
        li.nivelidentacion = index+1
        li.save()
        i+=1
        lis[0] = i
        strTexto.append(str(index+1) + ',' + li.nombre + ',' + '1'+ ',' + 'nada')
        ListaRecursiva(index+1,strTexto,li.nombre,proyecto,i,lis)
        
# def ListaRecursiva(index,strTexto,nombre,proyecto,i):
#     for li in Modelo.objects.filter(padre=nombre,proyecto=proyecto):
#         li.ordengeneracion = i
#         li.save()
#         i+=1
#         strTexto.append(str(index+1) + ',' + li.nombre)
#         ListaRecursiva(index+1,strTexto,li.nombre,proyecto,i)
from django.db.models import FloatField,F
# def ListaCrear(id,request):
#     numre=1
#     try:
#         proyecto = Proyecto.objects.get(id=id)
#         # strTextoa = rutinas.CambiaOrdenGeneracion(proyecto)
#         # strCrear = []
#         # for item in strTextoa:
#         #     strCrear.append(item)

#     # desde aqui
#         identa = 0
#         Crear.objects.all().delete()
#         # lista = Modelo.objects.filter(proyecto=proyecto).order_by('ordengeneracion').annotate(np=F('propiedad')).select_related('proyecto')
#         # lista = Modelo.objects.filter(proyecto=proyecto).order_by('ordengeneracion').select_related("proyecto").annotate(np = F("propiedad__nombre"),tp = F("propiedad__tipo"))
#         lista = Modelo.objects.filter(proyecto=proyecto).order_by('ordengeneracion').annotate(np=F('propiedad__nombre'),tp = F('propiedad__tipo'),idp = F('propiedad__id')).select_related('proyecto')
#         for os in lista:
#             print(os.np,os.tp,os.id,os.proyecto.id)
#         # lista = Proyecto.objects.all().select_related('modelo')
#         # lista = Propiedad.objects.all().select_related('modelo').filter(modelo__proyecto = proyecto).select_related('modelo').select_related('proyecto')
#         # print('lista ',lista,len(lista))
#         pid = 0
#         pim = 0
#         pip = 0
#         numre=35
#         for os in lista:
#             if str(pid) != str(os.proyecto.id):
#                 pid = os.proyecto.id
#                 listacrear = Crear()
#                 listacrear.elemento = 'p'
#                 listacrear.nombre = proyecto.nombre
#                 listacrear.nombrepadre = 'Genesis'
#                 listacrear.proyectoid = proyecto.id
#                 listacrear.identa = identa
#                 listacrear.save()
#             if str(pid) + str(pim) != str(os.proyecto.id) + str(os.id):
#                 numre=45
#                 pim = os.id
#                 nombre_modelo=os.nombre
#                 identa = os.identa * 50
#                 ml = os
#                 listacrear = Crear()
#                 listacrear.identa = identa
#                 listacrear.nombre = ml.nombre
#                 listacrear.elemento = 'm'
#                 listacrear.proyectoid = proyecto.id
#                 listacrear.modeloid = ml.id
#                 aplicacion = ml.aplicacion
#                 listacrear.aplicacionid = ml.aplicacion.id
#                 listacrear.posicion = ml.ordengeneracion
#                 listacrear.ultimoregistro = ml.ultimoregistro
#                 listacrear.save()
#                 numre=43
#             if str(pid) + str(pim) + str(pip) != str(os.proyecto.id) + str(os.id) + str(os.idp):
#                 try:
#                     pip = os.idp
#                     numre=3
#                     listacrear = Crear()
#                     listacrear.identa = identa + 70
#                     listacrear.nombre = os.np + ' (' + os.tp + ')'
#                     numre=333
#                     listacrear.elemento = 'd'
#                     listacrear.proyectoid = proyecto.id
#                     listacrear.aplicacionid = aplicacion.id
#                     listacrear.modeloid = ml.id
#                     listacrear.propiedadid = os.idp
#                     listacrear.save()
#                     for regla in Regla.objects.filter(propiedad__id = os.idp):
#                         listacrear = Crear()
#                         listacrear.identa = identa + 140
#                         listacrear.nombre = regla.mensaje
#                         listacrear.elemento = 'r'
#                         listacrear.proyectoid = proyecto.id
#                         listacrear.aplicacionid = aplicacion.id
#                         listacrear.modeloid = ml.id
#                         listacrear.propiedadid = os.idp
#                         listacrear.reglaid = regla.id
#                         listacrear.save()
#                 except:
#                     pass
#         # proyecto = Proyecto.objects.get(id=id)

#         # listacrear = Crear()
#         # listacrear.elemento = 'p'
#         # listacrear.nombre = proyecto.nombre
#         # listacrear.nombrepadre = 'Genesis'
#         # listacrear.proyectoid = proyecto.id
#         # listacrear.identa = identa
#         # listacrear.save()
#         # numer=4
#         # lista = Modelo.objects.filter(proyecto=proyecto).annotate(tp = F('propiedad__tipo'),np = F('propiedad__nombre'),propiedad_id = F('propiedad__id'))
#         # for os in lista:
#         #     print('listaaaa ',os.nombre,os.np)

#         # lista_modelos = Modelo.objects.select_related().all()
#         # Modelos
#         # for item in strCrear:
#         #     nombre_modelo=item.split(',')[1]
#         #     identa = int(item.split(',')[0]) * 50
#         #     ml = Modelo.objects.get(nombre=nombre_modelo,proyecto=proyecto)
#         #     listacrear = Crear()
#         #     listacrear.identa = identa
#         #     listacrear.nombre = ml.nombre
#         #     listacrear.elemento = 'm'
#         #     listacrear.proyectoid = proyecto.id
#         #     listacrear.modeloid = ml.id
#         #     aplicacion = Aplicacion.objects.get(id=ml.aplicacion.id)
#         #     listacrear.aplicacionid = aplicacion.id
#         #     listacrear.posicion = ml.ordengeneracion
#         #     listacrear.ultimoregistro = ml.ultimoregistro
#         #     listacrear.save()
#         #     for propiedad in Propiedad.objects.filter(modelo = ml):
#         #         listacrear = Crear()
#         #         # identa += 50
#         #         listacrear.identa = identa + 70
#         #         listacrear.nombre = propiedad.nombre + ' (' + propiedad.tipo + ')'
#         #         listacrear.elemento = 'd'
#         #         listacrear.proyectoid = proyecto.id
#         #         listacrear.aplicacionid = aplicacion.id
#         #         listacrear.modeloid = ml.id
#         #         listacrear.propiedadid = propiedad.id
#         #         listacrear.save()

#         #         for regla in Regla.objects.filter(propiedad = propiedad):
#         #             listacrear = Crear()
#         #             listacrear.identa = identa + 140
#         #             listacrear.nombre = regla.mensaje
#         #             listacrear.elemento = 'r'
#         #             listacrear.proyectoid = proyecto.id
#         #             listacrear.aplicacionid = aplicacion.id
#         #             listacrear.modeloid = ml.id
#         #             listacrear.propiedadid = propiedad.id
#         #             listacrear.reglaid = regla.id
#         #             listacrear.save()

#     # hasta aqui

#         # # crear aplicaciones
#         # pa=1
#         # for aplicacion in Aplicacion.objects.filter(proyecto=proyecto):
#         #     listacrear = Crear()
#         #     listacrear.elemento='a'
#         #     listacrear.nombre = aplicacion.nombre
#         #     if pa == 1:
#         #         pa=0
#         #         listacrear.primero = True
#         #     listacrear.proyectoid = proyecto.id
#         #     listacrear.aplicacionid = aplicacion.id
#         #     identa = 70
#         #     listacrear.identa = 70
#         #     listacrear.save()

#         #     # crear modelos
#         #     pm=1
#         #     for modelo in Modelo.objects.filter(aplicacion=aplicacion):
#         #         identa=70
#         #         listacrear = Crear()
#         #         listacrear.elemento ='m'
#         #         listacrear.nombre = modelo.nombre
#         #         listacrear.padre = modelo.padre
#         #         if pm == 1:
#         #             pm=0
#         #             listacrear.primero = True
#         #         listacrear.proyectoid = proyecto.id
#         #         listacrear.aplicacionid = aplicacion.id
#         #         listacrear.modeloid = modelo.id

#         #         # verificar la identacion del modelo
#         #         modeloi = modelo
#         #         # identa += 70
#         #         while modeloi.padre != 'nada':
#         #             identa += 55
#         #             modeloi = Modelo.objects.get(nombre=modeloi.padre , proyecto=proyecto)
#         #         listacrear.identa = identa + 55
#         #         listacrear.restoidenta = 12 - identa
#         #         identa = listacrear.identa
#         #         listacrear.save()

#         #         # crear propiedades
#         #         pd=1    
#         #         for propiedad in Propiedad.objects.filter(modelo=modelo):
#         #             listacrear = Crear()
#         #             listacrear.elemento ='d'
#         #             listacrear.nombre = propiedad.nombre
#         #             if pd == 1:
#         #                 pd=0
#         #                 listacrear.primero = True
#         #             listacrear.proyectoid = proyecto.id
#         #             listacrear.aplicacionid = aplicacion.id
#         #             listacrear.modeloid = modelo.id
#         #             listacrear.propiedadid = propiedad.id
#         #             listacrear.identa = identa + 55
#         #             listacrear.restoidenta = 12 - (identa + 1)
#         #             # identa = listacrear.identa
#         #             listacrear.save()

#         #             # crear reglas
#         #             pr=1    
#         #             for regla in Regla.objects.filter(propiedad=propiedad):
#         #                 listacrear = Crear()
#         #                 listacrear.elemento ='r'
#         #                 listacrear.nombre = regla.mensaje
#         #                 if pr == 1:
#         #                     pr=0
#         #                     listacrear.primero = True
#         #                 listacrear.proyectoid = proyecto.id
#         #                 listacrear.aplicacionid = aplicacion.id
#         #                 listacrear.modeloid = modelo.id
#         #                 listacrear.propiedadid = propiedad.id
#         #                 listacrear.reglaid = regla.id
#         #                 listacrear.identa = identa + 110
#         #                 listacrear.restoidenta = 12 - (identa + 2)
#         #                 identa = listacrear.identa
#         #                 listacrear.save()


#         lista = Crear.objects.filter(proyectoid=proyecto.id)
#         rutinas.DesplegarArbol(False, proyecto.id,request)
#         return lista

#     except Exception as e:
#         print (str(numre) +'error en crear lista ' + str(e))

def ListaCrear(id,request,modelo_id):
    num=1
    inicio = time.time()
    strCrear = []
    proyecto = Proyecto.objects.get(id=id)

    strTexto = []

    lista = Modelo.objects.filter(padre='nada',proyecto=proyecto).order_by('ordengeneracion')

    orden = 1
    lis = [orden]
    for li in lista:
        li.ordengeneracion = lis[0]
        if orden == lista.count():
            li.ultimoregistro = 'u'
        else:
            li.ultimoregistro = 'p'
        li.nivelidentacion = 1
        li.save()
        lis[0] += 1
        # lis = [orden]
        if int(modelo_id) == li.id:
            strTexto.append('1' + ',' + li.nombre + ',' + '1'+ ',' + 'collapse')
            ListaRecursiva(1,strTexto,li.nombre,proyecto,li.ordengeneracion+1,lis)
        else:
            strTexto.append('1' + ',' + li.nombre + ',' + '0'+ ',' + 'expand')
        orden+=1
    for item in strTexto:
        strCrear.append(item)

    fin = time.time()
    inicio = time.time()

# desde aqui
    identa = 0
    Crear.objects.all().delete()
    proyecto = Proyecto.objects.get(id=id)

    listacrear = Crear()
    listacrear.elemento = 'p'
    listacrear.nombre = proyecto.nombre
    listacrear.nombrepadre = 'Genesis'
    listacrear.proyectoid = proyecto.id
    listacrear.identa = identa
    listacrear.save()
    # Modelos
    for item in strCrear:
        nombre_modelo=item.split(',')[1]
        identa = int(item.split(',')[0]) * 50
        ml = Modelo.objects.get(nombre=nombre_modelo,proyecto=proyecto)
        listacrear = Crear()
        listacrear.identa = identa
        listacrear.nombre = ml.nombre
        listacrear.elemento = 'm'
        listacrear.proyectoid = proyecto.id
        listacrear.modeloid = ml.id
        aplicacion = Aplicacion.objects.get(id=ml.aplicacion.id)
        listacrear.aplicacionid = aplicacion.id
        listacrear.posicion = ml.ordengeneracion
        listacrear.ultimoregistro = ml.ultimoregistro
        listacrear.expand = item.split(',')[3]
        listacrear.save()
        if item.split(',')[2] == '1':
            for propiedad in Propiedad.objects.filter(modelo = ml):
                listacrear = Crear()
                # identa += 50
                listacrear.identa = identa + 70
                listacrear.nombre = propiedad.nombre + ' (' + propiedad.tipo + ')'
                listacrear.elemento = 'd'
                listacrear.proyectoid = proyecto.id
                listacrear.aplicacionid = aplicacion.id
                listacrear.modeloid = ml.id
                listacrear.propiedadid = propiedad.id
                listacrear.save()

                for regla in Regla.objects.filter(propiedad = propiedad):
                    listacrear = Crear()
                    listacrear.identa = identa + 140
                    listacrear.nombre = regla.mensaje
                    listacrear.elemento = 'r'
                    listacrear.proyectoid = proyecto.id
                    listacrear.aplicacionid = aplicacion.id
                    listacrear.modeloid = ml.id
                    listacrear.propiedadid = propiedad.id
                    listacrear.reglaid = regla.id
                    listacrear.save()

    fin = time.time()

# hasta aqui

    # # crear aplicaciones
    # pa=1
    # for aplicacion in Aplicacion.objects.filter(proyecto=proyecto):
    #     listacrear = Crear()
    #     listacrear.elemento='a'
    #     listacrear.nombre = aplicacion.nombre
    #     if pa == 1:
    #         pa=0
    #         listacrear.primero = True
    #     listacrear.proyectoid = proyecto.id
    #     listacrear.aplicacionid = aplicacion.id
    #     identa = 70
    #     listacrear.identa = 70
    #     listacrear.save()

    #     # crear modelos
    #     pm=1
    #     for modelo in Modelo.objects.filter(aplicacion=aplicacion):
    #         identa=70
    #         listacrear = Crear()
    #         listacrear.elemento ='m'
    #         listacrear.nombre = modelo.nombre
    #         listacrear.padre = modelo.padre
    #         if pm == 1:
    #             pm=0
    #             listacrear.primero = True
    #         listacrear.proyectoid = proyecto.id
    #         listacrear.aplicacionid = aplicacion.id
    #         listacrear.modeloid = modelo.id

    #         # verificar la identacion del modelo
    #         modeloi = modelo
    #         # identa += 70
    #         while modeloi.padre != 'nada':
    #             identa += 55
    #             modeloi = Modelo.objects.get(nombre=modeloi.padre , proyecto=proyecto)
    #         listacrear.identa = identa + 55
    #         listacrear.restoidenta = 12 - identa
    #         identa = listacrear.identa
    #         listacrear.save()

    #         # crear propiedades
    #         pd=1    
    #         for propiedad in Propiedad.objects.filter(modelo=modelo):
    #             listacrear = Crear()
    #             listacrear.elemento ='d'
    #             listacrear.nombre = propiedad.nombre
    #             if pd == 1:
    #                 pd=0
    #                 listacrear.primero = True
    #             listacrear.proyectoid = proyecto.id
    #             listacrear.aplicacionid = aplicacion.id
    #             listacrear.modeloid = modelo.id
    #             listacrear.propiedadid = propiedad.id
    #             listacrear.identa = identa + 55
    #             listacrear.restoidenta = 12 - (identa + 1)
    #             # identa = listacrear.identa
    #             listacrear.save()

    #             # crear reglas
    #             pr=1    
    #             for regla in Regla.objects.filter(propiedad=propiedad):
    #                 listacrear = Crear()
    #                 listacrear.elemento ='r'
    #                 listacrear.nombre = regla.mensaje
    #                 if pr == 1:
    #                     pr=0
    #                     listacrear.primero = True
    #                 listacrear.proyectoid = proyecto.id
    #                 listacrear.aplicacionid = aplicacion.id
    #                 listacrear.modeloid = modelo.id
    #                 listacrear.propiedadid = propiedad.id
    #                 listacrear.reglaid = regla.id
    #                 listacrear.identa = identa + 110
    #                 listacrear.restoidenta = 12 - (identa + 2)
    #                 identa = listacrear.identa
    #                 listacrear.save()


    lista = Crear.objects.filter(proyectoid=proyecto.id)
    rutinas.DesplegarArbol(False, proyecto.id,request)
    return lista


import shutil
from django.views import View

class dumpView(View):

    def get(self, request):
        vigente = VerificaVigenciaUsuario(self.request.user)
        error = ''
        try:
            user = self.request.user
            proyecto = Proyecto.objects.get(usuario = self.request.user, id = self.request.GET['proyecto_id'])
            etapa = 'CrearZip'
            # Borrar los errores de generacion

            # Borrar los errores
            ErroresCreacion.objects.filter(proyecto=proyecto.nombre,usuario=user.username).delete()
            # Leer los directorios
            gen = Genesis.objects.get(nombre='GENESIS')

            # Leer el archivo download.html
            stri =  rutinas.LeerArchivoEnTexto(gen.directoriotexto + 'download_file.html',etapa,proyecto.nombre,user.username )
            # Reemplazar nombre de archivo
            stri = stri.replace('@file', user.username + '/' + proyecto.nombre + '.zip')
            stri = stri.replace('@nombrefile', proyecto.nombre + '.zip')
            # Grabar el nuevo download en el directorio proyectos/username/
            error = 'No se creo el directorio: ' + gen.directoriogenesis + 'proyectos/templates/proyectos/' + user.username
            rutinas.CrearDirectorio(gen.directoriogenesis + 'proyectos/templates/proyectos/' + user.username,etapa,user.username,user.username,True)
            error = 'No se grabo el archivo : ' + gen.directoriogenesis + 'proyectos/templates/proyectos/' + user.username + '/download.html'
            rutinas.EscribirEnArchivo(gen.directoriogenesis + 'proyectos/templates/proyectos/' + user.username + '/download.html',stri,etapa,proyecto.nombre,user.username) 

            # leer el directorio de genesis
            cdzip = gen.directoriogenesis + 'core/static/core/zipfiles/' + user.username + '/' + proyecto.nombre
            cdarchivoazipear = gen.directoriozip + proyecto.nombre
            error = 'No se comprimio el archivo : ' + cdzip + '.zip'
            shutil.make_archive(cdzip, 'zip', cdarchivoazipear )
            error = ''
            return render(request, 'proyectos/' + user.username + '/download.html' ,{'nombre':proyecto.nombre, 'proyecto': proyecto,'vigente':vigente,'error':error})             
        except:
            return render(request, 'proyectos/arbol_proyecto.html' ,{'nombre':proyecto.nombre, 'proyecto': proyecto,'vigente':vigente,'error':error})             


        # proyecto = Proyecto.objects.get(usuario = self.request.user, id = self.request.GET['proyecto_id'])

        # user = self.request.user

        # gen = Genesis.objects.get(nombre='GENESIS')
        # # leer el directorio de genesis
        # cdzip = gen.directorio + '/core/static/core/zipfiles/' + user.username + '/proyecto'
        # cdarchivoazipear = gen.directoriozip + proyecto.nombre
        # shutil.make_archive(cdzip, 'zip', cdarchivoazipear )
        # return render(request, 'proyectos/' + user.username + '/download.html' ,{'nombre':proyecto.nombre})             

class DesplegarPreciosView(TemplateView):
    template_name = "proyectos/desplegar_precios.html"

    def post(self, request, *args, **kwargs):
        # crea la licencia gratuita
        lic = LicenciaUso()
        lic.usuario = self.request.user
        lic.opcion = 1
        lic.inicio = timezone.now()
        lic.expira = timezone.now() + datetime.timedelta(days=30)
        lic.save()

        return self.get(request, *args, **kwargs)

    def get_context_data(self,**kwargs):
        context = super(DesplegarPreciosView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        puede = 's'
        # Uso gratuito
        if LicenciaUso.objects.filter(usuario=self.request.user,opcion=1).count() == 1:
            lic = LicenciaUso.objects.get(usuario=self.request.user,opcion=1)
            if lic.expira > timezone.now():
                context['expira'] = 'Expirada'
            context['expira'] = lic.expira
            puede = 'n'
        context['puede'] = puede
        context['username'] = self.request.user.username
        lista = []
        for precio in Precio.objects.all():
            dt=Genesis.objects.get(nombre='GENESIS').directoriotexto
            stri = rutinas.LeerArchivo(dt + precio.paypal,'','','')
            lista.append([precio.titulo, precio.descripcion, precio.importe,stri])
        context['precios'] = lista
        context['error'] = ''
        return context  


class ListaTextoView(ListView):
    model = ProyectoTexto

    def get_context_data(self, **kwargs):
        context = super(ListaTextoView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['lista_texto'] = ProyectoTexto.objects.filter(usuario=self.request.user)
        context['error'] = ''
        context['criterio'] = self.request.GET['criterio']
        return context

class ListaJsonView(ListView):
    model = ProyectoJson

    def get_context_data(self, **kwargs):
        context = super(ListaJsonView, self).get_context_data(**kwargs)
        try:
            proyecto_json = self.request.GET['json']
            # proyecto_jsond = json.load(proyecto_json)
            user = self.request.user
            if self.request.GET['nuevo'] == "1":
                # proyecto_json["propiedades"][0]["id_base"] = 1
                proyecto = ProyectoJson()
                proyecto.texto =  proyecto_json
                proyecto.usuario = user
                proyecto.save()
            if self.request.GET['nuevo'] == "0":
                id = self.request.GET['id']
                proyectojson = ProyectoJson.objects.get(id=id)
                proyectojson.texto =  proyecto_json
                proyectojson.save()


        except:
            pass
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['lista_json'] = ProyectoJson.objects.filter(usuario=self.request.user)
        lista = []
        for pj in ProyectoJson.objects.filter(usuario=self.request.user):
            np = ''
            texto_json = json.loads(pj.texto)['propiedades']
            for i in range(len(texto_json)):
                if texto_json[i]['nombre_objeto'] == 'proyecto':
                    np = texto_json[i]['nombre']
                    break
            lista.append([np,pj])
        context['lista_json'] = lista

        context['error'] = ''
        context['criterio'] = self.request.GET['criterio']
        return context

class ListaObjetoView(ListView):
    model = ProyectoObjeto

    def get_context_data(self, **kwargs):
        context = super(ListaObjetoView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['lista_objeto'] = ProyectoObjeto.objects.filter(usuario=self.request.user)
        context['error'] = ''
        context['criterio'] = self.request.GET['criterio']
        return context

class CrearTextoView(CreateView):
    model = ProyectoTexto
    form_class = ProyectoTextoForm

    def get_success_url(self):
        # return reverse_lazy('proyectos:home')
        return reverse_lazy('proyectos:lista_texto') + '?criterio=' + self.request.GET['criterio']

    def get_context_data(self,**kwargs):
        context = super(CrearTextoView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['error'] = ''
        context['criterio'] = self.request.GET['criterio']
        context['etiquetas'] = Etiquetas()
        return context

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST,request.FILES)
        user = request.user
        if form.is_valid():
            proyectotexto = form.save(commit=False)
            proyectotexto.usuario = user
            proyectotexto.save()
            return HttpResponseRedirect(self.get_success_url())
        return render(request, 'proyectos/proyectotexto_form.html', {'form': form})

class EditarObjetoView(UpdateView):
    model = ProyectoObjeto
    form_class = ProyectoObjetoForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('proyectos:editar_objeto', args=[self.object.id]) + '?ok' + '&criterio=' + self.request.GET['criterio']

    def get_context_data(self,**kwargs):
        context = super(EditarObjetoView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['error'] = ''
        context['criterio'] = self.request.GET['criterio']
        return context

class EditarTextoView(UpdateView):
    model = ProyectoTexto
    form_class = ProyectoTextoForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('proyectos:editar_texto', args=[self.object.id]) + '?ok' + '&criterio=' + self.request.GET['criterio']

    def get_context_data(self,**kwargs):
        context = super(EditarTextoView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['error'] = ''
        context['criterio'] = self.request.GET['criterio']
        context['etiquetas'] = Etiquetas()
        return context

def Etiquetas():
    try:
        lista = []

        #   'conroles',
                  
        lista.append(['','CONSTRUCCION RAPIDA','t'])
        lista.append(['Proyecto', 'Esquema de un proyecto','e'])
        lista.append(['Aplicacion','Esquema de una aplicacion','e'])
        lista.append(['Modelo','Esquema de un modelo','e'])
        lista.append(['Propiedad','Esquema de una propiedad','e'])
        lista.append(['Regla','Esquema de una regla','e'])
        lista.append(['','FIN DE ATRIBUTO','t'])
        lista.append(['fin','Terminacion de atributo','e'])
        lista.append(['','PROYECTOS','t'])
        lista.append(['npr','Nombre del Proyecto','e'])
        lista.append(['dpr','Descripcion del Proyecto','e'])
        # lista.append(['cpp','Color de la pagina principal','e'])
        lista.append(['tit','Titulo del Proyecto','e'])
        lista.append(['pcs','El Proyecto tiene seguridad','e'])
        lista.append(['pcr','El Proyecto tiene roles','e'])
        lista.append(['pce','Codigo del Proyecto con etiquetas de personalizacion','e'])
        lista.append(['pcb','Proyecto con opcion de busqueda','e'])
        # lista.append(['ses','Separacion entre secciones','e'])
        # lista.append(['avw','Ancho del Logo del Proyecto','e'])
        # lista.append(['avh','Alto del Logo del Proyecto','e'])
        # lista.append(['itw','Ancho de la imagen del Titulo','e'])
        # lista.append(['ith','Alto de la imagen del Titulo','e'])
        # lista.append(['fti','Font del Titulo','e'])
        # lista.append(['cti','Color del texto del Titulo','e'])
        # lista.append(['act','Alto de la columna del Titulo','e'])
        # lista.append(['nct','Numero de columnas de la columna del Titulo','e'])
        # lista.append(['cct','Color de la columna del Titulo','e'])
        # lista.append(['jht','Justificacion horizontal del Titulo','e'])
        # lista.append(['jvt','Justificacion vertical del Titulo','e'])
        # lista.append(['afs','Altura de la fila superior','e'])
        # lista.append(['cfs','Color de la fila superior','e'])
        # lista.append(['nci','Numero de columnas de la columna superior izquierda','e'])
        # lista.append(['aci','Altura de la columna superior izquierda','e'])
        # lista.append(['cci','Color de la columna superior izquierda','e'])
        # lista.append(['ncd','Numero de columnas de la columna superior derecha','e'])
        # lista.append(['acd','Altura de la columna superior derecha','e'])
        # lista.append(['ccd','Color de la columna superior derecha','e'])
        # lista.append(['acl','Altura de la columna del Logo','e'])
        # lista.append(['ccl','Color de la columna del Logo','e'])
        # lista.append(['ncl','Numero de las columnas de la columna del Logo','e'])
        # lista.append(['jhl','Justificacion horizontal del Logo','e'])
        # lista.append(['jvl','Justificacion vertical del Logo','e'])
        # lista.append(['acg','Altura de la columna de Login','e'])
        # lista.append(['ncg','Numero de columnas de la columna de Login','e'])
        # lista.append(['ccg','Color de la columna de Login','e'])
        # lista.append(['bss','Borde de las secciones de la fila superior','e'])
        # lista.append(['cbss','Color borde de las secciones de la fila superior','e'])
        # lista.append(['abss','Ancho borde de las secciones de la fila superior','e'])
        # lista.append(['afb','Alto de la fila de bus-menu','e'])
        # lista.append(['cfb','Color de la fila de bus-menu','e'])
        # lista.append(['ncbi','Numero de columnas de la columna bus-menu izquierda ','e'])
        # lista.append(['acbi','Altura de la columna bus-menu izquierda','e'])
        # lista.append(['ccbi','Color de la columna bus-menu izquierda','e'])
        # lista.append(['ncbd','Numero de columnas de la columna bus-menu derecha','e'])
        # lista.append(['acbd','Altura de la columna bus-menu derecha','e'])
        # lista.append(['ccbd','Color de la columna bus-menu derecha','e'])
        # lista.append(['acb','Altura de la columna de busqueda','e'])
        # lista.append(['ncb','Numero de columnas de la columna de busqueda','e'])
        # lista.append(['ccb','Color de la columna de busqueda','e'])
        # lista.append(['acm','Altura de la columna del menu','e'])
        # lista.append(['ncm','Numero de columnas de la columna del menu','e'])
        # lista.append(['ccm','Color de la columna del menu','e'])
        # lista.append(['cme','Color de las opciones del menu','e'])
        # lista.append(['fme','Font de la opcion del menu','e'])
        # lista.append(['bme','Borde de las secciones de la fila de busqueda y menu','e'])
        # lista.append(['abme','Ancho del borde de las secciones de la fila de busqueda y menu','e'])
        # lista.append(['cbme','Color del borde de las secciones de la fila de busqueda y menu','e'])
        # lista.append(['afm','Altura de la fila del medio','e'])
        # lista.append(['cfm','Color de la fila del medio','e'])
        # lista.append(['jum','Justificacion del menu','e'])
        # lista.append(['acmi','Altura de la columna izquierda del medio','e'])
        # lista.append(['ncmi','Numero de columnas de la la columna izquierda del medio','e'])
        # lista.append(['ccmi','Color de la columna izquierda del medio','e'])
        # lista.append(['acmc','Altura de la columna central del medio','e'])
        # lista.append(['ncmc','Numero de columnas de la columna central del medio','e'])
        # lista.append(['ccmc','Color de la columna central del medio','e'])
        # lista.append(['acmd','Altura de la columna derecha del medio','e'])
        # lista.append(['ncmd','Numero de columnas de la columna derecha del medio','e'])
        # lista.append(['ccmd','Color de la columna derecha del medio','e'])
        # lista.append(['txm','Texto de la columna central del medio','e'])
        # lista.append(['ctxm','Color del texto de la columna central del medio','e'])
        # lista.append(['ftxm','Font del texto de la columna central del medio','e'])
        # lista.append(['afp','Alto de la fila del pie','e'])
        # lista.append(['cfp','Color de la fila del pie','e'])
        # lista.append(['acp','Altura de la columna del pie','e'])
        # lista.append(['ccp','Color de la columna del pie','e'])
        # lista.append(['txv','Texto de la opcion volver','e'])
        # lista.append(['ftxv','Font del texto de la opcion volver','e'])
        # lista.append(['ctxv','Color del texto de la opcion volver','e'])
        # lista.append(['mctg','Los menus son contiguos','e'])
        # lista.append(['bce','Borde en la seccion central','e'])
        # lista.append(['cbce','Color del borde de la seccion central','e'])
        # lista.append(['abce','Ancho del borde de la seccion central','e'])
        lista.append(['','APLICACIONES','t'])
        lista.append(['nap','Nombre de la Aplicacion','e'])
        lista.append(['dap','Descripcion de la Aplicacion','e'])
        lista.append(['txma','Texto de la opcion en el menu','e'])
        # lista.append(['as','Para acceder a la Aplicacion se debe ser miembro del staff','e'])
        # lista.append(['al','Para acceder a la Aplicacion se debe etar autenticado','e'])
        # lista.append(['tta','ToolTip en la opcion del menu','e'])
        # lista.append(['oga','Orden de generacion de la aplicacion','e'])
        # lista.append(['hlg','Para acceder a la aplicacion se debe estar auntenticado','e'])
        # lista.append(['hst','Para acceder a la aplicacion se debe ser miembro del staff','e'])
        lista.append(['','MODELOS','t'])
        lista.append(['nmo','Nombre del Modelo','e'])
        lista.append(['dmo','Descripcion del Modelo','e'])
        lista.append(['pmo','Padre del Modelo','e'])
        lista.append(['smo','Identificacion self del Modelo','e'])
        lista.append(['bmo','Identificacion de borrado del Modelo','e'])
        lista.append(['amo','Aplicacion del Modelo','e'])
        lista.append(['tom','Texto para la opcion del menu','e'])
        # lista.append(['ttm','ToolTip de la opcion del menu','e'])
        # lista.append(['mem','El Modelo no aparece en el menu','e'])
        # lista.append(['bli','El Modelo tiene un buscador en la lista','e'])
        # lista.append(['rgu','El Modelo Es de un solo registro','e'])
        # lista.append(['tvw','El Modelo se edita en TreeView','e'])
        # lista.append(['cftw','Color de fondo del TreeView','e'])
        # lista.append(['cltw','Color del listado del TreeView','e'])
        # lista.append(['opel','La opcion editar aparece en la lista','e'])

        # lista.append(['tli','Titulo de la lista del Modelo','e'])
        # lista.append(['ftli','Font del titulo de la lista del Modelo','e'])
        # lista.append(['cftl','Color de fondo del titulo de la lista','e'])
        # lista.append(['ctli','Color del titulo de la lista','e'])
        # lista.append(['atli','Altura del titulo de la lista','e'])
        # lista.append(['mtli','El titulo de la lista esta en mayusculas','e'])
        # lista.append(['jvtl','Justificacion vertical del titulo de la lista','e'])
        # lista.append(['jhtl','Justificacion horizontal del titulo de la lista','e'])
        # lista.append(['fcli','Fonto del comentario de la lista','e'])
        # lista.append(['cmli','Texto del comentario de la lista','e'])
        # lista.append(['cfcml','Color de fondo del comentario de la lista','e'])
        # lista.append(['ccmli','Color del texto del comentario de la lista','e'])
        # lista.append(['mco','Las columnas estan en mayusculas','e'])
        # lista.append(['aco','Altura de las columnas','e'])
        # lista.append(['cfcl','Color del fondo de las columnas de la lista','e'])
        # lista.append(['ccli','Color del texto de las columnas de la lista','e'])
        # lista.append(['fcli','Font del texto de las columnas de la lista','e'])
        # lista.append(['clcb','La columna de la lista tiene borde','e'])
        # lista.append(['ftxl','Font del texto de la lista','e'])
        # lista.append(['cftxc','Color de fondo del texto de la lista','e'])
        # lista.append(['ctxl','Color del texto de la lista','e'])
        # lista.append(['feb','Font texto editar borrar','e'])
        # lista.append(['ceb','Color del texto editar borrar','e'])
        # lista.append(['teb','Texto de Editar y Borrar','e'])
        # # lista.append(['flnm','Font del link de nuevo modelo','e'])

        # lista.append(['clnm','Color del link de nuevo modelo','e'])
        # lista.append(['tlnm','Texto del link de nuevo modelo','e'])
        # # lista.append(['lnm','La opcion de nuevo modelo es un link','e'])
        # lista.append(['tin','Titulo de formulario nuevo Modelo','e'])
        # lista.append(['ftin','Font del titulo del formulario nuevo Modelo','e'])
        # lista.append(['ctin','Color del titulo del formulario nuevo Modelo','e'])
        # lista.append(['cfti','Color de fondo del titulo del formulario nuevo Modelo','e'])
        # lista.append(['cffti','Color de fondo de la fila del titulo del formulario nuevo Modelo','e'])
        # lista.append(['afti','Altura de la fila del titulo del formulario nuevo Modelo','e'])
        # lista.append(['jvti','Justificacion vertical del titulo del formulario nuevo Modelo','e'])
        # lista.append(['jhti','Justificacion horizontal del titulo del formulario nuevo Modelo','e'])
        # lista.append(['cfci','Color de fondo del comentario del formulario nuevo Modelo','e'])
        # lista.append(['ccin','Color del comentario del formulario nuevo Modelo','e'])
        # lista.append(['fcin','Font del comentario del formulario nuevo Modelo','e'])
        # lista.append(['cin','Texto del comentario del formulario nuevo Modelo','e'])
        # lista.append(['ncii','Numero columnas del margen izquierdo formulario nuevo Modelo','e'])
        # lista.append(['ncmi','Numero de columnas para formulario nuevo Modelo','e'])
        # lista.append(['ncdi','Numero columnas del margen derecho formulario nuevo Modelo','e'])

        # lista.append(['tup','Titulo de formulario editar Modelo','e'])
        # lista.append(['ftup','Font del titulo del formulario editar Modelo','e'])
        # lista.append(['ctup','Color del titulo del formulario editar Modelo','e'])
        # lista.append(['cftu','Color de fondo del titulo del formulario editar Modelo','e'])
        # lista.append(['cfftu','Color de fondo de la fila del titulo del formulario editar Modelo','e'])
        # lista.append(['aftu','Altura de la fila del titulo del formulario editar Modelo','e'])
        # lista.append(['jvtu','Justificacion vertical del titulo del formulario editar Modelo','e'])
        # lista.append(['jhtu','Justificacion horizontal del titulo del formulario editar Modelo','e'])
        # lista.append(['cup','Texto del comentario del formulario nuevo Modelo','e'])
        # lista.append(['cfcu','Color de fondo del comentario del formulario nuevo Modelo','e'])
        # lista.append(['fcup','Font del comentario del formulario editar Modelo','e'])
        # lista.append(['ccup','Color del comentario del formulario editar Modelo','e'])
        # lista.append(['nciu','Numero columnas del margen izquierdo formulario editar Modelo','e'])
        # lista.append(['ncdu','Numero columnas del margen derecho formulario editar Modelo','e'])
        # lista.append(['ncmu','Numero de columnas para formulario editar Modelo','e'])
        # lista.append(['flm','Font de las etiquetas','e'])
        # lista.append(['clm','Color de las etiquetas','e'])
        # lista.append(['cau','Lo constroles se crean de forma automatica','e'])

        # lista.append(['tbo','Titulo de formulario borrar Modelo','e'])
        # lista.append(['ftbo','Font del titulo del formulario borrar Modelo','e'])
        # lista.append(['ctb','Color del titulo del formulario borrar Modelo','e'])
        # lista.append(['cftb','Color de fondo del titulo del formulario borrar Modelo','e'])
        # lista.append(['cfftb','Color de fondo de la fila del titulo del formulario borrar Modelo','e'])
        # lista.append(['aftb','Altura de la fila del titulo del formulario borrar Modelo','e'])
        # lista.append(['jvtb','Justificacion vertical del titulo del formulario borrar Modelo','e'])
        # lista.append(['jhtb','Justificacion horizontal del titulo del formulario borrar Modelo','e'])
        # lista.append(['cfcb','Color de fondo del comentario del formulario borrar Modelo','e'])
        # lista.append(['ccbo','Color del comentario del formulario borrar Modelo','e'])
        # lista.append(['fcbo','Font del comentario del formulario borrar Modelo','e'])
        # lista.append(['cbo','Texto del comentario del formulario borrar Modelo','e'])
        # lista.append(['cftxb','Color del fondo del texto borrar del formulario borrar Modelo','e'])
        # lista.append(['ctxb','Color del texto borrar del formulario borrar Modelo','e'])
        # lista.append(['ftxb','Font del texto borrar del formulario borrar Modelo','e'])
        # lista.append(['txbo','Texto de borrar del formulario borrar Modelo','e'])
        # lista.append(['txbb','Texto del boton borrar del formulario borrar Modelo','e'])
        # lista.append(['ncib','Numero columnas del margen izquierdo formulario borrar Modelo','e'])
        # lista.append(['ncdb','Numero columnas del margen derecho formulario borrar Modelo','e'])
        # lista.append(['ncmb','Numero de columnas para formulario borrar Modelo','e'])
        # lista.append(['hco','Los hijos del Modelo son contiguos','e'])
        # lista.append(['nchu','Numero columnas del margen derecho editar Hijos','e'])
        # lista.append(['ls','Para la lista se debe pertenecer al staff','e'])
        # lista.append(['ll','Para la lista se debe estar autenticado','e'])
        # lista.append(['cs','Para un nuevo Modelo se debe pertenecer al staff','e'])
        # lista.append(['cl','Para un nuevo Modelo se debe estar autenticado','e'])
        # lista.append(['es','Para editar un Modelo debe pertenecer al staff','e'])
        # lista.append(['el','Para editar un modelo se debe estra autenticado','e'])
        # lista.append(['bc','Para borrar un Modelo de debe pertenecer al staff','e'])
        # lista.append(['bl','Para borrar un Modelo se debe estar autenticado','e'])
        # lista.append(['nclb','Numero de columnas para las etiquetas','e'])
        # lista.append(['ncct','Numero de columnas para los controles','e'])
        # # lista.append(['msb','El Modelo no esta en la base de datos','e'])
        # lista.append(['cbnm','Color del boton del numevo modelo','e'])
        # lista.append(['ctbo','Color de titulo del formulario de borrado del modelo','e'])
        lista.append(['','PROPIEDADES','t'])
        lista.append(['npro','Nombre de la Propiedad','e'])
        lista.append(['dpro','Descripcion de la Propiedad','e'])
        lista.append(['tpro','Tipo de la Propiedad','e'])
        lista.append(['','s - String','p'])
        lista.append(['','x - Text Field','p'])
        lista.append(['','h - RichText','p'])
        lista.append(['','m - Entero small','p'])
        lista.append(['','i - Entero','p'])
        lista.append(['','l - Entero long','p'])
        lista.append(['','d - Decimal','p'])
        lista.append(['','f - Foranea','p'])
        lista.append(['','n - Fecha','p'])
        lista.append(['','t - Hora y Fecha','p'])
        lista.append(['','e - Hora','p'])
        lista.append(['','b - Boolean','p'])
        lista.append(['','r - Radio Button','p'])
        lista.append(['','p - Imagen','p'])
        lista.append(['','u - Usuario','p'])
        lista.append(['prf','Modelo para Propiedad foranea','e'])
        lista.append(['txb','Texto de los Radio Buttons','e'])
        # lista.append(['vdf','Valor inicial por defecto','e'])
        lista.append(['lst','Longitud de una Propiedad tipo string','e'])
        lista.append(['tph','Texto del PlaceHolder','e'])
        lista.append(['epro','Etiqueta de la Propiedad en el formulario','e'])
        lista.append(['enl','La Propedad se despliega en la lista del Modelo','e'])
        lista.append(['emb','La Propiedad puede ser vista en Mobile','e'])
        lista.append(['ncl','Numero de columnas de la Propiedad en la lista del Modelo','e'])
        # lista.append(['txc','Texto de la columna en la lista del Modelo','e'])
        # lista.append(['jtxc','Justificacion horizontal del texto en la columna de la lista','e'])
        # lista.append(['ffch','Formato de la Propiedad tipo DateTime','e'])
        # lista.append(['ear','La etiqueta se coloca arriba del control en el formulario','e'])
        # lista.append(['mdt','La Propiedad es mandatoria','e'])
        # lista.append(['nef','La Propiedad no aparece en el formulario','e'])
        lista.append(['pbl','La Propiedad participa en la busqueda de la lista','e'])
        lista.append(['tlz','La Propiedad se totaliza','e'])
        # lista.append(['lpe','La Propiedad es un link de edicion','e'])
        # lista.append(['enr','La Propiedad aparece en el reporte','e'])
        # lista.append(['anre','Ancho en el reporte','e'])
        lista.append(['','REGLAS','t'])
        lista.append(['msj','Mensaje de error cuando se incumple la Regla','e'])
        lista.append(['crg','Codigo de la Regla','e'])
        return lista
    except:
        return''

class BorrarTextoView(DeleteView):
    model = ProyectoTexto

    def get_success_url(self):
        return reverse_lazy('proyectos:lista_texto') + '?criterio=' + self.request.GET['criterio']

    def get_context_data(self,**kwargs):
        context = super(BorrarTextoView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['error'] = ''
        context['criterio'] = self.request.GET['criterio']
        return context

class BorrarObjetoView(DeleteView):
    model = ProyectoObjeto

    def get_success_url(self):
        return reverse_lazy('proyectos:lista_objeto') + '?criterio=' + self.request.GET['criterio']

    def get_context_data(self,**kwargs):
        context = super(BorrarObjetoView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['error'] = ''
        context['criterio'] = self.request.GET['criterio']
        return context

class BorrarJsonView(DeleteView):
    model = ProyectoJson

    def get_success_url(self):
        return reverse_lazy('proyectos:lista_json') + '?criterio=' + self.request.GET['criterio']

    def get_context_data(self,**kwargs):
        context = super(BorrarJsonView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['error'] = ''
        context['criterio'] = self.request.GET['criterio']
        return context

class CrearJsonView(TemplateView):
    template_name = "proyectos/arbol_drag_drop.html"

    def get_context_data(self,**kwargs):
        context = super(CrearJsonView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['error'] = ''        
        return context

class CrearObjetoView(CreateView):
    model = ProyectoObjeto
    form_class = ProyectoObjetoForm

    def get_success_url(self):
        # return reverse_lazy('proyectos:home')
        return reverse_lazy('proyectos:lista_objeto') + '?criterio=' + self.request.GET['criterio']

    def get_context_data(self,**kwargs):
        context = super(CrearObjetoView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['error'] = ''
        context['criterio'] = self.request.GET['criterio']
        return context

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST,request.FILES)
        user = request.user
        if form.is_valid():
            proyectoobjeto = form.save(commit=False)
            proyectoobjeto.usuario = user
            proyectoobjeto.save()
            return HttpResponseRedirect(self.get_success_url())
        return render(request, 'proyectos/proyectoobjeto_form.html', {'form': form})

class ProcesaJsonView(TemplateView):
    template_name = "proyectos/proyecto_procesa_json.html"

    def get_context_data(self,**kwargs):
        context = super(ProcesaJsonView, self).get_context_data(**kwargs)
        texto_procesar = ProyectoJson.objects.get(id=self.request.GET['id'])
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['error'] = ''
        context['error_texto'] = ''
        context['criterio'] = self.request.GET['criterio']

        lista_app = []
        lista_mod = []
        lista_prop = []
        try:
            try:
                proyecto_anterior = Proyecto.objects.get(id=texto_procesar.proyecto)
                # Recuperar las aplicaciones
                for aplicacion in Aplicacion.objects.filter(proyecto = proyecto_anterior):
                    lista_app.append(aplicacion)
                    for modelo in Modelo.objects.filter(aplicacion = aplicacion,proyecto=proyecto_anterior):
                        lista_mod.append(modelo)
                        for propiedad in Propiedad.objects.filter(modelo =  modelo):
                            lista_prop.append(propiedad)
                # Proyecto.objects.get(id=texto_procesar.proyecto).delete()
            except:
                proyecto_anterior = None            
            # Procesa texto
            # Encontrar el proyecto
            texto_json = json.loads(texto_procesar.texto)['propiedades']
            proyecto = None
            paso = '1'
            for i in range(len(texto_json)):
                if texto_json[i]['nombre_objeto'] == 'proyecto':
                    paso = '2'
                    proyecto = Proyecto()
                    proyecto.nombre = texto_json[i]['nombre']
                    proyecto.usuario = self.request.user
                    proyecto.save()
                    rutinas.CrearSeccionProyecto(proyecto)
                    texto_procesar.proyecto = proyecto.id
                    texto_procesar.save()
                    # encontrar las aplicaciones
                    for nap in range(len(texto_json)):
                        if texto_json[nap]['nombre_objeto'] == 'aplicacion':
                            paso = '3'
                            if int(texto_json[nap]['id_padre']) == int(texto_json[i]['id']):
                                aplicacion = None
                                if proyecto != None:
                                    aplicacion = Aplicacion()
                                    aplicacion.nombre = texto_json[nap]['nombre']
                                    aplicacion.proyecto = proyecto
                                    aplicacion.save()
                                    paso = '4'
                                    # Encontrar los modelos para las aplicaciones
                                    for nmo in range(len(texto_json)):
                                        if texto_json[nmo]['nombre_objeto'] == 'modelo':
                                            if int(texto_json[nmo]['id_padre']) == int(texto_json[nap]['id']):
                                                modelo = None
                                                if aplicacion != None:
                                                    modelo = Modelo()
                                                    modelo.nombre = texto_json[nmo]['nombre']
                                                    modelo.aplicacion = aplicacion
                                                    modelo.proyecto = proyecto
                                                    modelo.save()
                                                    paso = '5'
                                                    PropiedadesModelo(texto_json,nmo,modelo)
                                                    paso = '6'
                                                    # Encontrar los modelos hijo para el modelo
                                                    for nmoh in range(len(texto_json)):
                                                        if texto_json[nmoh]['nombre_objeto'] == 'modelo':
                                                            if int(texto_json[nmoh]['id_padre']) == int(texto_json[nmo]['id']):
                                                                if modelo != None:
                                                                    modelohijo = Modelo()
                                                                    modelohijo.padre = modelo.nombre
                                                                    modelohijo.aplicacion = aplicacion
                                                                    modelohijo.proyecto = proyecto
                                                                    modelohijo.nombre = texto_json[nmoh]['nombre']
                                                                    modelohijo.save()
                                                                    PropiedadesModelo(texto_json,nmoh,modelohijo)
                                else:   
                                    context['error_texto'] = 'No se definio un proyecto'

            if proyecto_anterior != None:                                    
                # Reconstruir los datos del proyecto anterior en el proyecto nuevo
                Reconstruye(proyecto, proyecto_anterior,lista_app,lista_mod,lista_prop)
            context['proyecto'] = proyecto
                                       
        except Exception as e:
            context['error_texto'] = 'Existe error en la construccion del Texto: ' + paso + ' ' + str(e)
        return context

class ProcesaObjetoView(TemplateView):
    template_name = "proyectos/proyecto_procesa_json.html"

    def get_context_data(self,**kwargs):
        context = super(ProcesaObjetoView, self).get_context_data(**kwargs)
        texto_procesar = ProyectoJson.objects.get(id=self.request.GET['id'])
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['error'] = ''
        context['error_texto'] = ''
        context['criterio'] = self.request.GET['criterio']

        lista_app = []
        lista_mod = []
        lista_prop = []
        try:
            try:
                proyecto_anterior = Proyecto.objects.get(id=texto_procesar.proyecto)
                # Recuperar las aplicaciones
                for aplicacion in Aplicacion.objects.filter(proyecto = proyecto_anterior):
                    lista_app.append(aplicacion)
                    for modelo in Modelo.objects.filter(aplicacion = aplicacion,proyecto=proyecto_anterior):
                        lista_mod.append(modelo)
                        for propiedad in Propiedad.objects.filter(modelo =  modelo):
                            lista_prop.append(propiedad)
                # Proyecto.objects.get(id=texto_procesar.proyecto).delete()
            except:
                proyecto_anterior = None            # Procesa texto
            # Encontrar el proyecto
            texto_json = json.loads(texto_procesar.texto)['propiedades']
            proyecto = None
            paso = '1'
            for i in range(len(texto_json)):
                if texto_json[i]['nombre_objeto'] == 'proyecto':
                    paso = '2'
                    proyecto = Proyecto()
                    proyecto.nombre = texto_json[i]['nombre']
                    proyecto.usuario = self.request.user
                    proyecto.save()
                    rutinas.CrearSeccionProyecto(proyecto)
                    texto_procesar.proyecto = proyecto.id
                    texto_procesar.save()
                    # encontrar las aplicaciones
                    for nap in range(len(texto_json)):
                        if texto_json[nap]['nombre_objeto'] == 'aplicacion':
                            paso = '3'
                            if int(texto_json[nap]['id_padre']) == int(texto_json[i]['id']):
                                aplicacion = None
                                if proyecto != None:
                                    aplicacion = Aplicacion()
                                    aplicacion.nombre = texto_json[nap]['nombre']
                                    aplicacion.proyecto = proyecto
                                    aplicacion.save()
                                    paso = '4'
                                    # Encontrar los modelos para las aplicaciones
                                    for nmo in range(len(texto_json)):
                                        if texto_json[nmo]['nombre_objeto'] == 'modelo':
                                            if int(texto_json[nmo]['id_padre']) == int(texto_json[nap]['id']):
                                                modelo = None
                                                if aplicacion != None:
                                                    modelo = Modelo()
                                                    modelo.nombre = texto_json[nmo]['nombre']
                                                    modelo.aplicacion = aplicacion
                                                    modelo.proyecto = proyecto
                                                    modelo.save()
                                                    paso = '5'
                                                    PropiedadesModelo(texto_json,nmo,modelo)
                                                    paso = '6'
                                                    # Encontrar los modelos hijo para el modelo
                                                    for nmoh in range(len(texto_json)):
                                                        if texto_json[nmoh]['nombre_objeto'] == 'modelo':
                                                            if int(texto_json[nmoh]['id_padre']) == int(texto_json[nmo]['id']):
                                                                if modelo != None:
                                                                    modelohijo = Modelo()
                                                                    modelohijo.padre = modelo.nombre
                                                                    modelohijo.aplicacion = aplicacion
                                                                    modelohijo.proyecto = proyecto
                                                                    modelohijo.nombre = texto_json[nmoh]['nombre']
                                                                    modelohijo.save()
                                                                    PropiedadesModelo(texto_json,nmoh,modelohijo)
                                else:   
                                    context['error_texto'] = 'No se definio un proyecto'

            if proyecto_anterior != None:                                    
                # Reconstruir los datos del proyecto anterior en el proyecto nuevo
                Reconstruye(proyecto, proyecto_anterior,lista_app,lista_mod,lista_prop)
                                       
        except Exception as e:
            context['error_texto'] = 'Existe error en la construccion del Texto: ' + paso + ' ' + str(e)
        return context

def PropiedadesModelo(texto_json, nmo, modelo):
    # Encontrar las propiedades para el modelo
    for npr in range(len(texto_json)):
        if texto_json[npr]['nombre_objeto'] == 'propiedad':
            if int(texto_json[npr]['id_padre']) == int(texto_json[nmo]['id']):
                if modelo != None:
                    propiedad = Propiedad()
                    propiedad.modelo = modelo
                    propiedad.nombre = texto_json[npr]['nombre']
                    if texto_json[npr]['tipo'] == 'string':
                        propiedad.tipo = 's'
                        propiedad.largostring = texto_json[npr]['largo_string'] 
                    if texto_json[npr]['tipo'] == 'entero':
                        propiedad.tipo = 'i'
                    if texto_json[npr]['tipo'] == 'boolean':
                        propiedad.tipo = 'b'
                    if texto_json[npr]['tipo'] == 'decimal':
                        propiedad.tipo = 'd'
                    if texto_json[npr]['tipo'] == 'hora':
                        propiedad.tipo = 'e'
                    if texto_json[npr]['tipo'] == 'richtextbox':
                        propiedad.tipo = 'h'
                    if texto_json[npr]['tipo'] == 'fecha':
                        propiedad.tipo = 'n'
                    if texto_json[npr]['tipo'] == 'imagen':
                        propiedad.tipo = 'p'
                    if texto_json[npr]['tipo'] == 'radiobutton':
                        propiedad.tipo = 'r'
                        propiedad.textobotones = texto_json[npr]['texto_botones'] 
                    if texto_json[npr]['tipo'] == 'foranea':
                        propiedad.tipo = 'f'
                        propiedad.foranea = texto_json[npr]['clase_foranea'] 
                    if texto_json[npr]['tipo'] == 'horafecha':
                        propiedad.tipo = 't'
                    if texto_json[npr]['tipo'] == 'textfield':
                        propiedad.tipo = 'x'

                    propiedad.save()

import re

class ProcesarObjetoView(TemplateView):
    template_name = "proyectos/proyecto_procesa_objeto.html"

    def get_context_data(self,**kwargs):
        context = super(ProcesarObjetoView, self).get_context_data(**kwargs)
        proyecto_objeto = ProyectoObjeto.objects.get(id=self.request.GET['id'])
        # texto_procesar = str(proyecto_objeto.textoobjetos)
        texto_procesar = rutinas.SinTags(proyecto_objeto.texto_objeto)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['error'] = ''
        context['error_texto'] = ''
        context['criterio'] = self.request.GET['criterio']
        context['lista_errores'] = None

        texto = texto_procesar.split('\n')
        lista_proyectos = []
        lista_aplicaciones = []
        lista_modelos = []
        lista_propiedades = []
        lista_reglas= []
        lista_errores = []

        lista_propiedades_proyecto = []
        lista_propiedades_modelo = []
        lista_propiedades_aplicacion = []
        lista_propiedades_propiedad = []

        lista_app = []
        lista_mod = []
        lista_prop = []
        lista_reg = []

        lpr = ['description','type','foreign','buttonstext','lenght','inlist','sections']
        ltp = ['boolean','decimal','time','foreign','richtext','integer','smallinteger','longinteger','date','image','radiobutton','string','datetime','user','textfield']
        lpm = ['description','parent','self','delete','menuoption']
        lpa = ['description','menuoption']
        lpp = ['description','safety','roles','search']        

        para_error = ''

        try:
            # try:
            #     proyecto_anterior = Proyecto.objects.get(id=proyecto_objeto.proyecto)
            #     # Recuperar las aplicaciones
            #     for aplicacion in Aplicacion.objects.filter(proyecto = proyecto_anterior):
            #         lista_app.append(aplicacion)
            #         for modelo in Modelo.objects.filter(aplicacion = aplicacion,proyecto=proyecto_anterior):
            #             lista_mod.append(modelo)
            #             for propiedad in Propiedad.objects.filter(modelo =  modelo):
            #                 lista_prop.append(propiedad)
            #                 for regla in Regla.objects.filter(propiedad=propiedad):
            #                     lista_reg.append(regla)

            #     # Proyecto.objects.get(id=proyecto_objeto.proyecto).delete()
            # except:
            #     proyecto_anterior = None            
            loQueSeCrea = ''
            for txt in texto:
                para_error = txt
                if len(txt) > 1 and txt.strip()[0] != '#':
                    # procesar una linea
                    errores=[]
                    antes_punto,antes_igual,antes_abierto,antes_cerrado,antes_final,error_puntos,error_igual,error_abierto,error_cerrado,errores = ProcesaLinea(txt)
                    # procesar el conjunto de variables de la linea
                    if error_puntos != '':
                        errores.append(error_puntos)
                    if error_igual != '':
                        errores.append(error_igual)
                    if error_abierto != '':
                        errores.append(error_abierto)
                    if error_cerrado != '':
                        errores.append(error_cerrado)
                    if antes_abierto != 'new' and antes_abierto !='':
                        # errores.append('En la linea ' + '"' + txt + '"' + ', la palabra antes de un ( debe ser siempre "new" y es: "' + antes_abierto + '"')
                        errores.append(['En la linea ',txt,'la palabra antes de un "(" debe ser siempre "new" y es: "' + antes_abierto + '"'])
                    elif antes_igual == '':
                        errores.append(['En la linea ',txt,' la palabra antes de un "=" debe existir y ser valida y esta vacia'])
                    elif antes_final != '' and (antes_abierto != '' or antes_cerrado != ''):
                        errores.append(['En la linea ',txt,' si la instruccion es la asignacion de una propiedad no deben existir el par "()"'])
                    elif antes_final != '' and (antes_abierto == '' and antes_cerrado == '') and (antes_punto == ''):
                        errores.append(['En la linea ',txt,' si la instruccion es la asignacion de una propiedad debe existir el objeto de asignacion'])
                    elif antes_final != '' and (antes_abierto == '' and antes_cerrado == '') and (antes_punto != ''):
                        # asignacion de una propiedad
                        # Ver si es de un proyecto
                        flgExisteObjeto = False
                        if loQueSeCrea == 'proyecto':
                            for pr in lista_proyectos:
                                if antes_punto == pr:
                                    flgExisteObjeto = True
                                    # propiedad para un proyecto
                                    # Lista de propiedades de un proyecto
                                    # lpp = 'description safety roles search'
                                    flgEsta = False
                                    for lp in lpp:
                                        if lp == antes_igual:
                                            flgEsta=True
                                            break
                                    if not flgEsta:
                                        errores.append(['En la linea ',txt, '  ' + antes_igual + ' no es una propiedad permitida para el proyecto'])
                                    else:
                                        for lp in lista_propiedades_proyecto:
                                            if lp['nombre'] == antes_punto:
                                                lp[antes_igual] = str(antes_final)
                        # Ver si es de una aplicacion
                        if loQueSeCrea == 'aplicacion':
                            for app in lista_aplicaciones:
                                if app == antes_punto:
                                    flgExisteObjeto = True
                                    # propiedad para una aplicacion
                                    # Lista de propiedades de una aplicacion
                                    flgEsta = False
                                    for lp in lpa:
                                        if lp == antes_igual:
                                            flgEsta=True
                                            break
                                    if not flgEsta:
                                        errores.append(['En la linea ',txt, '  ' + '"' + antes_igual + '"' + ' no es una propiedad permitida para la aplicacion'])
                                    else:
                                        for lp in lista_propiedades_aplicacion:
                                            if lp['nombre'] == antes_punto:
                                                lp[antes_igual] = str(antes_final)
                        # Ver si es de un modelo
                        if loQueSeCrea == 'modelo':
                            for mod in lista_modelos:
                                if mod[1] == antes_punto:
                                    flgExisteObjeto = True
                                    # propiedad para un modelo
                                    # Lista de propiedades de un modelo
                                    flgEsta = False
                                    for lp in lpm:
                                        if lp == antes_igual:
                                            flgEsta=True
                                            break
                                    if not flgEsta:
                                        errores.append(['En la linea ',txt,'"' + antes_igual + '"' +  ' no es una propiedad permitida para el modelo'])
                                    else:
                                        for lp in lista_propiedades_modelo:
                                            if lp['nombre'] == antes_punto:
                                                lp[antes_igual] = str(antes_final)
                        # Ver si es de una propiedad

                        if loQueSeCrea == 'propiedad':
                            for prop in lista_propiedades:
                                if prop[1] == antes_punto:
                                    flgExisteObjeto = True
                                    # propiedad para una propiedad
                                    # Lista de propiedades de una propiedad
                                    flgEsta = False
                                    for lp in lpr:
                                        if lp == antes_igual:
                                            flgEsta=True
                                            break
                                    if not flgEsta:
                                        errores.append(['En la linea ',txt, '"' + antes_igual + '"' +  ' no es una propiedad permitida para la propiedad'])
                                    else:
                                        if antes_igual == 'type':
                                            flgEsta = False
                                            for lt in ltp:
                                                if lt == antes_final:
                                                    flgEsta = True
                                                    break
                                            if not flgEsta:
                                                errores.append(['En la linea ',txt, '"' + antes_final + '"' + ', no corresponde a un tipo valido de propiedad'])
                                    for lp in lista_propiedades_propiedad:
                                        if lp['nombre'] == antes_punto:
                                            lp[antes_igual] = str(antes_final)
                        if not flgExisteObjeto:
                            errores.append(['En la linea ',txt, '"' +  '  ' + antes_punto + '"' + ', no es un modelo aun definido'])

                    elif antes_final == '' and (antes_abierto != '' and antes_cerrado != '') and (antes_punto == ''):
                        # Creacion de un proyecto nuevo
                        if antes_cerrado != 'project':
                            errores.append(['En la linea ',txt, ' la creacion de un nuevo proyecto debe tener la palabra project entre "()"'])
                        elif len(lista_proyectos) > 1:
                            errores.append(['En la linea ',txt,' solo puede existir una linea para la creacion de un nuevo proyecto'])
                        else:
                            lista_proyectos.append(antes_igual)
                            context['nombre_proyecto'] = antes_igual
                            propiedades = {'nombre':antes_igual,'description':'','safety':False,'roles':False,'search':False}
                            lista_propiedades_proyecto.append(propiedades)
                            loQueSeCrea = 'proyecto'
                    elif antes_final == '' and (antes_abierto != '' and antes_cerrado != '') and (antes_punto != ''):
                        # Creacion de un objeto no proyecto
                        if antes_cerrado == 'aplication':
                            # se crea una aplicacion
                            no_proyecto = True
                            for pr in lista_proyectos:
                                if pr == antes_punto:
                                    # el proyecto existe
                                    no_proyecto = False
                                    break
                            if not no_proyecto:
                                no_aplicacion = True
                                for app in lista_aplicaciones:
                                    if app == antes_punto:
                                        errores.append(['En la linea ',txt,' la aplicacion '+ '"' + antes_punto + '"' + ' ya existe'])
                                        no_aplicacion = False
                                        break
                                if no_aplicacion:
                                    lista_aplicaciones.append(antes_igual)
                                    propiedades = {'nombre':antes_igual,'description':'','menuoption':''}
                                    lista_propiedades_aplicacion.append(propiedades)
                                    loQueSeCrea = 'aplicacion'
                            else:
                                errores.append(['En la linea ',txt,' el proyecto ' + '"' + antes_punto + '"' + ' no existe'])
                        elif antes_cerrado == 'model':
                            no_aplicacion = True
                            for app in lista_aplicaciones:
                                if app == antes_punto:
                                    no_aplicacion=False
                                    break
                            if no_aplicacion:
                                errores.append(['En la linea ',txt,', la aplicacion ' + '"' + antes_punto + '"' + ' no esta definida'])
                            else:
                                no_modelo = True
                                for mod in lista_modelos:
                                    if antes_punto + ',' + antes_igual == mod:
                                        errores.append(['En la linea ',txt,' el modelo ' + '"' + antes_igual + '"' + ' ya fue definido para la aplicacion: ' + '"' + antes_punto + '"'])
                                        no_modelo=False
                                        break
                                if no_modelo:
                                    lista_modelos.append([antes_punto,antes_igual])
                                    propiedades = {'nombre':antes_igual,'description':'','menuoption':'','parent':'nada','self':'','delete':'','menuoption':''}
                                    lista_propiedades_modelo.append(propiedades)
                                    loQueSeCrea = 'modelo'
                        elif antes_cerrado == 'property':
                            no_modelo = True
                            for mod in lista_modelos:
                                if mod[1] == antes_punto:
                                    no_modelo=False
                                    break
                            if no_modelo:
                                errores.append(['En la linea ',txt,' el modelo ' + '"' + antes_punto + '"' + ' debe estar definido antes de crear una propiedad'])
                            else:
                                no_propiedad=True
                                for prop in lista_propiedades:
                                    if antes_punto + ',' + antes_igual == prop:
                                        no_propiedad = False
                                        break
                                if no_propiedad:
                                    lista_propiedades.append([antes_punto,antes_igual])
                                    propiedades = {'nombre':antes_igual,'description':'','type':'string','foreign':'nada','buttonstext':'','lenght':30,'inlist':False,'sections':1}
                                    lista_propiedades_propiedad.append(propiedades)
                                    loQueSeCrea = 'propiedad'
                                    
                    for er in errores:
                        lista_errores.append(er)
            if len(lista_errores) > 0:                
                context['lista_errores'] = lista_errores
                context['numero_errores'] = len(lista_errores)
            else:
                context['lista_errores'] = ''
                context['numero_errores'] = 0
                # Construye el proyecto
                if len(lista_proyectos) == 0:
                    lista_errores.append('Debe existir al menos un proyecto definido')
                    context['lista_errores'] = lista_errores
                    context['numero_errores'] = len(lista_errores)
                else:
                    # construye el proyecto
                    proyecto = Proyecto()
                    proyecto.nombre = lista_proyectos[0]
                    for pr in lista_propiedades_proyecto:
                        if pr['nombre'] == proyecto.nombre:
                            try:
                                proyecto.descripcion = pr['description']
                            except:
                                pass
                            try:
                                proyecto.seguridad = True if pr['safety'] == 'True' else False
                            except:
                                pass
                            try:
                                proyecto.conroles = True if pr['roles'] == 'True' else False
                            except:
                                pass
                            try:
                                proyecto.busqueda = True if pr['search'] == 'True' else False
                            except:
                                pass
                            try:
                                proyecto.usuario = self.request.user
                            except:
                                pass
                    proyecto.save()
                    context['proyecto'] = proyecto
                    # aplicaciones
                    for app in lista_aplicaciones:
                        aplicacion = Aplicacion()
                        aplicacion.nombre = app
                        for pr in lista_propiedades_aplicacion:
                            if pr['nombre'] == aplicacion.nombre:
                                try:
                                    aplicacion.descripcion = pr['description']
                                except:
                                    pass
                                try:
                                    aplicacion.textoenmenu = pr['menuoption']
                                except:
                                    pass
                        aplicacion.proyecto = proyecto
                        aplicacion.save()
                    # modelos
                    for mod in lista_modelos:
                        modelo = Modelo()
                        modelo.nombre = mod[1]
                        for pr in lista_propiedades_modelo:
                            if pr['nombre'] == modelo.nombre:
                                try:
                                    modelo.descripcion = pr['description']
                                except:
                                    pass
                                try:
                                    modelo.textoenmenu = pr['menuoption']
                                except:
                                    pass
                                try:
                                    modelo.padre = pr['parent']
                                except:
                                    pass
                                try:
                                    modelo.nombreself = pr['self']
                                except:
                                    pass
                                try:
                                    modelo.nombreborrar = pr['delete']
                                except:
                                    pass
                        app = Aplicacion.objects.get(nombre = mod[0], proyecto=proyecto)
                        modelo.aplicacion = app
                        modelo.proyecto = proyecto
                        modelo.save()
                    # propiedades
                    for prop in lista_propiedades:
                        propiedad = Propiedad()
                        propiedad.nombre = prop[1]

                        for pr in lista_propiedades_propiedad:
                            if pr['nombre'] == propiedad.nombre:
                                try:
                                    prop.descripcion = pr['description']
                                except:
                                    pass
                                try:
                                    for tp in ltp:
                                        if tp == pr['type']:
                                            if tp == 'boolean':
                                                propiedad.tipo = 'b'
                                            if tp == 'decimal':
                                                propiedad.tipo = 'd'
                                            if tp == 'time':
                                                propiedad.tipo = 'e'
                                            if tp == 'foreign':
                                                propiedad.tipo = 'f'
                                            if tp == 'richtext':
                                                propiedad.tipo = 'h'
                                            if tp == 'integer':
                                                propiedad.tipo = 'i'
                                            if tp == 'smallinteger':
                                                propiedad.tipo = 'm'
                                            if tp == 'longinteger':
                                                propiedad.tipo = 'l'
                                            if tp == 'date':
                                                propiedad.tipo = 'n'
                                            if tp == 'image':
                                                propiedad.tipo = 'p'
                                            if tp == 'radiobutton':
                                                propiedad.tipo = 'r'
                                            if tp == 'string':
                                                propiedad.tipo = 's'
                                            if tp == 'datetime':
                                                propiedad.tipo = 't'
                                            if tp == 'user':
                                                propiedad.tipo = 'u'
                                            if tp == 'textfield':
                                                propiedad.tipo = 'x'
                                            break
                                except:
                                    pass
                                try:
                                    propiedad.foranea = pr['foreign']
                                except:
                                    pass
                                try:
                                    propiedad.textobotones = pr['buttonstext']
                                except:
                                    pass
                                try:
                                    propiedad.largostring = pr['lenght']
                                except:
                                    pass
                                try:
                                    propiedad.enlista = True if pr['inlist'] == 'True' else False
                                except:
                                    pass
                                try:
                                    propiedad.numerocolumnas = pr['sections']
                                except:
                                    pass
                                break

                        mod = Modelo.objects.get(nombre = prop[0], proyecto=proyecto)
                        propiedad.modelo = mod
                        propiedad.save()

            proyecto_objeto.proyecto = proyecto.id
            proyecto_objeto.save()

            # if proyecto_anterior != None:                                    
            #     # Reconstruir los datos del proyecto anterior en el proyecto nuevo
            #     Reconstruye(proyecto,proyecto_anterior,lista_app,lista_mod,lista_prop)

        except Exception as e:
            lista_errores.append('Existe error en la construccion del Texto: ' + ' ' + str(e) + ' en la linea ' + para_error)
            context['lista_errores'] = lista_errores
            context['numero_errores'] = len(lista_errores)

        return context

def ProcesaLinea(linea_texto):
    antes_igual = ''
    antes_punto = ''
    antes_abierto = ''
    antes_cerrado = ''
    antes_final  = ''
    num_puntos = 0
    num_abierto = 0
    num_cerrado = 0
    num_igual = 0
    error_puntos = ''
    error_abierto = ''
    error_cerrado = ''
    error_igual = ''

    palabra = ''
    for caracter in linea_texto:
        if caracter == '.':
            if num_puntos == 0:
                num_puntos +=1
                antes_punto = palabra.strip()
                palabra = ''
            else:
                palabra += caracter
        elif caracter == '=':
            num_igual += 1
            antes_igual = palabra.strip()
            palabra = ''
        elif caracter == '(':
            num_abierto +=1
            antes_abierto = palabra.strip()
            palabra = ''
        elif caracter == ')':
            num_cerrado += 1
            antes_cerrado = palabra.strip()
            palabra = ''
        else:
            # if caracter != ' ':
            palabra += caracter

    antes_final = palabra.strip()
    error_final = rutinas.TextoValido(antes_final)

    error_punto = rutinas.VerificarSoloLetras(antes_punto.strip())
    error_igual = rutinas.VerificarSoloLetras(antes_igual.strip())
    error_abierto = rutinas.VerificarSoloLetras(antes_abierto.strip())
    error_cerrado = rutinas.VerificarSoloLetras(antes_cerrado.strip())
    error_numero_punto = rutinas.NoNumeroInicio(antes_punto.strip())
    error_numero_igual = rutinas.NoNumeroInicio(antes_igual.strip())
    error_numero_cerrado = rutinas.NoNumeroInicio(antes_cerrado.strip())
    error_numero_abierto = rutinas.NoNumeroInicio(antes_abierto.strip())

    if num_puntos>1:
        error_puntos = 'Solo debe existir un caracter "." en la linea'
    if num_igual>1:
        error_igual = 'Solo debe existir un caracter "=" en la linea'
    if num_abierto>1:
        error_abierto = 'Solo debe existir un caracter "(" en la linea'
    if num_cerrado>1:
        error_cerrado = 'Solo debe existir un caracter ")" en la linea'
        
    errores = []
    hay_errores = False

    if error_punto != '':
        errores.append('La palabra ' + antes_punto +  error_punto)
        hay_errores = True
    if error_igual != '':
        errores.append('La palabra ' + antes_igual +  error_igual)
        hay_errores = True
    if error_abierto != '':
        errores.append('La palabra ' + antes_abierto + error_abierto)
        hay_errores = True
    if error_cerrado != '':
        errores.append('La palabra ' + antes_cerrado + error_cerrado)
        hay_errores = True
    if error_numero_punto != '':
        errores.append('La palabra ' + antes_punto + error_numero_punto)
        hay_errores = True
    if error_numero_igual != '':
        errores.append('La palabra ' + antes_igual + error_numero_igual)
        hay_errores = True
    if error_numero_abierto != '':
        errores.append('La palabra ' + antes_abierto + error_numero_abierto)
        hay_errores = True
    if error_numero_cerrado != '':
        errores.append('La palabra ' + antes_cerrado + error_numero_cerrado)
        hay_errores = True
    if error_final != '':
        errores.append('La palabra final ' + error_final)
        hay_errores = True

    if hay_errores:
        errores.insert(0, 'Los errores en la linea ' + linea_texto + ' son: ') 

    return antes_punto,antes_igual,antes_abierto,antes_cerrado,antes_final,error_puntos,error_igual,error_abierto,error_cerrado,errores


class ProcesaTextoConCriterioView(TemplateView):
    template_name = "proyectos/proyecto_procesa_texto.html"
    numre=1
    def get_context_data(self,**kwargs):
        context = super(ProcesaTextoConCriterioView, self).get_context_data(**kwargs)
        texto_procesar = ProyectoTexto.objects.get(id=self.request.GET['id'])
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['error'] = ''
        context['error_texto'] = ''
        context['criterio'] = self.request.GET['criterio']

        caracteres_especiales = []
        caracteres_especiales.append(['&#39;',"'"])
        caracteres_especiales.append(['&quot;','"'])
        caracteres_especiales.append(['&lt;','<'])
        caracteres_especiales.append(['&gt;','>'])

        Texto = rutinas.SinTags(texto_procesar.texto_texto)

        # Cambiar caracteres espaciales

        for car in caracteres_especiales:
            Texto = Texto.replace(car[0],car[1])
            
        # Comienza en proceso
        # Proyecto que se crea
        tag = ''

        lista_app = []
        lista_mod = []
        lista_prop = []
        lista_reg = []
        lista_seccion=[]
        lista_fila=[]
        lista_columna=[]
        lista_sec=[]
        lista_fil=[]
        lista_col=[]
        lista_secp=[]
        lista_filp=[]
        lista_colp=[]
        lista_perso = []

        try:
            # Procesa texto
            proyecto = Proyecto()
            aplicacion = None
            modelo = None
            propiedad = None
            regla = None
            nap = 1
            nmo = 1
            npr = 1
            nrg = 1
            proyecto.usuario = self.request.user
            context['mensaje'] = Texto
            strTexto = Texto.split('[')
            numre=2

            for parrafo in strTexto:
                if parrafo != '':
                    strTag = parrafo.split(']')
                    elemento = strTag[0].replace('&nbsp;',' ').split(' ')
                    elementos = ''
                    for i in range(len(elemento)):
                        if i != 0:
                            if i < len(elemento)-1 :
                                elementos += elemento[i] + ' '
                            else:
                                elementos += elemento[i]
                    tag = elemento[0]
                    if tag == 'npr':
                        proyecto.nombre =  ProcesaTags(elementos,'nuevo')
                    if tag == 'dpr':
                        proyecto.descripcion =  ProcesaTags(elementos,'Descripcion')
                    if tag == 'tit':
                        proyecto.titulo =  ProcesaTags(elementos,'Titulo')
                    if tag == 'pcs':
                        proyecto.conseguridad =  True
                    if tag == 'pcr':
                        proyecto.conroles =  True
                    if tag == 'pcb':
                        proyecto.conbusqueda =  True
                    numre=3
                    proyecto.save()
                    numre=33
                    numre=3

                    # Aplicaciones
                    if tag == 'nap':
                        aplicacion = Aplicacion()
                        aplicacion.proyecto = proyecto
                        aplicacion.nombre = ProcesaTags(elementos,'app' + str(nap))
                        nap += 1
                        aplicacion.save()
                    if aplicacion != None:
                        if tag == 'dap':
                            aplicacion.descripcion = ProcesaTags(elementos,'app desc')
                        if tag == 'txma':
                            aplicacion.textoenmenu = ProcesaTags(elementos,'app desc')
                        aplicacion.save()
                    # Modelos
                    numre=4
                    if tag == 'nmo':
                        modelo = Modelo()
                        modelo.proyecto = proyecto
                        modelo.aplicacion = aplicacion
                        modelo.nombre = ProcesaTags(elementos,'modelo' + str(nmo))
                        nmo += 1
                        modelo.save()
                    if modelo != None:
                        if tag == 'dmo':
                            modelo.descripcion = ProcesaTags(elementos,'modelo' + str(nmo))
                        if tag == 'smo':
                            modelo.nombreself = ProcesaTags(elementos,'modelo' + str(nmo))
                        if tag == 'bmo':
                            modelo.nombreborrar = ProcesaTags(elementos,'modelo' + str(nmo))
                        if tag == 'pmo':
                            modelo.padre = ProcesaTags(elementos,'modelo' + str(nmo))
                        if tag == 'tom':
                            modelo.textoopcionmenu = ProcesaTags(elementos,'modelo' + str(nmo))
                        modelo.save()
                        numre=82

                    # Propiedades
                    numre=12

                    if tag == 'npro':
                        propiedad = Propiedad()
                        propiedad.modelo = modelo
                        propiedad.nombre = ProcesaTags(elementos,'propiedad' + str(npr))
                        npr += 1
                        propiedad.save()
                    if propiedad != None:
                        if tag == 'dpro':
                            propiedad.descripcion = ProcesaTags(elementos,'propiedad' + str(npr))
                        if tag == 'tpro':
                            propiedad.tipo = ProcesaTags(elementos,propiedad.tipo)
                        if tag == 'prf':
                            propiedad.foranea = ProcesaTags(elementos,propiedad.foranea)
                        if tag == 'txb':
                            propiedad.textobotones = ProcesaTags(elementos,propiedad.textobotones)
                        if tag == 'lst':
                            propiedad.largostring = ProcesaTags(elementos,propiedad.largostring)
                        if tag == 'vdf':
                            propiedad.valorinicial = ProcesaTags(elementos,propiedad.valorinicial)
                        if tag == 'tph':
                            propiedad.textoplaceholder = ProcesaTags(elementos,propiedad.textoplaceholder)
                        if tag == 'epro':
                            propiedad.etiqueta = ProcesaTags(elementos,propiedad.etiqueta)
                        if tag == 'enl':
                            propiedad.enlista = True
                        if tag == 'emb':
                            propiedad.enmobile = True
                        if tag == 'pbl':
                            propiedad.participabusquedalista = True
                        if tag == 'tlz':
                            propiedad.totaliza = True
                        propiedad.save()

                    # Reglas
                    if tag == 'msj':
                        regla = Regla()
                        regla.propiedad = propiedad
                        regla.mensaje = ProcesaTags(elementos,'regla' + str(nrg))
                        nrg += 1
                    if regla != None:
                        if tag == 'crg':
                            elementos = elementos.replace('~','[')
                            elementos = elementos.replace('@',']')
                            regla.codigo = ProcesaTags(elementos,regla.codigo)
                        regla.save()

            texto_procesar.proyecto = proyecto.id
            texto_procesar.save()

            rutinas.CrearSeccionProyecto(proyecto)
            context['proyecto'] = proyecto
            
            # if proyecto_anterior != None:                                    
            #     # Reconstruir los datos del proyecto anterior en el proyecto nuevo
            #     Reconstruye(proyecto,proyecto_anterior,lista_app,lista_mod,lista_prop)
        except Exception as e:
            context['error_texto'] = 'Existe error en la construccion del Texto: ' + ' ' + str(e) + str(numre)
        return context

def Reconstruye(proyecto, proyecto_anterior, lista_app, lista_mod, lista_prop):
    # Reconstruir los datos del proyecto anterior en el proyecto nuevo
    proyecto.avatar = proyecto_anterior.avatar
    proyecto.imagentitulo = proyecto_anterior.imagentitulo

    # Secciones de la pagina principal proyecto
    for seccion in Seccion.objects.filter(proyecto=proyecto_anterior):
        seccion.proyecto = proyecto
        seccion.save()

    # Secciones de la pagina inicial proyecto
    for seccion in Secp.objects.filter(proyecto=proyecto_anterior):
        seccion.proyecto = proyecto
        seccion.save()

    # Personalizacion del proyecto
    for perso in Personaliza.objects.filter(proyecto=proyecto_anterior):
        perso.proyecto = proyecto
        perso.save()

    # b) Aplicaciones
    for aplicacion in Aplicacion.objects.filter(proyecto = proyecto):
        for aplicacion_anterior in lista_app:
            if aplicacion.nombre == aplicacion_anterior.nombre:
                aplicacion.imagenmenu = aplicacion_anterior.imagenmenu
                aplicacion.fontmenu = aplicacion_anterior.fontmenu
                aplicacion.homelogin = aplicacion_anterior.homelogin
                aplicacion.homestaff = aplicacion_anterior.homestaff
                aplicacion.save()
                # c)Modelos
                for modelo in Modelo.objects.filter(aplicacion = aplicacion,proyecto = proyecto):
                    for modelo_anterior in lista_mod:
                        if modelo.nombre == modelo_anterior.nombre:
                            modelo.imagenmenu = modelo_anterior.imagenmenu
                            modelo.ultimoregistro = modelo_anterior.ultimoregistro
                            modelo.reportsize = modelo_anterior.reportsize
                            modelo.reportorientation = modelo_anterior.reportorientation
                            modelo.titulox = modelo_anterior.titulox
                            modelo.fechax = modelo_anterior.fechax
                            modelo.lineaix = modelo_anterior.lineaix
                            modelo.lineafx = modelo_anterior.lineafx
                            modelo.grosorlinea = modelo_anterior.grosorlinea
                            modelo.datoinicialx = modelo_anterior.datoinicialx
                            modelo.identacionautomatica = modelo_anterior.identacionautomatica
                            modelo.margenes = modelo_anterior.margenes
                            modelo.font_titulo = modelo_anterior.font_titulo
                            modelo.font_titulo_size = modelo_anterior.font_titulo_size
                            modelo.font_columnas = modelo_anterior.font_columnas
                            modelo.font_columnas_size = modelo_anterior.font_columnas_size
                            modelo.font = modelo_anterior.font
                            modelo.font_size = modelo_anterior.font_size
                            modelo.font_encabezado = modelo_anterior.font_encabezado
                            modelo.font_encabezado_size = modelo_anterior.font_encabezado_size
                            modelo.identa = modelo_anterior.identa
                            modelo.save()
                            # Secciones del modelo
                            for seccion in Sec.objects.filter(modelo=modelo_anterior):
                                seccion.modelo = modelo
                                seccion.save()


                            # d) Propiedades

                            for propiedad in Propiedad.objects.filter(modelo = modelo):
                                for propiedad_anterior in lista_prop:
                                    if propiedad.nombre == propiedad_anterior.nombre:
                                        propiedad.save()
                                        for reg in Regla.objects.filter(propiedad=propiedad):
                                            reg.propiedad = propiedad
                                            reg.save
                                        break
                                        
                            break
                break

class ProcesaTextoView(TemplateView):
    template_name = "proyectos/proyecto_procesa_texto.html"

    def get_context_data(self,**kwargs):
        context = super(ProcesaTextoView, self).get_context_data(**kwargs)
        texto_procesar = ProyectoTexto.objects.get(id=self.request.GET['id'])
        try:
            Proyecto.objects.get(id=texto_procesar.proyecto).delete()
        except:
            pass
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['error'] = ''
        context['criterio'] = self.request.GET['criterio']

        caracteres_especiales = []
        caracteres_especiales.append(['&#39;',"'"])
        caracteres_especiales.append(['&quot;','"'])
        caracteres_especiales.append(['&lt;','<'])
        caracteres_especiales.append(['&gt;','>'])
        Texto = texto_procesar.texto

        # Cambiar caracteres espaciales

        for car in caracteres_especiales:
            Texto = Texto.replace(car[0],car[1])
            
        # Comienza en proceso
        # Proyecto que se crea
        tag = ''

        try:
            proyecto = Proyecto()
            aplicacion = None
            modelo = None
            propiedad = None
            regla = None
            nap = 1
            nmo = 1
            npr = 1
            nrg = 1
            proyecto.usuario = self.request.user
            context['mensaje'] = Texto
            strTexto = Texto.split('[')
            for parrafo in strTexto:
                if parrafo != '':
                    strTag = parrafo.split(']')
                    elemento = strTag[0].replace('&nbsp;',' ').split(' ')
                    elementos = ''
                    for i in range(len(elemento)):
                        if i != 0:
                            if i < len(elemento)-1 :
                                elementos += elemento[i] + ' '
                            else:
                                elementos += elemento[i]
                    tag = elemento[0]
                    if tag == 'npr':
                        proyecto.nombre =  ProcesaTags(elementos,'nuevo')
                    if tag == 'dpr':
                        proyecto.descripcion =  ProcesaTags(elementos,'Descripcion')
                    if tag == 'cpp':
                        proyecto.colorpaginaprincipal =  ProcesaTags(elementos,proyecto.colorpaginaprincipal)
                    if tag == 'tit':
                        proyecto.titulo =  ProcesaTags(elementos,proyecto.titulo)
                    if tag == 'pcs':
                        proyecto.conseguridad =  True
                    if tag == 'pcr':
                        proyecto.conroles =  True
                    if tag == 'pce':
                        proyecto.conetiquetaspersonalizacion = True
                    if tag == 'pcb':
                        proyecto.conbusqueda = True
                    if tag == 'avw':
                        proyecto.avatarwidth = ProcesaTags(elementos,proyecto.avatarwidth)
                    if tag == 'ses':
                        proyecto.separacionsecciones = ProcesaTags(elementos,proyecto.separacionsecciones)
                    if tag == 'avh':
                        proyecto.avatarheight = ProcesaTags(elementos,proyecto.avatarheight)
                    if tag == 'itw':
                        proyecto.imagentitulowidth = ProcesaTags(elementos,proyecto.imagentitulowidth)
                    if tag == 'ith':
                        proyecto.imagentituloheight = ProcesaTags(elementos,proyecto.imagentituloheight)
                    if tag == 'fti':
                        proyecto.fonttitulo = ProcesaTags(elementos,proyecto.fonttitulo)
                    if tag == 'cti':
                        proyecto.colortitulo = ProcesaTags(elementos,proyecto.colortitulo)
                    if tag == 'act':
                        proyecto.altocolumnatitulo = ProcesaTags(elementos,proyecto.altocolumnatitulo)
                    if tag == 'nct':
                        proyecto.numerocolumnatitulo = ProcesaTags(elementos,proyecto.numerocolumnatitulo)
                    if tag == 'cct':
                        proyecto.colorcolumnatitulo = ProcesaTags(elementos,proyecto.colorcolumnatitulo)
                    if tag == 'jht':
                        proyecto.justificacionhorizontaltitulo = ProcesaTags(elementos,proyecto.justificacionhorizontaltitulo)
                    if tag == 'jvt':
                        proyecto.justificacionverticaltitulo = ProcesaTags(elementos,proyecto.justificacionverticaltitulo)
                    if tag == 'afs':
                        proyecto.altofilaenizcede = ProcesaTags(elementos,proyecto.altofilaenizcede)
                    if tag == 'cfs':
                        proyecto.colorfilaenizcede = ProcesaTags(elementos,proyecto.colorfilaenizcede)
                    if tag == 'nci':
                        proyecto.numerocolumnaenizquierda = ProcesaTags(elementos,proyecto.numerocolumnaenizquierda)
                    if tag == 'aci':
                        proyecto.altocolumnaenizquierda = ProcesaTags(elementos,proyecto.altocolumnaenizquierda)
                    if tag == 'cci':
                        proyecto.colorcolumnaenizquierda = ProcesaTags(elementos,proyecto.colorcolumnaenizquierda)
                    if tag == 'ncd':
                        proyecto.numerocolumnaenderecha = ProcesaTags(elementos,proyecto.numerocolumnaenderecha)
                    if tag == 'acd':
                        proyecto.altocolumnaenderecha = ProcesaTags(elementos,proyecto.altocolumnaenderecha)
                    if tag == 'ccd':
                        proyecto.colorcolumnaenderecha = ProcesaTags(elementos,proyecto.colorcolumnaenderecha)
                    if tag == 'ncl':
                        proyecto.numerocolumnalogo = ProcesaTags(elementos,proyecto.numerocolumnalogo)
                    if tag == 'acl':
                        proyecto.altocolumnalogo= ProcesaTags(elementos,proyecto.altocolumnalogo)
                    if tag == 'ccl':
                        proyecto.colorcolumnalogo = ProcesaTags(elementos,proyecto.colorcolumnalogo)
                    if tag == 'jhl':
                        proyecto.justificacionhorizontallogo = ProcesaTags(elementos,proyecto.justificacionhorizontallogo)
                    if tag == 'jvl':
                        proyecto.justificacionverticallogo = ProcesaTags(elementos,proyecto.justificacionverticallogo)
                    if tag == 'ncg':
                        proyecto.numerocolumnalogin = ProcesaTags(elementos,proyecto.numerocolumnalogin)
                    if tag == 'acg':
                        proyecto.altocolumnalogin = ProcesaTags(elementos,proyecto.altocolumnalogin)
                    if tag == 'ccg':
                        proyecto.colorcolumnalogin = ProcesaTags(elementos,proyecto.colorcolumnalogin)
                    if tag == 'bss':
                        proyecto.enborde = True
                    if tag == 'cbss':
                        proyecto.encolorborde = ProcesaTags(elementos,proyecto.encolorborde)
                    if tag == 'abss':
                        proyecto.enanchoborde = ProcesaTags(elementos,proyecto.enanchoborde)
                    if tag == 'afb':
                        proyecto.altofilabume = ProcesaTags(elementos,proyecto.altofilabume)
                    if tag == 'cfb':
                        proyecto.colorfilabume = ProcesaTags(elementos,proyecto.colorfilabume)
                    if tag == 'ncbi':
                        proyecto.numerocolumnabumeizquierda = ProcesaTags(elementos,proyecto.numerocolumnabumeizquierda)
                    if tag == 'acbi':
                        proyecto.altocolumnabumeizquierda = ProcesaTags(elementos,proyecto.altocolumnabumeizquierda)
                    if tag == 'ccbi':
                        proyecto.colorcolumnabumeizquierda = ProcesaTags(elementos,proyecto.colorcolumnabumeizquierda)
                    if tag == 'ncbd':
                        proyecto.numerocolumnabumederecha = ProcesaTags(elementos,proyecto.numerocolumnabumederecha)
                    if tag == 'acbd':
                        proyecto.altocolumnabumederecha = ProcesaTags(elementos,proyecto.altocolumnabumederecha)
                    if tag == 'ccbd':
                        proyecto.colorcolumnabumederecha = ProcesaTags(elementos,proyecto.colorcolumnabumederecha)
                    if tag == 'ncb':
                        proyecto.numerocolumnabusqueda = ProcesaTags(elementos,proyecto.numerocolumnabusqueda)
                    if tag == 'acb':
                        proyecto.altocolumnabusqueda = ProcesaTags(elementos,proyecto.altocolumnabusqueda)
                    if tag == 'ccb':
                        proyecto.colorcolumnabusqueda = ProcesaTags(elementos,proyecto.colorcolumnabusqueda)
                    if tag == 'ncm':
                        proyecto.numerocolumnamenu = ProcesaTags(elementos,proyecto.numerocolumnamenu)
                    if tag == 'acm':
                        proyecto.altocolumnamenu = ProcesaTags(elementos,proyecto.altocolumnamenu)
                    if tag == 'ccm':
                        proyecto.colorcolumnamenu = ProcesaTags(elementos,proyecto.colorcolumnamenu)
                    if tag == 'cme':
                        proyecto.colormenu = ProcesaTags(elementos,proyecto.colormenu)
                    if tag == 'fme':
                        proyecto.fontmenu = ProcesaTags(elementos,proyecto.fontmenu)
                    if tag == 'jum':
                        proyecto.justificacionmenu = ProcesaTags(elementos,proyecto.justificacionmenu)
                    if tag == 'bme':
                        proyecto.bumeborde = True
                    if tag == 'cbme':
                        proyecto.bumecolorborde = ProcesaTags(elementos,proyecto.bumecolorborde)
                    if tag == 'abme':
                        proyecto.bumeanchoborde = ProcesaTags(elementos,proyecto.bumeanchoborde)
                    if tag == 'afm':
                        proyecto.altofilamedio = ProcesaTags(elementos,proyecto.altofilamedio)
                    if tag == 'cfm':
                        proyecto.colorfilamedio = ProcesaTags(elementos,proyecto.colorfilamedio)
                    if tag == 'acmi':
                        proyecto.altocolumnamedioizquierda = ProcesaTags(elementos,proyecto.altocolumnamedioizquierda)
                    if tag == 'ncmi':
                        proyecto.numerocolumnamedioizquierda = ProcesaTags(elementos,proyecto.numerocolumnamedioizquierda)
                    if tag == 'ccmi':
                        proyecto.colorcolumnamedioizquierda = ProcesaTags(elementos,proyecto.colorcolumnamedioizquierda)
                    if tag == 'acmc':
                        proyecto.altocolumnamediocentro = ProcesaTags(elementos,proyecto.altocolumnamediocentro)
                    if tag == 'ncmc':
                        proyecto.numerocolumnamediocentro = ProcesaTags(elementos,proyecto.numerocolumnamediocentro)
                    if tag == 'ccmc':
                        proyecto.colorcolumnamediocentro = ProcesaTags(elementos,proyecto.colorcolumnamediocentro)
                    if tag == 'acmd':
                        proyecto.altocolumnamedioderecha = ProcesaTags(elementos,proyecto.altocolumnamedioderecha)
                    if tag == 'ncmd':
                        proyecto.numerocolumnamedioderecha = ProcesaTags(elementos,proyecto.numerocolumnamedioderecha)
                    if tag == 'ccmd':
                        proyecto.colorcolumnamedioderecha = ProcesaTags(elementos,proyecto.colorcolumnamedioderecha)
                    if tag == 'txm':
                        proyecto.textomedio = ProcesaTags(elementos,proyecto.textomedio)
                    if tag == 'ctxm':
                        proyecto.colortextomedio = ProcesaTags(elementos,proyecto.colortextomedio)
                    if tag == 'ftxm':
                        proyecto.fonttextomedio = ProcesaTags(elementos,proyecto.fonttextomedio)
                    if tag == 'afp':
                        proyecto.altofilapie = ProcesaTags(elementos,proyecto.altofilapie)
                    if tag == 'cfp':
                        proyecto.colorfilapie = ProcesaTags(elementos,proyecto.colorfilapie)
                    if tag == 'afm':
                        proyecto.altofilamedio = ProcesaTags(elementos,proyecto.altofilamedio)
                    if tag == 'acp':
                        proyecto.altocolumnapie = ProcesaTags(elementos,proyecto.altocolumnapie)
                    if tag == 'ccp':
                        proyecto.colorcolumnapie = ProcesaTags(elementos,proyecto.colorcolumnapie)
                    if tag == 'txv':
                        proyecto.textovolver = ProcesaTags(elementos,proyecto.textovolver)
                    if tag == 'ftxv':
                        proyecto.fonttextovolver = ProcesaTags(elementos,proyecto.fonttextovolver)
                    if tag == 'ctxv':
                        proyecto.colortextovolver = ProcesaTags(elementos,proyecto.colortextovolver)
                    if tag == 'mctg':
                        proyecto.menuscotiguos = True
                    if tag == 'bce':
                        proyecto.ceneborde = True
                    if tag == 'cbce':
                        proyecto.cencolorborde = ProcesaTags(elementos,proyecto.bumecolorborde)
                    if tag == 'abce':
                        proyecto.cenanchoborde = ProcesaTags(elementos,proyecto.bumeanchoborde)
                    proyecto.save()
                    # Aplicaciones
                    if tag == 'nap':
                        aplicacion = Aplicacion()
                        aplicacion.proyecto = proyecto
                        aplicacion.nombre = ProcesaTags(elementos,'app' + str(nap))
                        nap += 1
                    if aplicacion != None:
                        if tag == 'dap':
                            aplicacion.descripcion = ProcesaTags(elementos,'app desc')
                        if tag == 'txma':
                            aplicacion.textoenmenu = ProcesaTags(elementos,aplicacion.textoenmenu)
                        if tag == 'tta':
                            aplicacion.tooltip = ProcesaTags(elementos,aplicacion.tooltip)
                        if tag == 'oga':
                            aplicacion.ordengeneracion = ProcesaTags(elementos,aplicacion.ordengeneracion)
                        if tag == 'hlg':
                            aplicacion.homelogin = True
                        if tag == 'hst':
                            aplicacion.homestaff = True
                        aplicacion.save()
                    # Modelos
                    if tag == 'nmo':
                        modelo = Modelo()
                        modelo.proyecto = proyecto
                        modelo.aplicacion = aplicacion
                        modelo.nombre = ProcesaTags(elementos,'modelo' + str(nmo))
                        nmo += 1
                    if modelo != None:
                        if tag == 'dmo':
                            modelo.descripcion = ProcesaTags(elementos,modelo.descripcion)
                        if tag == 'pmo':
                            modelo.padre = ProcesaTags(elementos,modelo.padre)
                        if tag == 'smo':
                            modelo.nombreself = ProcesaTags(elementos,modelo.nombreself)
                        if tag == 'bmo':
                            modelo.nombreborrar = ProcesaTags(elementos,modelo.nombreborrar)
                        if tag == 'amo':
                            napp = ProcesaTags(elementos,aplicacion.nombre)
                            aplicacion = Aplicacion.objects.get(nombre=napp,proyecto=proyecto)
                            modelo.aplicacion = aplicacion
                        if tag == 'tom':
                            modelo.textoopcionmenu = ProcesaTags(elementos,modelo.textoopcionmenu)
                        if tag == 'ttm':
                            modelo.tooltip = ProcesaTags(elementos,modelo.tooltip)
                        if tag == 'tli':
                            modelo.titulolista = ProcesaTags(elementos,modelo.titulolista)
                        if tag == 'ftli':
                            modelo.fonttitulolista = ProcesaTags(elementos,modelo.fonttitulolista)
                        if tag == 'cftl':
                            modelo.colorfondotitulolista = ProcesaTags(elementos,modelo.colorfondotitulolista)
                        if tag == 'ctli':
                            modelo.colortitulolista = ProcesaTags(elementos,modelo.colortitulolista)
                        if tag == 'atli':
                            modelo.altotitulolista = ProcesaTags(elementos,modelo.altotitulolista)
                        if tag == 'mtli':
                            modelo.mayusculastitulolista = True
                        if tag == 'jvtl':
                            modelo.justificacionverticaltitulolista = ProcesaTags(elementos,modelo.justificacionverticaltitulolista)
                        if tag == 'jhtl':
                            modelo.justificacionhorizontaltitulolista = ProcesaTags(elementos,modelo.justificacionhorizontaltitulolista)
                        if tag == 'fcli':
                            modelo.fontcomentariolista = ProcesaTags(elementos,modelo.fontcomentariolista)
                        if tag == 'cli':
                            modelo.comentariolista = ProcesaTags(elementos,modelo.comentariolista)
                        if tag == 'cfcl':
                            modelo.colorfondocomentariolista = ProcesaTags(elementos,modelo.colorfondocomentariolista)
                        if tag == 'ccli':
                            modelo.colorcomentariolista = ProcesaTags(elementos,modelo.colorcomentariolista)
                        if tag == 'mco':
                            modelo.mayusculascolumnas = True
                        if tag == 'aco':
                            modelo.altocolumnas = ProcesaTags(elementos,modelo.altocolumnas)
                        if tag == 'cfcl':
                            modelo.colorfondocolumnaslista = ProcesaTags(elementos,modelo.colorfondocolumnaslista)
                        if tag == 'ccli':
                            modelo.colorcolumnaslista = ProcesaTags(elementos,modelo.colorcolumnaslista)
                        if tag == 'fcli':
                            modelo.fontcolumnaslista = ProcesaTags(elementos,modelo.fontcolumnaslista)
                        if tag == 'clcb':
                            modelo.columnaslistaconborde = True
                        if tag == 'ftxl':
                            modelo.fonttextolista = ProcesaTags(elementos,modelo.fonttextolista)
                        if tag == 'cftxl':
                            modelo.colorfondotextolista = ProcesaTags(elementos,modelo.colorfondotextolista)
                        if tag == 'ctxl':
                            modelo.colortextolista = ProcesaTags(elementos,modelo.colortextolista)
                        if tag == 'feb':
                            modelo.fonteditarborrar = ProcesaTags(elementos,modelo.fonteditarborrar)
                        if tag == 'ceb':
                            modelo.coloreditarborrar = ProcesaTags(elementos,modelo.coloreditarborrar)
                        if tag == 'teb':
                            modelo.textoeditarborrar = ProcesaTags(elementos,modelo.textoeditarborrar)
                        if tag == 'flnm':
                            modelo.fontlinknuevomodelo = ProcesaTags(elementos,modelo.fontlinknuevomodelo)
                        if tag == 'clnm':
                            modelo.colorlinknuevomodelo = ProcesaTags(elementos,modelo.colorlinknuevomodelo)
                        if tag == 'tlnm':
                            modelo.textolinknuevomodelo = ProcesaTags(elementos,modelo.textolinknuevomodelo)
                        if tag == 'lnm':
                            modelo.linknuevomodelo = True
                        if tag == 'tin':
                            modelo.tituloinserta = ProcesaTags(elementos,modelo.tituloinserta)
                        if tag == 'ftin':
                            modelo.fonttituloinserta = ProcesaTags(elementos,modelo.fonttituloinserta)
                        if tag == 'ctin':
                            modelo.colortituloinserta = ProcesaTags(elementos,modelo.colortituloinserta)
                        if tag == 'cfti':
                            modelo.colorfondotituloinserta = ProcesaTags(elementos,modelo.colorfondotituloinserta)
                        if tag == 'cffti':
                            modelo.colorfondofilatituloinserta = ProcesaTags(elementos,modelo.colorfondofilatituloinserta)
                        if tag == 'afti':
                            modelo.altofilatituloinserta = ProcesaTags(elementos,modelo.altofilatituloinserta)
                        if tag == 'jvti':
                            modelo.justificacionverticaltituloinserta = ProcesaTags(elementos,modelo.justificacionverticaltituloinserta)
                        if tag == 'jhti':
                            modelo.justificacionhorizontaltituloinserta = ProcesaTags(elementos,modelo.justificacionhorizontaltituloinserta)
                        if tag == 'cfci':
                            modelo.colorfondocomentarioinserta = ProcesaTags(elementos,modelo.colorfondocomentarioinserta)
                        if tag == 'ccin':
                            modelo.colorcomentarioinserta = ProcesaTags(elementos,modelo.colorcomentarioinserta)
                        if tag == 'fcin':
                            modelo.fontcomentarioinserta = ProcesaTags(elementos,modelo.fontcomentarioinserta)
                        if tag == 'cin':
                            modelo.comentarioinserta = ProcesaTags(elementos,modelo.comentarioinserta)
                        if tag == 'ncii':
                            modelo.numerocolumnasizquierdainserta = ProcesaTags(elementos,modelo.numerocolumnasizquierdainserta)
                        if tag == 'ncmi':
                            modelo.numerocolumnasmodeloinserta = ProcesaTags(elementos,modelo.numerocolumnasmodeloinserta)
                        if tag == 'ncdi':
                            modelo.numerocolumnasderechainserta = ProcesaTags(elementos,modelo.numerocolumnasderechainserta)
                        if tag == 'tup':
                            modelo.tituloupdate = ProcesaTags(elementos,modelo.tituloupdate)
                        if tag == 'ftup':
                            modelo.fonttituloupdate = ProcesaTags(elementos,modelo.fonttituloupdate)
                        if tag == 'ctup':
                            modelo.colortituloupdate = ProcesaTags(elementos,modelo.colortituloupdate)
                        if tag == 'cftu':
                            modelo.colorfondotituloupdate = ProcesaTags(elementos,modelo.colorfondotituloupdate)
                        if tag == 'cfftu':
                            modelo.colorfondofilatituloupdate = ProcesaTags(elementos,modelo.colorfondofilatituloupdate)
                        if tag == 'aftu':
                            modelo.altofilatituloupdate = ProcesaTags(elementos,modelo.altofilatituloupdate)
                        if tag == 'jvtu':
                            modelo.justificacionverticaltituloupdate = ProcesaTags(elementos,modelo.justificacionverticaltituloupdate)
                        if tag == 'jhtu':
                            modelo.justificacionhorizontaltituloupdate = ProcesaTags(elementos,modelo.justificacionhorizontaltituloupdate)
                        if tag == 'cup':
                            modelo.comentarioupdate = ProcesaTags(elementos,modelo.comentarioupdate)
                        if tag == 'cfcu':
                            modelo.colorfondocomentarioupdate = ProcesaTags(elementos,modelo.colorfondocomentarioupdate)
                        if tag == 'fcup':
                            modelo.fontcomentarioupdate = ProcesaTags(elementos,modelo.fontcomentarioupdate)
                        if tag == 'ccup':
                            modelo.colorcomentarioupdate = ProcesaTags(elementos,modelo.colorcomentarioupdate)
                        if tag == 'nciu':
                            modelo.numerocolumnasizquierdaupdate = ProcesaTags(elementos,modelo.numerocolumnasizquierdaupdate)
                        if tag == 'ncdu':
                            modelo.numerocolumnasderechaupdate = ProcesaTags(elementos,modelo.numerocolumnasderechaupdate)
                        if tag == 'ncmu':
                            modelo.numerocolumnasmodeloupdate = ProcesaTags(elementos,modelo.numerocolumnasmodeloupdate)
                        if tag == 'flm':
                            modelo.fontlabelmodelo = ProcesaTags(elementos,modelo.fontlabelmodelo)
                        if tag == 'clm':
                            modelo.colorlabelmodelo = ProcesaTags(elementos,modelo.colorlabelmodelo)
                        if tag == 'cau':
                            modelo.controlesautomaticos = True
                        if tag == 'tbo':
                            modelo.tituloborra = ProcesaTags(elementos,modelo.tituloborra)
                        if tag == 'ftbo':
                            modelo.fonttituloborra = ProcesaTags(elementos,modelo.fonttituloborra)
                        if tag == 'ctbo':
                            modelo.colortituloborra = ProcesaTags(elementos,modelo.colortituloborra)
                        if tag == 'cftb':
                            modelo.colorfondotituloborra = ProcesaTags(elementos,modelo.colorfondotituloborra)
                        if tag == 'cfftb':
                            modelo.colorfondofilatituloborra = ProcesaTags(elementos,modelo.colorfondofilatituloborra)
                        if tag == 'aftb':
                            modelo.altofilatituloborra = ProcesaTags(elementos,modelo.altofilatituloborra)
                        if tag == 'jvtb':
                            modelo.justificacionverticaltituloborra = ProcesaTags(elementos,modelo.justificacionverticaltituloborra)
                        if tag == 'jhtb':
                            modelo.justificacionhorizontaltituloborra = ProcesaTags(elementos,modelo.justificacionhorizontaltituloborra)
                        if tag == 'cfcb':
                            modelo.colorfondocomentarioborra = ProcesaTags(elementos,modelo.colorfondocomentarioborra)
                        if tag == 'ccbo':
                            modelo.colorcomentarioborra = ProcesaTags(elementos,modelo.colorcomentarioborra)
                        if tag == 'fcbo':
                            modelo.fontcomentarioborra = ProcesaTags(elementos,modelo.fontcomentarioborra)
                        if tag == 'cbo':
                            modelo.comentarioborra = ProcesaTags(elementos,modelo.comentarioborra)
                        if tag == 'cftxb':
                            modelo.colorfondotextoborra = ProcesaTags(elementos,modelo.colorfondotextoborra)
                        if tag == 'ctxb':
                            modelo.colortextoborra = ProcesaTags(elementos,modelo.colortextoborra)
                        if tag == 'ftxb':
                            modelo.fonttextoborra = ProcesaTags(elementos,modelo.fonttextoborra)
                        if tag == 'txbo':
                            modelo.textoborra = ProcesaTags(elementos,modelo.textoborra)
                        if tag == 'txbb':
                            modelo.textobotonborra = ProcesaTags(elementos,modelo.textobotonborra)
                        if tag == 'ncib':
                            modelo.numerocolumnasizquierdaborra = ProcesaTags(elementos,modelo.numerocolumnasizquierdaborra)
                        if tag == 'ncdb':
                            modelo.numerocolumnasderechaborra = ProcesaTags(elementos,modelo.numerocolumnasderechaborra)
                        if tag == 'ncmb':
                            modelo.numerocolumnasmodeloborra = ProcesaTags(elementos,modelo.numerocolumnasmodeloborra)
                        if tag == 'hco':
                            modelo.hijoscontiguos = True
                        if tag == 'ncho':
                            modelo.numerocolumnashijosupdate = ProcesaTags(elementos,modelo.numerocolumnashijosupdate)
                        if tag == 'ls':
                            modelo.listastaff = True
                        if tag == 'll':
                            modelo.listalogin = True
                        if tag == 'cl':
                            modelo.crearlogin = True
                        if tag == 'cs':
                            modelo.crearstaff = True
                        if tag == 'es':
                            modelo.editarstaff = True
                        if tag == 'el':
                            modelo.editarlogin = True
                        if tag == 'bs':
                            modelo.borrarstaff = True
                        if tag == 'bl':
                            modelo.borrarlogin = True
                        if tag == 'nclb':
                            modelo.numerocolumnaslabels = ProcesaTags(elementos,modelo.numerocolumnaslabels)
                        if tag == 'ncct':
                            modelo.numerocolumnascontroles = ProcesaTags(elementos,modelo.numerocolumnascontroles)
                        if tag == 'msb':
                            modelo.sinbasedatos = True
                        if tag == 'mem':
                            modelo.modeloenmenu = True
                        if tag == 'bli':
                            modelo.buscadorlista = True
                        if tag == 'cbnm':
                            modelo.colorbotonlinknuevomodelo = ProcesaTags(elementos,modelo.colorfondocomentarioborra)
                        if tag == 'ctbo':
                            modelo.colortituloborra = ProcesaTags(elementos,modelo.colorfondocomentarioborra)
                        modelo.save()
                    # Propiedades
                    if tag == 'npro':
                        propiedad = Propiedad()
                        propiedad.modelo = modelo
                        propiedad.nombre = ProcesaTags(elementos,'propiedad' + str(npr))
                        npr += 1
                    if propiedad != None:
                        tag = tag.replace('&nbsp','')
                        if tag == 'dpro':
                            propiedad.descripcion = ProcesaTags(elementos,propiedad.descripcion)
                        if tag == 'tpro':
                            propiedad.tipo = ProcesaTags(elementos,propiedad.tipo)
                        if tag == 'prf':
                            propiedad.foranea = ProcesaTags(elementos,propiedad.foranea)
                        if tag == 'txb':
                            propiedad.textobotones = ProcesaTags(elementos,propiedad.textobotones)
                        if tag == 'vdf':
                            propiedad.valorinicial = ProcesaTags(elementos,propiedad.valorinicial)
                        if tag == 'lst':
                            propiedad.largostring = ProcesaTags(elementos,propiedad.largostring)
                        if tag == 'tph':
                            propiedad.textoplaceholder = ProcesaTags(elementos,propiedad.textoplaceholder)
                        if tag == 'epro':
                            propiedad.etiqueta = ProcesaTags(elementos,propiedad.etiqueta)
                        if tag == 'enl':
                            propiedad.enlista = True
                        if tag == 'emb':
                            propiedad.enmobile = True
                        if tag == 'ncl':
                            propiedad.numerocolumnas = ProcesaTags(elementos,propiedad.numerocolumnas)
                        if tag == 'txc':
                            propiedad.textocolumna = ProcesaTags(elementos,propiedad.textocolumna)
                        if tag == 'jtxc':
                            propiedad.justificaciontextocolumna = ProcesaTags(elementos,propiedad.justificaciontextocolumna)
                        if tag == 'ffch':
                            propiedad.formatofecha = ProcesaTags(elementos,propiedad.formatofecha)
                        if tag == 'ear':
                            propiedad.etiquetaarriba = True
                        if tag == 'nef':
                            propiedad.noestaenformulario = True
                        if tag == 'pbl':
                            propiedad.participabusquedalista = True
                        if tag == 'tlz':
                            propiedad.totaliza = True
                        if tag == 'enr':
                            propiedad.enreporte = True
                        if tag == 'anre':
                            propiedad.anchoenreporte = ProcesaTags(elementos,propiedad.largostring)
                        propiedad.save()
                    # Reglas
                    if tag == 'msj':
                        regla = Regla()
                        regla.propiedad = propiedad
                        regla.mensaje = ProcesaTags(elementos,'regla' + str(nrg))
                        nrg += 1
                    if regla != None:
                        if tag == 'crg':
                            elementos = elementos.replace('~','[')
                            elementos = elementos.replace('@',']')
                            regla.codigo = ProcesaTags(elementos,regla.codigo)
                        regla.save()
            context['error_texto'] = ''
            context['proyecto'] =  proyecto
            texto_procesar.proyecto = proyecto.id
            texto_procesar.save()
            context['mensaje'] =  Texto
            # proyecto.save()
        except Exception as e:
            context['error_texto'] = 'Existe error en la construccion del Texto: ' + str(e)
        return context

def ProcesaTags(elementos,campo):
    try:
        return elementos.replace('&nbsp',' ')
    except:
        return campo.replace('&nbsp',' ')

class EsquemaView(TemplateView):
    template_name = 'esquema.html'

    def get_context_data(self,**kwargs):
        context = super(EsquemaView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['error'] = ''
        return context

class DuplicaView(FormView):
    template_name = 'esquema.html'

    def get_context_data(self,**kwargs):
        context = super(DuplicaView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['error'] = ''
        return context        

class BaseProyectoView(ListView):
    model = Secp
    template_name = 'proyectos/base_proyecto.html'

    def get_context_data(self, **kwargs):
        context = super(BaseProyectoView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(usuario = self.request.user, id = self.request.GET['proyecto_id'])
            # Forma el arbol para el template
            context['proyecto'] = proyecto
            context['proyecto_id'] = proyecto.id
            # Crea la lista
            lista = []
            rutinas.CreaListaSeccion(lista,Secp,Filp,Colp,proyecto,None)
            context['existe'] = False
            # ns=0
            # nf=0
            # nc=0
            # iw=''
            # ih=''
            # url=''
            # jh=''
            # jv=''
            # texto = ''
            # ctexto = ''
            # stri = ''
            # for seccion in Secp.objects.filter(proyecto=proyecto):
            #     context['existe'] = True
            #     lista.append([seccion,'s',0,ns])
            #     ns+=1
            #     for fila in Filp.objects.filter(seccion=seccion):
            #         lista.append([fila,'f',50,nf])
            #         nf=+1
            #         for columna in Colp.objects.filter(fila=fila):
            #             fn = columna.fonttexto.split(',')[0]
            #             fs = columna.fonttexto.split(',')[1]
            #             fb = columna.fonttexto.split(',')[2]
            #             try:
            #                 ms = columna.margeninterno.split(',')[0]
            #                 md = columna.margeninterno.split(',')[1]
            #                 mb = columna.margeninterno.split(',')[2]
            #                 mi = columna.margeninterno.split(',')[3]
            #             except:
            #                 ms = '0px'
            #                 md = '0px'
            #                 mb = '0px'
            #                 mi = '0px'
            #             # logo
            #             if columna.funcion == 'l':
            #                 if proyecto.avatar:
            #                     url = proyecto.avatar.url
            #                     iw = str(proyecto.avatarwidth) + 'px'
            #                     ih = str(proyecto.avatarheight) + 'px'
            #                     if proyecto.justificacionhorizontallogo == 'c':
            #                         jh= 'center'
            #                     if proyecto.justificacionhorizontallogo == 'i':
            #                         jh='start'
            #                     if proyecto.justificacionhorizontallogo == 'd':
            #                         jh='end'
            #                     if proyecto.justificacionverticallogo == 'c':
            #                         jv='center'
            #                     if proyecto.justificacionverticallogo == 's':
            #                         jv='start'
            #                     if proyecto.justificacionverticallogo == 'i':
            #                         jv='end'
            #                 elif columna.imagen:
            #                     url = columna.imagen.url
            #                     iw = columna.dimensionesimagen.split(',')[0]
            #                     ih = columna.dimensionesimagen.split(',')[1]
            #                     jh=columna.justificacionhorizontaltexto
            #                     jv=columna.justificacionverticaltexto
            #                 else:
            #                     url=''
            #                     texto = columna.textocolumna
            #                     ctexto = columna.colortexto
            #                     jh=columna.justificacionhorizontaltexto
            #                     jv=columna.justificacionverticaltexto
            #             # titulo
            #             if columna.funcion == 't':
            #                 texto = ''
            #                 if proyecto.imagentitulo or proyecto.titulo != '':
            #                     if proyecto.justificacionhorizontaltitulo == 'c':
            #                         jh= 'center'
            #                     if proyecto.justificacionhorizontaltitulo == 'i':
            #                         jh='start'
            #                     if proyecto.justificacionhorizontaltitulo == 'd':
            #                         jh='end'
            #                     if proyecto.justificacionverticaltitulo == 'c':
            #                         jv='center'
            #                     if proyecto.justificacionverticaltitulo == 's':
            #                         jv='start'
            #                     if proyecto.justificacionverticaltitulo == 'i':
            #                         jv='end'
            #                 if proyecto.imagentitulo:
            #                     url = proyecto.imagentitulo.url
            #                 elif proyecto.titulo:
            #                     url=''
            #                     texto = proyecto.titulo
            #                     ctexto = proyecto.colortitulo
            #                     fn = proyecto.fonttitulo.split(',')[0]
            #                     fs = proyecto.fonttitulo.split(',')[1]
            #                     fb = proyecto.fonttitulo.split(',')[2]
            #                 elif columna.imagen:
            #                     url = columna.imagen.url
            #                     jh=columna.justificacionhorizontaltexto
            #                     jv=columna.justificacionverticaltexto
            #                 else:
            #                     url=''
            #                     texto = columna.textocolumna
            #                     ctexto = columna.colortexto
            #                     jh=columna.justificacionhorizontaltexto
            #                     jv=columna.justificacionverticaltexto
            #             if columna.funcion == 'b':
            #                 texto = ''
            #                 url=''
            #                 jh='center'
            #                 jv='center'
            #             if columna.funcion == 'o':
            #                 texto = ''
            #                 if columna.imagen:
            #                     url = columna.imagen.url
            #                     iw = columna.dimensionesimagen.split(',')[0]
            #                     ih = columna.dimensionesimagen.split(',')[1]
            #                     jh=columna.justificacionhorizontaltexto
            #                     jv=columna.justificacionverticaltexto
            #                 else:
            #                     url=''
            #                     texto = columna.textocolumna
            #                     ctexto = columna.colortexto
            #                     jh=columna.justificacionhorizontaltexto
            #                     jv=columna.justificacionverticaltexto

            #             lista.append([columna,'c',100,nc,fn,fs,fb,iw,ih,ms,md,mb,mi,proyecto,url,jh,jv,texto,ctexto,stri])
            # nc+=1
            context['lista'] = lista

        except Exception as e:
            context['error'] = '!!! No eres el propietario del proyecto !!!' + str(e)
        return context

class EditarSeccionView(UpdateView):
    model = Secp
    form_class = SeccionForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('proyectos:editar_seccion', args=[self.object.id]) + '?ok'

    def get_context_data(self,**kwargs):
        context = super(EditarSeccionView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(id=self.object.proyecto.id,usuario=self.request.user)
            context['proyecto'] = proyecto
            context['proyecto_id'] = self.object.proyecto.id
            context['seccion'] = self.object
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        form = self.get_form()
        seccion = form.save(commit=False)
        mensaje_error=''
        proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'])
        if form.is_valid():
            seccion.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            mensaje_error = 'Error en el formulario, intente nuevamente'
            return HttpResponseRedirect('/principal/editar_seccion/' + str(seccion.id) + '/?proyecto_id=' + str(proyecto.id) + '&mensaje_error=' + mensaje_error) 


class CrearSeccionView(CreateView):
    model = Secp
    form_class = SeccionForm

    def get_success_url(self):
        return reverse_lazy('proyectos:base_proyecto') + '?proyecto_id=' + self.request.GET['proyecto_id']

    def get_context_data(self,**kwargs):
        context = super(CrearSeccionView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            context['proyecto'] = proyecto
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

    def post(self,request,*args,**kwargs):
        mensaje_error=''
        form = self.form_class(request.POST)
        proyecto = Proyecto.objects.get(id = request.GET['proyecto_id'])
        if form.is_valid():
            seccion = form.save(commit=False)
            seccion.proyecto = proyecto
            seccion.save()
            return HttpResponseRedirect(self.get_success_url())
        return HttpResponseRedirect('/principal/crear_seccion' + '/?proyecto_id=' + str(proyecto.id))             

class BorrarSeccionView(DeleteView):
    model = Secp

    def get_success_url(self):
        return reverse_lazy('proyectos:base_proyecto') + '?proyecto_id=' + self.request.GET['proyecto_id']

    def get_context_data(self,**kwargs):
        context = super(BorrarSeccionView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            context['error'] = ''
            obj = Secp.objects.get(id=self.object.id)
            context['proyecto_id'] = obj.proyecto.id
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

class CrearFilaView(CreateView):
    model = Filp
    form_class = FilaForm

    def get_success_url(self):
        return reverse_lazy('proyectos:base_proyecto') + '?proyecto_id=' + self.request.GET['proyecto_id']

    def get_context_data(self,**kwargs):
        context = super(CrearFilaView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            proyecto = Proyecto.objects.get(id = self.request.GET['proyecto_id'],usuario=self.request.user)
            seccion = Secp.objects.get(id = self.request.GET['seccion_id'])
            context['proyecto'] = proyecto
            context['seccion'] = seccion
            context['error'] = ''
        except Exception as e:
            context['error'] = '!!! No eres el propietario del proyecto !!!' + str(e)
        return context

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST, request.FILES)
        seccion = Secp.objects.get(id = request.GET['seccion_id'])
        proyecto = Proyecto.objects.get(id = seccion.proyecto.id)
        mensaje_error = ''
        if form.is_valid():
            fila = form.save(commit=False)
            fila.seccion = seccion
            # Colocamos el valor del padre
            fila.save()
            return HttpResponseRedirect(self.get_success_url())
        return HttpResponseRedirect('/principal/crear_fila' + '/?proyecto_id=' + str(proyecto.id)) 

class EditarFilaView(UpdateView):
    model = Filp
    form_class = FilaForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        fila = Filp.objects.get(id=self.request.GET['fila_id'])
        return reverse_lazy('proyectos:editar_fila', args=[fila.id]) + '?ok&proyecto_id=' + self.request.GET['proyecto_id'] + '&seccion_id=' + self.request.GET['seccion_id']

    def get_context_data(self,**kwargs):
        context = super(EditarFilaView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            seccion = Secp.objects.get(id=self.request.GET['seccion_id'])
            context['proyecto'] = proyecto
            context['seccion'] = seccion
            context['fila'] = Filp.objects.get(id=self.object.id)
            context['error'] = ''
        except Exception as e:
            context['error'] = '!!! No eres el propietario del proyecto !!!' + str(e)
        return context
    
    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        form = self.get_form()
        fila = form.save(commit=False)
        fila.save()
        return HttpResponseRedirect(self.get_success_url())

class BorrarFilaView(DeleteView):
    model = Filp

    def get_success_url(self):
        return reverse_lazy('proyectos:base_proyecto') + '?proyecto_id=' + self.request.GET['proyecto_id']

    def get_context_data(self,**kwargs):
        context = super(BorrarFilaView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            obj = Filp.objects.get(id=self.object.id)
            context['fila'] = obj
            context['proyecto'] = Proyecto.objects.get(id=obj.seccion.proyecto.id)
            context['error'] = ''
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

class CrearColumnaView(CreateView):
    model = Colp
    form_class = ColumnaForm

    def get_success_url(self):
        return reverse_lazy('proyectos:base_proyecto') + '?proyecto_id=' + self.request.GET['proyecto_id']

    def get_context_data(self,**kwargs):
        context = super(CrearColumnaView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            fila = Filp.objects.get(id=self.request.GET['fila_id'])
            context['fila'] = fila
            proyecto = Proyecto.objects.get(id=fila.seccion.proyecto.id,usuario=self.request.user)
            context['proyecto'] = proyecto
            context['error'] = ''
            context['seccion'] = 'proyecto'
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        fila = Filp.objects.get(id = request.GET['fila_id'])
        if form.is_valid():
            columna = form.save(commit=False)
            columna.fila = fila
            columna.save()
            return HttpResponseRedirect(self.get_success_url())
        return render(request, 'proyectos/columnap_form.html', {'form': form})

class EditarColumnaView(UpdateView):
    model = Colp
    form_class = ColumnaForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('proyectos:editar_columna', args=[self.object.id]) + '?ok&proyecto_id=' + self.request.GET['proyecto_id']

    def get_context_data(self,**kwargs):
        context = super(EditarColumnaView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            obj = self.object
            context['columna'] = obj
            context['fila'] = Filp.objects.get(id=obj.fila.id)
            proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            context['nombre'] = obj.nombre
            context['proyecto'] = proyecto
            context['error'] = ''
            context['seccion'] = 'proyecto'
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

class BorrarColumnaView(DeleteView):
    model = Colp

    def get_success_url(self):
        return reverse_lazy('proyectos:base_proyecto') + '?ok&proyecto_id=' + self.request.GET['proyecto_id']

    def get_context_data(self,**kwargs):
        context = super(BorrarColumnaView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            obj = self.object
            fila = Filp.objects.get(id=obj.fila.id)
            proyecto = Proyecto.objects.get(id=fila.seccion.proyecto.id,usuario=self.request.user)
            context['nombre'] = obj.nombre
            context['proyecto'] = proyecto
            context['error'] = ''
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context


        