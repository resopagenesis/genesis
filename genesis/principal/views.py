from django.shortcuts import render
from .models import Seccion, Fila, Columna
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from registration.views import VerificaVigenciaUsuario
from proyectos.models import Proyecto
from .forms import SeccionForm, FilaForm, ColumnaForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.

class ArbolPrincipalView(ListView):
    model = Seccion
    template_name = 'principal/arbol_principal.html'

    def get_context_data(self, **kwargs):
        context = super(ArbolPrincipalView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(usuario = self.request.user, id = self.request.GET['proyecto_id'])
            # Forma el arbol para el template
            context['proyecto'] = proyecto
            context['proyecto_id'] = proyecto.id
            # Crea la lista
            ns=0
            nf=0
            nc=0

            lista = []
            for seccion in Seccion.objects.filter(proyecto=proyecto):
                lista.append([seccion,'s',0,ns])
                ns+=1
                for fila in Fila.objects.filter(seccion=seccion):
                    lista.append([fila,'f',50,nf])
                    nf=+1
                    for columna in Columna.objects.filter(fila=fila):
                        fn = columna.fonttexto.split(',')[0]
                        fs = columna.fonttexto.split(',')[1]
                        fb = columna.fonttexto.split(',')[2]
                        iw = columna.dimensionesimagen.split(',')[0]
                        ih = columna.dimensionesimagen.split(',')[1]
                        try:
                            margen = columna.margeninterno.split(',')[0] + ' ' + columna.margeninterno.split(',')[1] + ' ' + columna.margeninterno.split(',')[2] + ' ' + columna.margeninterno.split(',')[3]
                        except:
                            margen = '0px'
                        lista.append([columna,'c',100,nc,fn,fs,fb,iw,ih,margen])
                        nc+=1
            context['lista'] = lista

        except Exception as e:
            context['error'] = '!!! No eres el propietario del proyecto !!!' + str(e)
        return context


class EditarSeccionView(UpdateView):
    model = Seccion
    form_class = SeccionForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('principal:editar_seccion', args=[self.object.id]) + '?ok'

    def get_context_data(self,**kwargs):
        context = super(EditarSeccionView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            context['error'] = ''
            proyecto = Proyecto.objects.get(id=self.object.proyecto.id,usuario=self.request.user)
            context['proyecto'] = proyecto
            context['nombre'] = self.object.nombre
            context['proyecto_id'] = self.object.proyecto.id
            context['aplicacion'] = self.object
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
    model = Seccion
    form_class = SeccionForm

    def get_success_url(self):
        return reverse_lazy('principal:arbol') + '?proyecto_id=' + self.request.GET['proyecto_id']

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
    model = Seccion

    def get_success_url(self):
        return reverse_lazy('principal:arbol') + '?proyecto_id=' + self.request.GET['proyecto_id']

    def get_context_data(self,**kwargs):
        context = super(BorrarSeccionView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            context['error'] = ''
            obj = Seccion.objects.get(id=self.object.id)
            context['nombre'] = obj.nombre
            context['proyecto_id'] = obj.proyecto.id
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

class CrearFilaView(CreateView):
    model = Fila
    form_class = FilaForm

    def get_success_url(self):
        return reverse_lazy('principal:arbol') + '?proyecto_id=' + self.request.GET['proyecto_id']

    def get_context_data(self,**kwargs):
        context = super(CrearFilaView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            proyecto = Proyecto.objects.get(id = self.request.GET['proyecto_id'],usuario=self.request.user)
            seccion = Seccion.objects.get(id = self.request.GET['seccion_id'])
            context['proyecto'] = proyecto
            context['seccion'] = seccion
            context['error'] = ''
        except Exception as e:
            context['error'] = '!!! No eres el propietario del proyecto !!!' + str(e)
        return context

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST, request.FILES)
        seccion = Seccion.objects.get(id = request.GET['seccion_id'])
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
    model = Fila
    form_class = FilaForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        fila = Fila.objects.get(id=self.request.GET['fila_id'])
        return reverse_lazy('principal:editar_fila', args=[fila.id]) + '?ok&proyecto_id=' + self.request.GET['proyecto_id'] + '&seccion_id=' + self.request.GET['seccion_id']

    def get_context_data(self,**kwargs):
        context = super(EditarFilaView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            seccion = Seccion.objects.get(id=self.request.GET['seccion_id'])
            context['proyecto'] = proyecto
            context['seccion'] = seccion
            context['fila'] = Fila.objects.get(id=self.object.id)
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
        return reverse_lazy('principal:arbol') + '?proyecto_id=' + self.request.GET['proyecto_id']

    def get_context_data(self,**kwargs):
        context = super(BorrarFilaView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            obj = Fila.objects.get(id=self.object.id)
            context['fila'] = obj
            context['proyecto'] = Proyecto.objects.get(id=obj.seccion.proyecto.id)
            context['nombre'] = obj.nombre
            context['error'] = ''
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

class CrearColumnaView(CreateView):
    model = Columna
    form_class = ColumnaForm

    def get_success_url(self):
        return reverse_lazy('principal:arbol') + '?proyecto_id=' + self.request.GET['proyecto_id']

    def get_context_data(self,**kwargs):
        context = super(CrearColumnaView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            fila = Fila.objects.get(id=self.request.GET['fila_id'])
            context['fila'] = fila
            proyecto = Proyecto.objects.get(id=fila.seccion.proyecto.id,usuario=self.request.user)
            context['proyecto'] = proyecto
            context['error'] = ''
            context['seccion'] = 'principal'

        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        fila = Fila.objects.get(id = request.GET['fila_id'])
        if form.is_valid():
            columna = form.save(commit=False)
            columna.fila = fila
            columna.save()
            return HttpResponseRedirect(self.get_success_url())
        return render(request, 'principal/columna_form.html', {'form': form})

class EditarColumnaView(UpdateView):
    model = Columna
    form_class = ColumnaForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('principal:editar_columna', args=[self.object.id]) + '?ok&proyecto_id=' + self.request.GET['proyecto_id']

    def get_context_data(self,**kwargs):
        context = super(EditarColumnaView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            obj = self.object
            context['columna'] = obj
            context['fila'] = Fila.objects.get(id=obj.fila.id)
            proyecto = Proyecto.objects.get(id=self.request.GET['proyecto_id'],usuario=self.request.user)
            context['proyecto'] = proyecto
            context['error'] = ''
            context['seccion'] = 'principal'
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context

class BorrarColumnaView(DeleteView):
    model = Columna

    def get_success_url(self):
        return reverse_lazy('principal:arbol') + '?ok&proyecto_id=' + self.request.GET['proyecto_id']

    def get_context_data(self,**kwargs):
        context = super(BorrarColumnaView, self).get_context_data(**kwargs)
        context['vigente'] = VerificaVigenciaUsuario(self.request.user)
        try:
            obj = self.object
            fila = Fila.objects.get(id=obj.fila.id)
            proyecto = Proyecto.objects.get(id=fila.seccion.proyecto.id,usuario=self.request.user)
            context['nombre'] = obj.nombre
            context['proyecto'] = proyecto
            context['error'] = ''
        except:
            context['error'] = '!!! No eres el propietario del proyecto !!!'
        return context


