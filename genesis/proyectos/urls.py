from django.urls import path
from .views import ListaProyectosView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .views import ListaProyectosView, ArbolProyectoView, WizzardArbolProyectoView, CrearProyectoView, EditarProyectoView, BorrarProyectoView, dumpView, DesplegarPreciosView
from .views import ListaTextoView, CrearTextoView, EditarTextoView, BorrarTextoView, ProcesaTextoConCriterioView, EsquemaView, ListaJsonView, ListaObjetoView
from .views import CrearJsonView, ProcesaJsonView, BaseProyectoView
from .views import CrearSeccionView, EditarSeccionView, BorrarSeccionView
from .views import CrearFilaView, EditarFilaView, BorrarFilaView
from .views import CrearColumnaView, EditarColumnaView, BorrarColumnaView
from .views import CrearObjetoView, BorrarObjetoView,BorrarJsonView,ProcesarObjetoView, EditarObjetoView

proyectos_patterns = ([
    path('lista/', login_required(ListaProyectosView.as_view()), name='lista'),
    path('arbol/', login_required(ArbolProyectoView.as_view()), name='arbol'),
    path('wizzard_arbol/', login_required(WizzardArbolProyectoView.as_view()), name='wizzard_arbol'),
    path('crear/', login_required(CrearProyectoView.as_view()), name='crear'),
    path('crear_texto/', login_required(CrearTextoView.as_view()), name='crear_texto'),
    path('crear_json/', login_required(CrearJsonView.as_view()), name='crear_json'),
    path('crear_objeto/', login_required(CrearObjetoView.as_view()), name='crear_objeto'),
    path('lista_texto/', login_required(ListaTextoView.as_view()), name='lista_texto'),
    path('lista_json/', login_required(ListaJsonView.as_view()), name='lista_json'),
    path('lista_objeto/', login_required(ListaObjetoView.as_view()), name='lista_objeto'),
    path('editar_texto/<int:pk>/', login_required(EditarTextoView.as_view()), name='editar_texto'),
    path('editar_json/<int:pk>/', login_required(EditarTextoView.as_view()), name='editar_json'),
    path('editar_objeto/<int:pk>/', login_required(EditarObjetoView.as_view()), name='editar_objeto'),
    path('borrar_texto/<int:pk>/', login_required(BorrarTextoView.as_view()), name='borrar_texto'),
    path('borrar_json/<int:pk>/', login_required(BorrarJsonView.as_view()), name='borrar_json'),
    path('borrar_objeto/<int:pk>/', login_required(BorrarObjetoView.as_view()), name='borrar_objeto'),
    path('procesa_texto/', login_required(ProcesaTextoConCriterioView.as_view()), name='procesa_texto'),
    path('procesa_json/', login_required(ProcesaJsonView.as_view()), name='procesa_json'),
    path('procesa_objeto/', login_required(ProcesarObjetoView.as_view()), name='procesa_objeto'),
    path('editar/<int:pk>/',login_required(EditarProyectoView.as_view()), name='editar'),
    path('borrar/<int:pk>/',login_required(BorrarProyectoView.as_view()), name='borrar'),
    path('descarga/',login_required(dumpView.as_view()), name='descarga'),
    path('desplegar_precios', login_required(DesplegarPreciosView.as_view()), name='desplegar_precios'),
    path('esquema', login_required(EsquemaView.as_view()), name='esquema'),
    path('base_proyecto/',login_required(BaseProyectoView.as_view()), name='base_proyecto'),
    path('crear_seccion/',login_required(CrearSeccionView.as_view()), name='crear_seccion'),
    path('editar_seccion/<int:pk>/',login_required(EditarSeccionView.as_view()), name='editar_seccion'),
    path('borrar_seccion/<int:pk>/',login_required(BorrarSeccionView.as_view()), name='borrar_seccion'),
    path('crear_fila/',login_required(CrearFilaView.as_view()), name='crear_fila'),
    path('editar_fila/<int:pk>/',login_required(EditarFilaView.as_view()), name='editar_fila'),
    path('borrar_fila/<int:pk>/',login_required(BorrarFilaView.as_view()), name='borrar_fila'),
    path('crear_columna/',login_required(CrearColumnaView.as_view()), name='crear_columna'),
    path('editar_columna/<int:pk>/',login_required(EditarColumnaView.as_view()), name='editar_columna'),
    path('borrar_columna/<int:pk>/',login_required(BorrarColumnaView.as_view()), name='borrar_columna'),

], 'proyectos')