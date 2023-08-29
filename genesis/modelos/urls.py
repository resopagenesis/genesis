from django.urls import path
from .views import CrearModeloView, EditarModeloView, BorrarModeloView, BaseModeloView, ReporteModeloView, ReporteModeloListView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .views import CrearSeccionView, EditarSeccionView, BorrarSeccionView
from .views import CrearFilaView, EditarFilaView, BorrarFilaView
from .views import CrearColumnaView, EditarColumnaView, BorrarColumnaView
from .views import  BorrarReporteJsonView
from .views import  BorrarReporteAdHocJsonView,ReporteAdHocModeloView, ReporteAdHocModeloListView
from .views import ReporteAdHocObjetoListView, CrearReporteAdHocObjetoView,EditarReporteAdHocObjetoView,BorrarReporteAdHocObjetoView,ProcesarReporteAdHocObjetoView
from .views import DashObjetoListView, CrearDashObjetoView,EditarDashObjetoView,BorrarDashObjetoView,ProcesarDashObjetoView
from .views import DashObjetoListView

modelos_patterns = ([
    path('crear/',login_required(CrearModeloView.as_view()), name='crear'),
    path('editar/<int:pk>/',login_required(EditarModeloView.as_view()), name='editar'),
    path('borrar/<int:pk>/',login_required(BorrarModeloView.as_view()), name='borrar'),
    path('base_modelo/',login_required(BaseModeloView.as_view()), name='base_modelo'),
    path('crear_seccion/',login_required(CrearSeccionView.as_view()), name='crear_seccion'),
    path('editar_seccion/<int:pk>/',login_required(EditarSeccionView.as_view()), name='editar_seccion'),
    path('borrar_seccion/<int:pk>/',login_required(BorrarSeccionView.as_view()), name='borrar_seccion'),
    path('crear_fila/',login_required(CrearFilaView.as_view()), name='crear_fila'),
    path('editar_fila/<int:pk>/',login_required(EditarFilaView.as_view()), name='editar_fila'),
    path('borrar_fila/<int:pk>/',login_required(BorrarFilaView.as_view()), name='borrar_fila'),
    path('crear_columna/',login_required(CrearColumnaView.as_view()), name='crear_columna'),
    path('editar_columna/<int:pk>/',login_required(EditarColumnaView.as_view()), name='editar_columna'),
    path('borrar_columna/<int:pk>/',login_required(BorrarColumnaView.as_view()), name='borrar_columna'),
    path('reporte/',login_required(ReporteModeloView.as_view()), name='reporte'),
    path('reporte_lista/',login_required(ReporteModeloListView.as_view()), name='reporte_lista'),
    path('borrar_reporte_json/<int:pk>/', login_required(BorrarReporteJsonView.as_view()), name='borrar_reporte_json'),
    path('reporte_adhoc_objeto_lista/', login_required(ReporteAdHocObjetoListView.as_view()), name='reporte_adhoc_objeto_lista'),
    path('crear_reporte_adhoc_objeto/', login_required(CrearReporteAdHocObjetoView.as_view()), name='crear_reporte_adhoc_objeto'),
    path('editar_reporte_adhoc_objeto/<int:pk>/', login_required(EditarReporteAdHocObjetoView.as_view()), name='editar_reporte_adhoc_objeto'),
    path('borrar_reporte_adhoc_objeto/<int:pk>/', login_required(BorrarReporteAdHocObjetoView.as_view()), name='borrar_reporte_adhoc_objeto'),
    path('procesar_reporte_adhoc_objeto/', login_required(ProcesarReporteAdHocObjetoView.as_view()), name='procesar_reporte_adhoc_objeto'),
    path('reporte_adhoc/',login_required(ReporteAdHocModeloView.as_view()), name='reporte_adhoc'),
    path('reporte_adhoc_lista/',login_required(ReporteAdHocModeloListView.as_view()), name='reporte_adhoc_lista'),
    path('borrar_reporte_adhoc_json/<int:pk>/', login_required(BorrarReporteAdHocJsonView.as_view()), name='borrar_reporte_adhoc__json'),
    path('procesar_dash_objeto/', login_required(ProcesarDashObjetoView.as_view()), name='procesar_dash_objeto'),
    path('dash_objeto_lista/', login_required(DashObjetoListView.as_view()), name='dash_objeto_lista'),
    path('crear_dash_objeto/', login_required(CrearDashObjetoView.as_view()), name='crear_dash_objeto'),
    path('editar_dash_objeto/<int:pk>/', login_required(EditarDashObjetoView.as_view()), name='editar_dash_objeto'),
    path('borrar_dash_objeto/<int:pk>/', login_required(BorrarDashObjetoView.as_view()), name='borrar_dash_objeto'),
], 'modelos')