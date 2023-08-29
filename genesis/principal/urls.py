from django.urls import path
from .views import CrearSeccionView, EditarSeccionView, BorrarSeccionView, ArbolPrincipalView
from .views import CrearFilaView, EditarFilaView, BorrarFilaView
from .views import CrearColumnaView, EditarColumnaView, BorrarColumnaView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

principal_patterns = ([
    path('arbol/', login_required(ArbolPrincipalView.as_view()), name='arbol'),
    path('crear_seccion/',login_required(CrearSeccionView.as_view()), name='crear_seccion'),
    path('editar_seccion/<int:pk>/',login_required(EditarSeccionView.as_view()), name='editar_seccion'),
    path('borrar_seccion/<int:pk>/',login_required(BorrarSeccionView.as_view()), name='borrar_seccion'),
    path('crear_fila/',login_required(CrearFilaView.as_view()), name='crear_fila'),
    path('editar_fila/<int:pk>/',login_required(EditarFilaView.as_view()), name='editar_fila'),
    path('borrar_fila/<int:pk>/',login_required(BorrarFilaView.as_view()), name='borrar_fila'),
    path('crear_columna/',login_required(CrearColumnaView.as_view()), name='crear_columna'),
    path('editar_columna/<int:pk>/',login_required(EditarColumnaView.as_view()), name='editar_columna'),
    path('borrar_columna/<int:pk>/',login_required(BorrarColumnaView.as_view()), name='borrar_columna'),
], 'principal')