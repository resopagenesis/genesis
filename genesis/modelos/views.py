from django.shortcuts import render, redirect
from django.views.generic.list import ListView
# from aplicaciones.models import Aplicacion
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from .models import Modelo, ZonaReporte, ZonaReporteAdHoc, ReporteAdHocObjeto, DashObjeto
from proyectos.models import Proyecto
from propiedades.models import Propiedad
from .forms import ModeloForm,ReporteAdHocObjetoForm, DashObjetoForm
from django import forms
from django.http import HttpResponseRedirect
from proyectos.views import VerificaVigenciaUsuario
from .models import Seccion, Fila, Columna
from .forms import SeccionForm, FilaForm, ColumnaForm
from crear.views import rutinas

class CrearModeloView(CreateView):
    model = Modelo
    form_class = ModeloForm

    def get_success_url(self):
        return reverse_lazy('proyectos:arbol') + '?proyecto_id=' + self.request.GET['proyecto_id']

    def get_context_data(self,**kwargs):
        context = super(CrearModeloView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            proyecto = Proyecto.objects.get(id = self.request.GET['proyecto_id'],usuario=self.request.user)
            context['proyecto'] = proyecto
            context['modelo'] = None
            context['mensaje_error'] = self.request.GET['mensaje_error']
            if self.request.GET['modelo_id'] != '0' and self.request.GET['modelo_id'] != 'None':
                context['modelo'] = Modelo.objects.get(id=self.request.GET['modelo_id'])
            context['error'] = ''
            # verifica si tiene vigencia de uso
            # context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        # rutinas.DesplegarArbol(False, self.object.id )
        return context

    def get_form(self,form_class=None):
        form = super(CrearModeloView, self).get_form()
        #Modificar en tiempo real
        # aplicacion = Aplicacion.objects.get(id = self.request.GET['aplicacion_id'])
        proyecto = Proyecto.objects.get(id = self.request.GET['proyecto_id'],usuario=self.request.user)
        PADRES_LIST = []
        PADRES_LIST.append(['nada','nada'])
        for ml in Modelo.objects.filter(proyecto=proyecto):
           PADRES_LIST.append([ml.nombre, ml.nombre])
        form.fields['padre'].widget = forms.Select(attrs={'class':'form-control font_control'},choices=PADRES_LIST)
        return form

    def get_form_kwargs(self):
        proyecto= self.request.GET['proyecto_id']
        kwargs = super(CrearModeloView, self).get_form_kwargs()
        kwargs.update({'proyect': proyecto})
        return kwargs
        
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST, request.FILES)
        proyecto = Proyecto.objects.get(id = request.GET['proyecto_id'])
        mensaje_error = ''
        if form.is_valid():
            modelo = form.save(commit=False)
            modelo.proyecto = Proyecto.objects.get(id = request.GET['proyecto_id'])
            # Colocamos el valor del padre
            modelo.padre = 'nada'
            if self.request.GET['modelo_id'] != '0':
                modpadre = Modelo.objects.get(id=self.request.GET['modelo_id'])
                modelo.padre = modpadre.nombre
            # Validar que el modelo sea unico

            if Modelo.objects.filter(nombre=modelo.nombre,proyecto=modelo.proyecto).count() == 0:
                if modelo.padre == 'nada':
                    modelo.nivelidentacion = 1
                    if Modelo.objects.filter(proyecto = proyecto).count()==0:
                        modelo.ultimoregistro = 'p'
                    else:
                        modelo.ultimoregistro = 'u'
                else:
                    modelo.nivelidentacion = modpadre.nivelidentacion + 1 
                modelo.save()
                # controla que sea ultimo registro
                for obj in Modelo.objects.filter(padre='nada',proyecto=proyecto):
                    if obj.ultimoregistro != 'p' and obj.id != modelo.id:
                        obj.ultimoregistro = 'x'
                        obj.save()
                rutinas.CrearSeccionProyecto(modelo,proyecto)
                rutinas.DesplegarArbol(True, proyecto.id,self.request )
                return HttpResponseRedirect(self.get_success_url())
            else:
                mensaje_error = 'El Modelo ' + modelo.nombre + ' ya existe en el proyecto, intente con otro nombre'
                return HttpResponseRedirect('/modelos/crear' + '/?proyecto_id=' + str(proyecto.id) + '&modelo_id=' + str(modelo.id) + '&mensaje_error=' + mensaje_error) 
        # return render(request, 'modelos/modelo_form.html', {'form': form,'mensaje_error':mensaje_error})
        return HttpResponseRedirect('/modelos/crear' + '/?proyecto_id=' + str(proyecto.id)) 

