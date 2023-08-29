from django.urls import path
from .views import HomeView, ListaErroresView, ConfigurarBaseView, PaletaView
from .views import ColoresView, OtrosView, ConfigurarModeloNuevaView
from .views import EditarReporteView, CrearBaseView
from .views import ConfigurarUpdateContiguoView, ConfigurarUpdateAbajoView, ConfigurarBorraView, ConfigurarBaseNuevaView
from .views import CrearPasosView, PreviewProyectoView, PreviewMainView, PreviewModeloInsertarView,PreviewModeloUpdateView,PreviewModeloBorrarView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .views import ConfiguraProyectoView, Conf_11, Conf_12, Conf_13, Conf_14, Conf_15
from .views import Conf_21, Conf_22, Conf_23, Conf_24
from .views import Conf_31, Conf_32, Conf_33, PanelAjustableView, PanelAjustableModeloView, WizzardView

crear_patterns = ([
    path('crear/',login_required(HomeView.as_view()), name='home'),
    path('lista/',login_required(ListaErroresView.as_view()), name='lista'),
    path('conf_base/',login_required(ConfigurarBaseView.as_view()), name='conf_base'),
    path('crear_base/',login_required(CrearBaseView.as_view()), name='crear_base'),
    # path('conf_base_nueva/',login_required(ConfigurarBaseNuevaView.as_view()), name='conf_base_nueva'),
    path('conf_base_nueva/',login_required(PanelAjustableView.as_view()), name='conf_base_nueva'),
    path('preview_main/',login_required(PreviewMainView.as_view()), name='preview_main'),
    path('preview_proyecto/',login_required(PreviewProyectoView.as_view()), name='preview_proyecto'),
    path('preview_modelo_insertar/',login_required(PreviewModeloInsertarView.as_view()), name='preview_modelo_insertar'),
    path('preview_modelo_update/',login_required(PreviewModeloUpdateView.as_view()), name='preview_modelo_update'),
    path('preview_modelo_borrar/',login_required(PreviewModeloBorrarView.as_view()), name='preview_modelo_borrar'),
    path('paleta/',login_required(PaletaView.as_view()), name='paleta'),
    path('colores/',login_required(ColoresView.as_view()), name='colores'),
    path('otros/',login_required(OtrosView.as_view()), name='otros'),
    path('conf_modelo/',login_required(PanelAjustableModeloView.as_view()), name='conf_modelo'),
    # path('conf_modelo/',login_required(ConfigurarModeloNuevaView.as_view()), name='conf_modelo'),
    path('conf_update_contiguo/',login_required(ConfigurarUpdateContiguoView.as_view()), name='conf_update_contiguo'),
    path('conf_update_abajo/',login_required(ConfigurarUpdateAbajoView.as_view()), name='conf_update_abajo'),
    path('conf_borra/',login_required(ConfigurarBorraView.as_view()), name='conf_borra'),
    path('crear_pasos/',login_required(CrearPasosView.as_view()), name='crear_pasos'),
    path('reporte/<int:pk>/',login_required(EditarReporteView.as_view()), name='reporte'),
    path('configura_proyecto/<int:pk>/',ConfiguraProyectoView.as_view(), name='configura_proyecto'),
    path('wizzard/',login_required(WizzardView.as_view()), name='wizzard'),

    path('conf_11/<int:pk>/',Conf_11.as_view(),name='conf_11'),
    path('conf_12/<int:pk>/',Conf_12.as_view(),name='conf_12'),
    path('conf_13/<int:pk>/',Conf_13.as_view(),name='conf_13'),
    path('conf_14/<int:pk>/',Conf_14.as_view(),name='conf_14'),
    path('conf_15/<int:pk>/',Conf_15.as_view(),name='conf_15'),
    path('conf_21/<int:pk>/',Conf_21.as_view(),name='conf_21'),
    path('conf_22/<int:pk>/',Conf_22.as_view(),name='conf_22'),
    path('conf_23/<int:pk>/',Conf_23.as_view(),name='conf_23'),
    path('conf_24/<int:pk>/',Conf_24.as_view(),name='conf_24'),
    path('conf_31/<int:pk>/',Conf_31.as_view(),name='conf_31'),
    path('conf_32/<int:pk>/',Conf_32.as_view(),name='conf_32'),
    path('conf_33/<int:pk>/',Conf_33.as_view(),name='conf_33'),
], 'crear')