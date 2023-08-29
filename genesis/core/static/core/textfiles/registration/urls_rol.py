from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .views import HomeView
from .views import ListarrolView, CrearrolView, EditarrolView, BorrarrolView, ReporterolView
from .views import Crearmodelo_rolView, Editarmodelo_rolView, Borrarmodelo_rolView
from .views import Crearpropiedad_rolView, Editarpropiedad_rolView, Borrarpropiedad_rolView
from .views import ListarusuariorolView, CrearusuariorolView, EditarusuariorolView, BorrarusuariorolView, ReporteusuariorolView
from .views import CrearrolusuarioView, EditarrolusuarioView, BorrarrolusuarioView




seguridad_patterns = ([
	path('',(HomeView.as_view()), name='home'),
	path('listar_rol/',staff_member_required(ListarrolView.as_view()), name='listar_rol'),
	path('reporte_rol/',ReporterolView, name='reporte_rol'),
	path('editar_rol/<int:pk>/',(EditarrolView.as_view()), name='editar_rol'),
	path('crear_rol/',(CrearrolView.as_view()), name='crear_rol'),
	path('borrar_rol/<int:pk>/',(BorrarrolView.as_view()), name='borrar_rol'),

	path('editar_modelo_rol/<int:pk>/',(Editarmodelo_rolView.as_view()), name='editar_modelo_rol'),
	path('crear_modelo_rol/',(Crearmodelo_rolView.as_view()), name='crear_modelo_rol'),
	path('borrar_modelo_rol/<int:pk>/',(Borrarmodelo_rolView.as_view()), name='borrar_modelo_rol'),

	path('editar_propiedad_rol/<int:pk>/',(Editarpropiedad_rolView.as_view()), name='editar_propiedad_rol'),
	path('crear_propiedad_rol/',(Crearpropiedad_rolView.as_view()), name='crear_propiedad_rol'),
	path('borrar_propiedad_rol/<int:pk>/',(Borrarpropiedad_rolView.as_view()), name='borrar_propiedad_rol'),

	path('listar_usuariorol/',staff_member_required(ListarusuariorolView.as_view()), name='listar_usuariorol'),
	path('reporte_usuariorol/',ReporteusuariorolView, name='reporte_usuariorol'),
	path('editar_usuariorol/<int:pk>/',(EditarusuariorolView.as_view()), name='editar_usuariorol'),
	path('crear_usuariorol/',(CrearusuariorolView.as_view()), name='crear_usuariorol'),
	path('borrar_usuariorol/<int:pk>/',(BorrarusuariorolView.as_view()), name='borrar_usuariorol'),

	path('editar_rolusuario/<int:pk>/',(EditarrolusuarioView.as_view()), name='editar_rolusuario'),
	path('crear_rolusuario/',(CrearrolusuarioView.as_view()), name='crear_rolusuario'),
	path('borrar_rolusuario/<int:pk>/',(BorrarrolusuarioView.as_view()), name='borrar_rolusuario'),



], 'seguridad')