class EditarModeloView(UpdateView):
    model = Modelo
    form_class = ModeloForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        modelo = Modelo.objects.get(id=self.request.GET['modelo_id'])
        return reverse_lazy('modelos:editar', args=[modelo.id]) + '?ok&proyecto_id=' + self.request.GET['proyecto_id'] + '&modelo_id=' + self.request.GET['modelo_id']

    def get_context_data(self,**kwargs):
        context = super(EditarModeloView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            context['proyecto'] = proyecto
            modelo = Modelo.objects.get(id=self.object.id)
            context['modelo'] = modelo
            # context['mensaje_error'] = self.request.GET['mensaje_error']
            context['error'] = ''

            try:
                context['font_titulo_lista'] = [modelo.fonttitulolista.split(',')[0],modelo.fonttitulolista.split(',')[1],modelo.fonttitulolista.split(',')[2]]
            except:
                context['font_titulo_lista'] = ['Arial','10','500']
            try:
                context['font_comentario_lista'] = [modelo.fontcomentariolista.split(',')[0],modelo.fontcomentariolista.split(',')[1],modelo.fontcomentariolista.split(',')[2]]
            except:
                context['font_comentario_lista'] = ['Arial','8','500']
            try:
                context['font_columnas_lista'] = [modelo.fontcolumnaslista.split(',')[0],modelo.fontcolumnaslista.split(',')[1],modelo.fontcolumnaslista.split(',')[2]]
            except:
                context['font_columnas_lista'] = ['Arial','8','500']
            try:
                context['font_texto_lista'] = [modelo.fonttextolista.split(',')[0],modelo.fonttextolista.split(',')[1],modelo.fonttextolista.split(',')[2]]
            except:
                context['font_texto_lista'] = ['Arial','8','500']
            try:
                context['texto_editar_borrar'] = [modelo.textoeditarborrar.split(',')[0],modelo.textoeditarborrar.split(',')[1]]
            except:
                context['texto_editar_borrar'] = ['Editar','Borrar']
            try:
                context['font_editar_borrar'] = [modelo.fonteditarborrar.split(',')[0],modelo.fonteditarborrar.split(',')[1],modelo.fonteditarborrar.split(',')[2]]
            except:
                context['font_editar_borrar'] = ['Arial','8','500']
            try:
                context['font_titulo_inserta'] = [modelo.fonttituloinserta.split(',')[0],modelo.fonttituloinserta.split(',')[1],modelo.fonttituloinserta.split(',')[2]]
            except:
                context['font_titulo_inserta'] = ['Arial','10','500']
            try:
                context['font_comentario_inserta'] = [modelo.fontcomentarioinserta.split(',')[0],modelo.fontcomentarioinserta.split(',')[1],modelo.fontcomentarioinserta.split(',')[2]]
            except:
                context['font_comentario_inserta'] = ['Arial','8','500']
            try:
                context['font_label'] = [modelo.fontlabelmodelo.split(',')[0],modelo.fontlabelmodelo.split(',')[1],modelo.fontlabelmodelo.split(',')[2]]
            except:
                context['font_label'] = ['Arial','8','500']
            try:
                context['font_titulo_update'] = [modelo.fonttituloupdate.split(',')[0],modelo.fonttituloupdate.split(',')[1],modelo.fonttituloupdate.split(',')[2]]
            except:
                context['font_titulo_update'] = ['Arial','10','500']
            try:
                context['font_comentario_update'] = [modelo.fontcomentarioupdate.split(',')[0],modelo.fontcomentarioupdate.split(',')[1],modelo.fontcomentarioupdate.split(',')[2]]
            except:
                context['font_comentario_update'] = ['Arial','8','500']
            try:
                context['font_titulo_borra'] = [modelo.fonttituloborra.split(',')[0],modelo.fonttituloborra.split(',')[1],modelo.fonttituloborra.split(',')[2]]
            except:
                context['font_titulo_borra'] = ['Arial','10','500']
            try:
                context['font_comentario_borra'] = [modelo.fontcomentarioborra.split(',')[0],modelo.fontcomentarioborra.split(',')[1],modelo.fontcomentarioborra.split(',')[2]]
            except:
                context['font_comentario_borra'] = ['Arial','8','500']
            try:
                context['font_texto_borra'] = [modelo.fonttextoborra.split(',')[0],modelo.fonttextoborra.split(',')[1],modelo.fonttextoborra.split(',')[2]]
            except:
                context['font_texto_borra'] = ['Arial','8','500']
            try:
                context['font_menu'] = [modelo.aplicacion.fontmenu.split(',')[0],modelo.aplicacion.fontmenu.split(',')[1],modelo.aplicacion.fontmenu.split(',')[2]]
            except:
                context['font_menu'] = ['Arial','8','500']

            context['font_titulo_lista_hijo'] = ['roboto','8','500']
            context['font_comentario_lista_hijo'] = ['arial','8',500]
            context['font_columnas_lista_hijo'] = ['roboto','8','700']
            context['font_texto_lista_hijo'] = ['roboto','8',500]
            context['texto_editar_borrar_hijo'] = ['edita','borra']
            context['font_editar_borrar_hijo'] = ['arial','6','500']

            # verifica si tiene vigencia de uso
            # context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        except Exception as e:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        # rutinas.DesplegarArbol(False, self.object.id )
        return context
    
    def get_form(self,form_class=None):
        form = super(EditarModeloView, self).get_form()
        #Modificar en tiempo real
        # aplicacion = Aplicacion.objects.get(id = self.request.GET['aplicacion_id'])
        proyecto = Proyecto.objects.get(id = self.request.GET['proyecto_id'],usuario=self.request.user)
        PADRES_LIST = []
        PADRES_LIST.append(['nada','nada'])
        for ml in Modelo.objects.filter(proyecto=proyecto):
           PADRES_LIST.append([ml.nombre, ml.nombre])
        form.fields['padre'].widget = forms.Select(attrs={'class':'form-control font_control'},choices=PADRES_LIST)
        return form

    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        form = self.get_form()
        modelo = form.save(commit=False)
        mensaje_error=''
        proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'])
        # Validar que el modelo sea unico
        nombre_antiguo = Modelo.objects.get(id=self.request.GET['modelo_id'], proyecto=proyecto).nombre
        if nombre_antiguo != modelo.nombre:
            if Modelo.objects.filter(nombre=modelo.nombre,proyecto=proyecto).count() == 0:
                modelo.save()
                rutinas.DesplegarArbol(True, proyecto.id,self.request )
                ActualizaModeloPadre(nombre_antiguo, modelo.nombre, proyecto)
                return HttpResponseRedirect(self.get_success_url())
            else:
                mensaje_error = 'El Modelo ' + modelo.nombre + ' ya existe en el proyecto, intente con otro nombre'
                return HttpResponseRedirect('/modelos/editar/' + str(modelo.id) + '/?proyecto_id=' + str(proyecto.id) + '&modelo_id=' + str(modelo.id) + '&mensaje_error=' + mensaje_error) 
        else:
            modelo.save()
            return HttpResponseRedirect(self.get_success_url())

    def get_form_kwargs(self):
        proyecto= self.request.GET['proyecto_id']
        kwargs = super(EditarModeloView, self).get_form_kwargs()
        kwargs.update({'proyect': proyecto})
        return kwargs
        # return render(request, 'modelos/modelo_update_form.html', {'form': form,'mensaje_error':mensaje_error})

def ActualizaModeloPadre(nombrePadreAnterior, nuevoNombrePadre,proyecto):
    for modelo in Modelo.objects.filter(proyecto=proyecto, padre=nombrePadreAnterior):
        modelo.padre = nuevoNombrePadre
        modelo.save()

class BorrarModeloView(DeleteView):
    model = Modelo

    def get_success_url(self):
        proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'])
        strTexto = []
        BorraRecursiva(strTexto,self.request.GET['nombre'],proyecto)
        for mid in strTexto:
            Modelo.objects.get(id=mid).delete()
        try:
            if self.request.GET['borra'] == '0':
                rutinas.DesplegarArbol(False, self.object.proyecto.id,self.request )
        except:
            rutinas.DesplegarArbol(True, self.object.proyecto.id,self.request )

        try:
            if self.request.GET['wizzard'] == '1':
                return reverse_lazy('proyectos:wizzard_arbol') + '?ok&proyecto_id=' + self.request.GET['proyecto_id']
        except:
            return reverse_lazy('proyectos:arbol') + '?proyecto_id=' + self.request.GET['proyecto_id']


    def get_context_data(self,**kwargs):
        context = super(BorrarModeloView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            obj = Modelo.objects.get(id=self.object.id)
            context['modelo'] = obj
            context['proyecto'] = Proyecto.objects.get(id=obj.proyecto.id)
            context['nombre'] = obj.nombre
            context['error'] = ''
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

def BorraRecursiva(strTexto,nombre,proyecto):
    for li in Modelo.objects.filter(padre=nombre,proyecto=proyecto):
        strTexto.append(li.id)
        BorraRecursiva(strTexto,li.nombre,proyecto)

class ReporteModeloView(TemplateView):

    template_name = "modelos/reporte_modelo.html"

    def get_success_url(self):
        return reverse_lazy('proyectos:arbol') + '?proyecto_id=' + self.request.GET['proyecto_id']

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def get_context_data(self,**kwargs):
        context = super(ReporteModeloView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            proyecto = Proyecto.objects.get(id = self.request.GET['proyecto_id'],usuario=self.request.user)
            modelo = Modelo.objects.get(id = self.request.GET['modelo_id'],proyecto=proyecto)
            context['proyecto'] = proyecto
            context['modelo'] = modelo
            # context['mensaje_error'] = self.request.GET['mensaje_error']
            # Enviamos el json de los reportes
            lista=[]
            zonas = []
            TablasRecusivas(modelo,lista,5,proyecto,modelo.id,1)
            context['lista'] = lista
            try:
                json = ZonaReporte.objects.get(id=self.request.GET['id'])
                context['json'] = json.texto
                context['font'] = modelo.font
            except Exception as e:
                print(str(e))
                context['json'] = ''
            context['error'] = ''
        except Exception as e:
            context['error'] = '!!! No eres el propietario del proyecto !!!' + str(e)
        return context

# la lista de propiedades es :
# 0 - nombre de propiedad
# 1 - Identificado registro
# 2 - Identacion
# 3 - id de la propiedad
# 4 - Numero de la zona
# 5 - Tipo de la propiedad
# 6 - Texto botones
# 7 - Largo de string
# 8 - Totaliza
# 9 - Ancho en reporte
# 10 - id del modelo

def TablasRecusivas(modelo,lista,ident,proyecto,id_modelo,zona):
    if modelo.padre =='nada':
        lista.append([modelo.nombre,'mp',ident,str(id_modelo),str(zona),modelo.font])
    else:
        lista.append([modelo.nombre,'mh',ident+6,str(id_modelo),str(zona),modelo.font])
    id=1
    for prop in Propiedad.objects.filter(modelo=modelo):
        if prop.enreporte:
            lista.append([prop.nombre,'np',ident+12,str(prop.id),str(zona),prop.tipo,prop.textobotones,prop.largostring,prop.totaliza,prop.anchoenreporte,str(id_modelo)])
    for mod in Modelo.objects.filter(padre=modelo.nombre, proyecto=proyecto):
        TablasRecusivas(mod, lista,ident+5,proyecto,mod.id,zona+1)

class ReporteModeloListView(ListView):
    model = ZonaReporte
    template_name = 'modelos/reporte_modelo_list.html'

    def get_context_data(self, **kwargs):
        context = super(ReporteModeloListView, self).get_context_data(**kwargs)

        # Recibe datos del reporte de un modelo
        try:
            proyecto_json = self.request.GET['json']
            modeloid = self.request.GET['modelo_id']
            user = self.request.user
            if self.request.GET['nuevo'] == "1":
                # definir el numero de reporte
                numero = 0
                numrow = ZonaReporte.objects.filter(modeloid = modeloid).order_by('nombre').count()
                lista = ZonaReporte.objects.filter(modeloid=modeloid).order_by('-nombre')
                try:
                    if numrow > 0:
                        numero = int(lista[0].nombre.split('_')[1]) + 1
                    else:
                        numero = 1
                except:
                    numero = 1
                modelo = ZonaReporte()
                modelo.nombre = Modelo.objects.get(id=modeloid).nombre + '_' + str(numero)
                modelo.texto =  proyecto_json
                modelo.modeloid = modeloid
                modelo.save()
            if self.request.GET['nuevo'] == "0":
                id = self.request.GET['id']
                modelo = ZonaReporte.objects.get(id=id)
                modelo.texto =  proyecto_json
                # texto_json = json.loads(texto_procesar.texto)['propiedades']
                modelo.save()            
        except Exception as e:
            print(str(e))
            pass

        try:
            modeloid = self.request.GET['modelo_id']
            context['modelo'] = Modelo.objects.get(id=modeloid)
            context['proyecto'] = context['modelo'].proyecto
            context['vigente'] = VerificaVigenciaUsuario(self.request.user)
            context['lista_json'] = ZonaReporte.objects.filter(modeloid = modeloid)
            context['error'] = ''
        except Exception as e:
            context['error'] = str(e) 

        # context['criterio'] = self.request.GET['criterio']
        return context

class BorrarReporteJsonView(DeleteView):
    model = ZonaReporte

    def get_success_url(self):
        return reverse_lazy('modelos:reporte_lista') + '?modelo_id=' + str(Modelo.objects.get(id=self.request.GET['modelo_id']).id) + '&criterio=' + self.request.GET['criterio']

    def get_context_data(self,**kwargs):
        context = super(BorrarReporteJsonView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['error'] = ''
        context['criterio'] = self.request.GET['criterio']
        return context

class ReporteAdHocObjetoListView(ListView):
    model = ReporteAdHocObjeto

    def get_context_data(self, **kwargs):
        context = super(ReporteAdHocObjetoListView, self).get_context_data(**kwargs)
        modelo = Modelo.objects.get(id=self.request.GET['modelo_id'])
        proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'])
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['lista_objeto'] = ReporteAdHocObjeto.objects.filter(modeloid = modelo.id)
        context['modelo'] = modelo
        context['proyecto'] = proyecto
        context['error'] = ''
        return context

class CrearReporteAdHocObjetoView(CreateView):
    model = ReporteAdHocObjeto
    form_class = ReporteAdHocObjetoForm

    def get_success_url(self):
        return reverse_lazy('modelos:reporte_adhoc_objeto_lista') + '?modelo_id=' + self.request.GET['modelo_id'] + '&proyecto_id=' + self.request.GET['proyecto_id']

    def get_context_data(self,**kwargs):
        context = super(CrearReporteAdHocObjetoView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        modelo = Modelo.objects.get(id = self.request.GET['modelo_id'])
        context['modelo'] = modelo
        context['proyecto'] = modelo.proyecto
        context['error'] = ''
        return context

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST,request.FILES)
        modelo = Modelo.objects.get(id = request.GET['modelo_id'])
        if form.is_valid():
            reporteadhoc = form.save(commit=False)
            reporteadhoc.modeloid = modelo.id
            reporteadhoc.save()
            return HttpResponseRedirect(self.get_success_url())
        return render(request, 'modelos/proyectoobjeto_form.html', {'form': form})

class EditarReporteAdHocObjetoView(UpdateView):
    model = ReporteAdHocObjeto
    form_class = ReporteAdHocObjetoForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('modelos:editar_reporte_adhoc_objeto', args=[self.object.id]) + '?ok' + '&modelo_id=' + self.request.GET['modelo_id'] + '&proyecto_id=' + self.request.GET['proyecto_id']

    def get_context_data(self,**kwargs):
        context = super(EditarReporteAdHocObjetoView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        modelo = Modelo.objects.get(id = self.request.GET['modelo_id'])
        context['modelo'] = modelo
        context['proyecto'] = modelo.proyecto
        context['error'] = ''
        return context

class BorrarReporteAdHocObjetoView(DeleteView):
    model = ReporteAdHocObjeto

    def get_success_url(self):
        return reverse_lazy('modelos:reporte_adhoc_objeto_lista') + '?modelo_id=' + self.request.GET['modelo_id'] + '&proyecto_id=' + self.request.GET['proyecto_id']

    def get_context_data(self,**kwargs):
        context = super(BorrarReporteAdHocObjetoView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['error'] = ''
        return context

class ProcesarReporteAdHocObjetoView(TemplateView):
    template_name = "modelos/modelo_procesa_reporte_adhoc_objeto.html"

    def get_context_data(self,**kwargs):
        context = super(ProcesarReporteAdHocObjetoView, self).get_context_data(**kwargs)
        modelo_reporte_adhoc_objeto = ReporteAdHocObjeto.objects.get(id=self.request.GET['id'])
        proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'])
        modelo = Modelo.objects.get(id=self.request.GET['modelo_id'])
        texto_procesar = rutinas.SinQuotes(modelo_reporte_adhoc_objeto.texto)
        texto_procesar = rutinas.SinTags(texto_procesar)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['error'] = ''
        context['error_texto'] = ''
        context['modelo'] = modelo
        context['proyecto'] = proyecto
        # context['criterio'] = self.request.GET['criterio']
        context['lista_errores'] = None

        texto = texto_procesar.split('\n')

        lista_lineas = []
        lista_modelos = []
        lista_campos = []
        lista_errores = []
        codigo = ''

        para_error = ''

        try:
            for txt in texto:
                para_error = txt
                if len(txt) > 1 and txt.strip()[0] != '#':
                    # procesar una linea
                    textop = ProcesaLinea(txt, proyecto, modelo,lista_errores, codigo)
                    codigo += textop
            modelo_reporte_adhoc_objeto.codigo = codigo
            modelo_reporte_adhoc_objeto.save()
            context['modeloreporte'] = modelo_reporte_adhoc_objeto
            if len(lista_errores) > 0:                
                context['lista_errores'] = lista_errores
                context['numero_errores'] = len(lista_errores)

        except Exception as e:
            lista_errores.append('Existe error en la construccion del Texto: ' + ' ' + str(e) + ' en la linea ' + para_error)
            context['lista_errores'] = lista_errores
            context['numero_errores'] = len(lista_errores)

        return context

class DashObjetoListView(ListView):
    model = DashObjeto

    def get_context_data(self, **kwargs):
        context = super(DashObjetoListView, self).get_context_data(**kwargs)
        modelo = Modelo.objects.get(id=self.request.GET['modelo_id'])
        proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'])
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['lista_objeto'] = DashObjeto.objects.filter(modeloid = modelo.id)
        context['modelo'] = modelo
        context['proyecto'] = proyecto
        context['error'] = ''
        return context

class CrearDashObjetoView(CreateView):
    model = DashObjeto
    form_class = DashObjetoForm

    def get_success_url(self):
        return reverse_lazy('modelos:dash_objeto_lista') + '?modelo_id=' + self.request.GET['modelo_id'] + '&proyecto_id=' + self.request.GET['proyecto_id']

    def get_context_data(self,**kwargs):
        context = super(CrearDashObjetoView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        modelo = Modelo.objects.get(id = self.request.GET['modelo_id'])
        context['modelo'] = modelo
        context['proyecto'] = modelo.proyecto
        context['error'] = ''
        return context

    def get_form(self,form_class=None):
        my_form = super(CrearDashObjetoView,self).get_form()
        # my_form = DashObjetoForm()
        
        my_form.fields['extrafield'] = forms.CharField()
        return my_form

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST,request.FILES)
        modelo = Modelo.objects.get(id = request.GET['modelo_id'])
        if form.is_valid():
            dash = form.save(commit=False)
            dash.modeloid = modelo.id
            dash.save()
            return HttpResponseRedirect(self.get_success_url())
        return render(request, 'modelos/dashobjeto_form.html', {'form': form})

class EditarDashObjetoView(UpdateView):
    model = DashObjeto
    form_class = DashObjetoForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('modelos:editar_dash_objeto', args=[self.object.id]) + '?ok' + '&modelo_id=' + self.request.GET['modelo_id'] + '&proyecto_id=' + self.request.GET['proyecto_id']

    def get_context_data(self,**kwargs):
        context = super(EditarDashObjetoView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        modelo = Modelo.objects.get(id = self.request.GET['modelo_id'])
        context['modelo'] = modelo
        context['proyecto'] = modelo.proyecto
        context['error'] = ''
        return context

class BorrarDashObjetoView(DeleteView):
    model = DashObjeto

    def get_success_url(self):
        return reverse_lazy('modelos:dash_objeto_lista') + '?modelo_id=' + self.request.GET['modelo_id'] + '&proyecto_id=' + self.request.GET['proyecto_id']

    def get_context_data(self,**kwargs):
        context = super(BorrarDashObjetoView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['error'] = ''
        return context

class ProcesarDashObjetoView(TemplateView):
    template_name = "modelos/modelo_procesa_dash_objeto.html"

    def get_context_data(self,**kwargs):
        context = super(ProcesarDashObjetoView, self).get_context_data(**kwargs)
        modelo_reporte_adhoc_objeto = DashObjeto.objects.get(id=self.request.GET['id'])
        proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'])
        modelo = Modelo.objects.get(id=self.request.GET['modelo_id'])
        texto_procesar = rutinas.SinQuotes(modelo_reporte_adhoc_objeto.texto)
        texto_procesar = rutinas.SinTags(texto_procesar)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['error'] = ''
        context['error_texto'] = ''
        context['modelo'] = modelo
        context['proyecto'] = proyecto
        context['lista_errores'] = None

        texto = texto_procesar.split('\n')

        lista_lineas = []
        lista_modelos = []
        lista_campos = []
        lista_errores = []
        codigo = ''

        para_error = ''

        try:
            pass
        except Exception as e:
            lista_errores.append('Existe error en la construccion del Texto: ' + ' ' + str(e) + ' en la linea ' + para_error)
            context['lista_errores'] = lista_errores
            context['numero_errores'] = len(lista_errores)

        return context

def ProcesaLinea(linea_texto,proyecto,modelo,errores, codigo):
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

    comandos = ['read,', 'readF','select,','group,','create,','order,','orderd,','union,','filter','fields']
    
    palabra = ''
    texto = ''
    for caracter in linea_texto:
        if caracter == ']':
            antes_cerrado = palabra.strip()
            palabra = ''
            if antes_abierto == 'read':
                # if not ExisteModelo(antes_abierto,proyecto):
                #     errores.append('En la linea ' + linea_texto + ' ' + antes_cerrado + ' no es un modelo del proyecto')
                # else:
                tx = antes_cerrado.split(',')
                if len(tx) > 1:
                    texto = '\n' + tx[0] + ' = ' + tx[1] + '.objects.all()'
                else:
                    texto = '\n' + tx[0] + '.objects.all()'
            elif antes_abierto == 'readF':
                tx = antes_cerrado.split(',')
                if len(tx) > 2:
                    txp = tx[2].replace(';',',')
                    texto = '\n' + tx[0] + ' = ' + tx[1] + '.objects.filter(' + txp + ')'
                else:
                    texto = '\n' + tx[0] + '.objects.all()'
            elif antes_abierto == 'create':
                texto = '.annotate(' + antes_cerrado + ')'
            elif antes_abierto == 'select':
                # if not ExisteModelo(antes_abierto,proyecto):
                #     errores.append('En la linea ' + linea_texto + ' ' + antes_cerrado + ' no es un modelo del proyecto')
                # else:
                texto = '.select_related(' + antes_cerrado + ')'
            elif antes_abierto == 'order':
                texto = '.order_by(' + antes_cerrado + ')'
            elif antes_abierto == 'orderd':
                texto = '.order_by(' + '-' + antes_cerrado + ')'
            elif antes_abierto == 'group':
                texto = '.values(' + antes_cerrado + ')'
            elif antes_abierto == 'filter':
                texto = '.filter(' + antes_cerrado + ')'
            elif antes_abierto == 'union':
                tx = antes_cerrado.split(',')
                for i in range(len(tx)):
                    if i == 0:
                        texto = '\n' + tx[i] + ' = '
                    elif i == 1:
                        texto += tx[i]
                    else:
                        texto += '.union(' + tx[i] + ')'
            elif antes_abierto == 'fields':
                texto = '\nfields(' + antes_cerrado + ')'
            else:
                errores.append('La palabra antes de "(" debe ser: ' + ' '.join(comandos))
        elif caracter == '[':
            antes_abierto = palabra.strip()
            palabra = ''
        else:
            palabra += caracter

    antes_final = palabra.strip()
    # if antes_abierto == 'create':
    #     texto = '.annotate(' + antes_cerrado + ' = ' + antes_final + ')'

    return texto

def ExisteModelo(texto,proyecto):
    try:
        Modelo.objects.get(nombre = texto,proyecto=proyecto)
        return True
    except:
        return False
    
def ExistePropiedad(texto,modelo):
    try:
        Propiedad.objects.get(nombre = texto,modelo=modelo)
        return True
    except:
        return False
    
class ReporteAdHocModeloListView(ListView):
    model = ZonaReporteAdHoc
    template_name = 'modelos/reporte_adhoc_modelo_list.html'

    def get_context_data(self, **kwargs):
        context = super(ReporteAdHocModeloListView, self).get_context_data(**kwargs)

        # Recibe datos del reporte de un modelo
        try:
            proyecto_json = self.request.GET['json']
            modeloid = self.request.GET['modelo_id']
            user = self.request.user
            if self.request.GET['nuevo'] == "1":
                modelo = ZonaReporteAdHoc()
                modelo.texto =  proyecto_json
                modelo.modeloid = modeloid
                modelo.save()
            if self.request.GET['nuevo'] == "0":
                modelo = ZonaReporteAdHoc.objects.get(modeloid=modeloid)
                modelo.texto =  proyecto_json
                # texto_json = json.loads(texto_procesar.texto)['propiedades']
                modelo.save()            
        except Exception as e:
            pass

        try:
            modeloid = self.request.GET['modelo_id']
            context['modelo'] = Modelo.objects.get(id=modeloid)
            context['proyecto'] = context['modelo'].proyecto
            context['vigente'] = VerificaVigenciaUsuario(self.request.user)
            context['lista_json'] = ZonaReporteAdHoc.objects.filter(modeloid = modeloid)
            context['error'] = ''
        except Exception as e:
            context['error'] = str(e)

        # context['criterio'] = self.request.GET['criterio']
        return context

class ReporteAdHocModeloView(TemplateView):

    template_name = "modelos/reporte_adhoc_modelo.html"

    def get_success_url(self):
        return reverse_lazy('proyectos:arbol') + '?proyecto_id=' + self.request.GET['proyecto_id']

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def get_context_data(self,**kwargs):
        context = super(ReporteAdHocModeloView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            proyecto = Proyecto.objects.get(id = self.request.GET['proyecto_id'],usuario=self.request.user)
            modelo = Modelo.objects.get(id = self.request.GET['modelo_id'],proyecto=proyecto)
            context['proyecto'] = proyecto
            context['modelo'] = modelo
            # context['mensaje_error'] = self.request.GET['mensaje_error']
            # Enviamos el json de los reportes
            lista=[]
            zonas = []
            TablasRecusivas(modelo,lista,5,proyecto,modelo.id,1)
            context['lista'] = lista
            try:
                json = ZonaReporteAdHoc.objects.get(id=self.request.GET['id'])
                context['json'] = json.texto
                context['font'] = modelo.font
            except Exception as e:
                print(str(e))
                context['json'] = ''
            context['error'] = ''
        except Exception as e:
            context['error'] = '!!! No eres el propietario del proyecto !!!' + str(e)
        return context

class BorrarReporteAdHocJsonView(DeleteView):
    model = ZonaReporteAdHoc

    def get_success_url(self):
        return reverse_lazy('modelos:reporte_lista') + '?modelo_id=' + str(Modelo.objects.get(id=self.request.GET['modelo_id']).id) + '&criterio=' + self.request.GET['criterio']

    def get_context_data(self,**kwargs):
        context = super(BorrarReporteAdHocJsonView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        context['error'] = ''
        context['criterio'] = self.request.GET['criterio']
        return context

class BaseModeloView(ListView):
    model = Seccion
    template_name = 'modelos/base_modelo.html'

    def get_context_data(self, **kwargs):
        context = super(BaseModeloView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            num=1
            context['error'] = ''
            # proyecto = Proyecto.objects.get(usuario = self.request.user, id = self.request.GET['proyecto_id'])
            modelo = Modelo.objects.get(id = self.request.GET['modelo_id'])
            # Forma el arbol para el template
            # context['proyecto'] = proyecto
            context['modelo'] = modelo
            context['proyecto'] = modelo.proyecto
            # Crea la lista
            lista=[]
            rutinas.CreaListaSeccion(lista,Seccion,Fila,Columna,modelo.proyecto,modelo)
            # ns=0
            # nf=0
            # nc=0
            # num+=1
            # context['existe'] = False
            # lista = []
            # for seccion in Seccion.objects.filter(modelo=modelo):
            #     context['existe'] = True
            #     lista.append([seccion,'s',0,ns])
            #     num+=1
            #     ns+=1
            #     for fila in Fila.objects.filter(seccion=seccion):
            #         lista.append([fila,'f',50,nf])
            #         nf=+1
            #         for columna in Columna.objects.filter(fila=fila):
            #             fn = columna.fonttexto.split(',')[0]
            #             fs = columna.fonttexto.split(',')[1]
            #             fb = columna.fonttexto.split(',')[2]
            #             lista.append([columna,'c',100,nc,fn,fs,fb])
            #             nc+=1
            #     num+=1
            context['lista'] = lista

        except Exception as e:
            context['error'] = '!!! No eres el propietario del proyecto !!!' + str(e) + str(num)
        return context


class EditarSeccionView(UpdateView):
    model = Seccion
    form_class = SeccionForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('modelos:editar_seccion', args=[self.object.id]) + '?ok'

    def get_context_data(self,**kwargs):
        context = super(EditarSeccionView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(id=self.object.modelo.proyecto.id,usuario=self.request.user)
            modelo = Modelo.objects.get(id=self.object.modelo.id)
            context['proyecto'] = proyecto
            context['modelo'] = modelo
            context['nombre'] = self.object.nombre
            context['seccion'] = self.object
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        form = self.get_form()
        seccion = form.save(commit=False)
        mensaje_error=''
        modelo = Modelo.objects.get(id=self.request.GET['modelo_id'])
        if form.is_valid():
            seccion.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            mensaje_error = 'Error en el formulario, intente nuevamente'
            return HttpResponseRedirect('/modelos/editar_seccion/' + str(seccion.id) + '/?modelo_id=' + str(modelo.id) + '&mensaje_error=' + mensaje_error) 

class CrearSeccionView(CreateView):
    model = Seccion
    form_class = SeccionForm

    def get_success_url(self):
        return reverse_lazy('modelos:base_modelo') + '?modelo_id=' + self.request.GET['modelo_id']

    def get_context_data(self,**kwargs):
        context = super(CrearSeccionView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            context['error'] = ''
            # proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            modelo = Modelo.objects.get(id=self.request.GET['modelo_id'])
            # context['proyecto'] = proyecto
            context['modelo'] = modelo
        except Exception as e:
            context['error'] = '!!! No eres el propietario del proyecto !!!' + str(e)
        return context

    def post(self,request,*args,**kwargs):
        mensaje_error=''
        form = self.form_class(request.POST)
        modelo = Modelo.objects.get(id = request.GET['modelo_id'])
        if form.is_valid():
            seccion = form.save(commit=False)
            seccion.modelo = modelo
            seccion.save()
            return HttpResponseRedirect(self.get_success_url())
        return HttpResponseRedirect('/modelos/crear_seccion' + '/?modelo_id=' + str(modelo.id))             

class BorrarSeccionView(DeleteView):
    model = Seccion

    def get_success_url(self):
        return reverse_lazy('modelos:base_modelo') + '?modelo_id=' + self.request.GET['modelo_id']

    def get_context_data(self,**kwargs):
        context = super(BorrarSeccionView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            context['error'] = ''
            obj = Seccion.objects.get(id=self.object.id)
            context['nombre'] = obj.nombre
            # context['proyecto'] = obj.modelo.proyecto
            context['modelo'] = obj.modelo
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

class CrearFilaView(CreateView):
    model = Fila
    form_class = FilaForm

    def get_success_url(self):
        return reverse_lazy('modelos:base_modelo') + '?modelo_id=' + self.request.GET['modelo_id'] 

    def get_context_data(self,**kwargs):
        context = super(CrearFilaView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            # proyecto = Proyecto.objects.get(id = self.request.GET['proyecto_id'],usuario=self.request.user)
            modelo = Modelo.objects.get(id = self.request.GET['modelo_id'])
            seccion = Seccion.objects.get(id = self.request.GET['seccion_id'])
            # context['proyecto'] = proyecto
            # context['modelo'] = modelo
            context['seccion'] = seccion
            context['error'] = ''
        except Exception as e:
            context['error'] = '!!! No eres el propietario del proyecto !!!' + str(e)
        return context

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST, request.FILES)
        seccion = Seccion.objects.get(id = request.GET['seccion_id'])
        # proyecto = Proyecto.objects.get(id = request.GET['proyecto_id'])
        # modelo = Modelo.objects.get(id = self.request.GET['modelo_id'])
        mensaje_error = ''

        if form.is_valid():
            fila = form.save(commit=False)
            fila.seccion = seccion
            # Colocamos el valor del padre
            fila.save()
            return HttpResponseRedirect(self.get_success_url())
        # return HttpResponseRedirect('/modelos/crear_fila' + '/?proyecto_id=' + str(proyecto.id) + '&modelo_id=' + str(modelo.id) + '&seccion_id=' + str(seccion.id))
        return HttpResponseRedirect('/modelos/crear_fila' + '/?seccion_id=' + str(seccion.id))

class EditarFilaView(UpdateView):
    model = Fila
    form_class = FilaForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        fila = Fila.objects.get(id=self.request.GET['fila_id'])
        return reverse_lazy('modelos:editar_fila', args=[fila.id]) + '?ok&modelo_id=' + self.request.GET['modelo_id'] + '&seccion_id=' + self.request.GET['seccion_id']

    def get_context_data(self,**kwargs):
        context = super(EditarFilaView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            # proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            modelo = Modelo.objects.get(id=self.request.GET['modelo_id'])
            seccion = Seccion.objects.get(id=self.request.GET['seccion_id'])
            context['modelo'] = modelo
            # context['proyecto'] = proyecto
            context['seccion'] = seccion
            context['fila'] = self.object
            context['error'] = ''
        except Exception as e:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context
    
    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        form = self.get_form()
        fila = form.save(commit=False)
        fila.save()
        return HttpResponseRedirect(self.get_success_url())

class BorrarFilaView(DeleteView):
    model = Fila

    def get_success_url(self):
        return reverse_lazy('modelos:base_modelo') + '?modelo_id=' + self.request.GET['modelo_id']

    def get_context_data(self,**kwargs):
        context = super(BorrarFilaView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            fila = self.object
            context['fila'] = fila
            # context['proyecto'] = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            context['modelo'] = Modelo.objects.get(id=self.request.GET['modelo_id'])
            # context['seccion'] = Seccion.objects.get(id=self.request.GET['seccion_id'])
            context['nombre'] = fila.nombre
            context['error'] = ''
        except Exception as e:
            context['error'] = '!!! No eres el propietario del proyecto !!!' + str(e)
        return context

class CrearColumnaView(CreateView):
    model = Columna
    form_class = ColumnaForm

    def get_success_url(self):
        return reverse_lazy('modelos:base_modelo') + '?modelo_id=' + self.request.GET['modelo_id']

    def get_context_data(self,**kwargs):
        context = super(CrearColumnaView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            fila = Fila.objects.get(id=self.request.GET['fila_id'])
            context['fila'] = fila
            modelo = Modelo.objects.get(id=fila.seccion.modelo.id)
            context['modelo'] = modelo
            context['error'] = ''
            context['seccion'] = 'modelo'
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

    def post(self,request,*args,**kwargs):
        error = ''
        form = self.form_class(request.POST)
        fila = Fila.objects.get(id = request.GET['fila_id'])
        if form.is_valid():
            columna = form.save(commit=False)
            columna.fila = fila
            columna.save()
            return HttpResponseRedirect(self.get_success_url())
        response = redirect('modelos:crear_columna')
        response['Location'] += '?modelo_id=' + str(fila.seccion.modelo.id) + '&fila_id=' + str(fila.id)
        return response
        # return render(request, 'modelos/columna_form.html/&modelo_id=' + str(fila.seccion.modelo.id), {'form': form,'error':error})

class EditarColumnaView(UpdateView):
    model = Columna
    form_class = ColumnaForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('modelos:editar_columna', args=[self.object.id]) + '?ok&modelo_id=' + self.request.GET['modelo_id']

    def get_context_data(self,**kwargs):
        context = super(EditarColumnaView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            obj = self.object
            context['columna'] = obj
            context['fila'] = Fila.objects.get(id=obj.fila.id)
            modelo = Modelo.objects.get(id=self.request.GET['modelo_id'])
            context['modelo'] = modelo
            context['error'] = ''
            context['seccion'] = 'modelo'
            
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

class BorrarColumnaView(DeleteView):
    model = Columna

    def get_success_url(self):
        return reverse_lazy('modelos:base_modelo') + '?ok&modelo_id=' + self.request.GET['modelo_id']

    def get_context_data(self,**kwargs):
        context = super(BorrarColumnaView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            obj = self.object
            modelo = Modelo.objects.get(id=obj.fila.seccion.modelo.id)
            context['nombre'] = obj.nombre
            context['modelo'] = modelo
            context['error'] = ''
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context


