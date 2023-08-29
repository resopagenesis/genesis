from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.base import TemplateView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Sum, Count, Avg, Q
import random
import datetime
from django import forms
import time
import os

# Reporte

from core.views import Reporte
from reportlab.lib.pagesizes import letter,landscape,portrait,A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, mm, cm
from reportlab.lib import colors

from core import views as roles
from seguridad.models import rol
from seguridad.models import modelo_rol
from seguridad.models import propiedad_rol
from seguridad.models import usuariorol
from seguridad.models import rolusuario




from .forms import rolForm
from .forms import modelo_rolForm
from .forms import propiedad_rolForm
from .forms import usuariorolForm
from .forms import rolusuarioForm




# Create your views here.
class HomeView(TemplateView):
	template_name = 'seguridad/home.html'

# Este modelo es independiente por lo que
# se elabora una lista de sus registros
class ListarrolView(ListView):
	# Definir el modelo a utilizar
	model = rol
	# Especificar el template HTML
	template_name = 'seguridad/rol_list.html'

	# Prepara los context para el HTML
	def get_context_data(self,**kwargs):
		context = super(ListarrolView, self).get_context_data(**kwargs)
		context['lista'] = rol.objects.all()
		context['unico'] = '0'
			# # Controla si el usuario puede ver la propiedad: nombre del modelo
			# context['puede_ver_nombre'] = roles.PuedeVerPropiedad('nombre',self.request.user.username)
			# # Controla si el usuario puede ver la propiedad: descripcion del modelo
			# context['puede_ver_descripcion'] = roles.PuedeVerPropiedad('descripcion',self.request.user.username)
			# # Controla si el usuario puede listar los registros del modelo
			# if not roles.PuedeListar('rol',self.request.user.username):
			# 	context['lista'] = None
			# # Controla si el usuario puede insertar registros al modelo
			# context['puede_insertar'] = roles.PuedeInsertar('rol',self.request.user.username)
			# # Controla si el usuario puede editar registros al modelo
			# context['puede_editar'] = roles.PuedeEditar('rol',self.request.user.username)
			# # Controla si el usuario puede borrar registros al modelo
			# context['puede_borrar'] = roles.PuedeBorrar('rol',self.request.user.username)
		return context

# Este modelo es independiente y esta vista
# es la utilizada para la edicion de un registro
# ya grabado en la Base de Datos
class EditarrolView(UpdateView):
	# Define el modelo
	model = rol
	# Define el formulario
	form_class = rolForm
	# Define el HTML de edicion
	template_name = 'seguridad/rol_update_form.html'

	# Procedimiento de salida despues de actualizacion exitosa
	def get_success_url(self):
		# Retorna al HTML de edicion con la comunicacion de correcta actualizacion
		return reverse_lazy('seguridad:editar_rol', args=[self.object.id]) + '?correcto'

	# Prepara los context para el HTML de edicion
	def get_context_data(self,**kwargs):
		context = super(EditarrolView, self).get_context_data(**kwargs)
		# Recupera el modelo a ser editado y envia su id
		rol = (self.object)
		context["rol"] = rol
		modelo_current = (self.object)
		context['rol_id'] = modelo_current.id
		modelo_rol_lista = modelo_rol.objects.filter(rol = rol)
		context['listamodelo_rol'] =  modelo_rol_lista
			# # Controla si el usuario puede listar registros del modelo: modelo_rol
			# if not roles.PuedeListar('modelo_rol',self.request.user.username):
			# 	context['listamodelo_rol'] = None
			# # Controla si el usuario puede ver el valor a la propiedad: nombre del modelo
			# context['puede_ver_nombre'] = roles.PuedeVerPropiedad('nombre',self.request.user.username)
			# # Controla si el usuario puede ver el valor a la propiedad: puedelistar del modelo
			# context['puede_ver_puedelistar'] = roles.PuedeVerPropiedad('puedelistar',self.request.user.username)
			# # Controla si el usuario puede ver el valor a la propiedad: puedeinsertar del modelo
			# context['puede_ver_puedeinsertar'] = roles.PuedeVerPropiedad('puedeinsertar',self.request.user.username)
			# # Controla si el usuario puede ver el valor a la propiedad: puedeeditar del modelo
			# context['puede_ver_puedeeditar'] = roles.PuedeVerPropiedad('puedeeditar',self.request.user.username)
			# # Controla si el usuario puede ver el valor a la propiedad: puedeborrar del modelo
			# context['puede_ver_puedeborrar'] = roles.PuedeVerPropiedad('puedeborrar',self.request.user.username)
			# # Controla si el usuario puede insertar registros al modelo: modelo_rol
			# context['puede_insertar_modelo_rol'] = roles.PuedeInsertar('modelo_rol',self.request.user.username)
			# # Controla si el usuario puede editar registros al modelo
			# context['puede_editar_modelo_rol'] = roles.PuedeEditar('modelo_rol',self.request.user.username)
			# # Controla si el usuario puede borrar registros al modelo
			# context['puede_borrar_modelo_rol'] = roles.PuedeBorrar('modelo_rol',self.request.user.username)

		# Envia el context con la identificacion que se dio al borrado
		context['nombre'] = str(modelo_current.nombre)
		# Envia el context con el numero de modelos dependientes
		context['numeromodelo_rol'] = modelo_rol.objects.filter(rol=rol).count()
			# # Controla si el usuario puede editar el valor a la propiedad: nombre del modelo
			# context['puede_editar_nombre'] = roles.PuedeEditarPropiedad('nombre',self.request.user.username)
			# # Controla si el usuario puede editar el valor a la propiedad: descripcion del modelo
			# context['puede_editar_descripcion'] = roles.PuedeEditarPropiedad('descripcion',self.request.user.username)
		return context

# Este modelo es independiente y esta vista
# es la utilizada para la insercion de un nuevo registro
# en la Base de Datos
class CrearrolView(CreateView):
	# Define el modelo cuyo registro se inserta
	model = rol
	# Define el formulario de controles
	form_class = rolForm
	# Define el HTML de insercion
	template_name = 'seguridad/rol_form.html'

	# Procedimiento de retorno por insercion exitosa
	def get_success_url(self):
		# Retorna al HTML de la lista de registros del modelo
		return reverse_lazy('seguridad:listar_rol') + '?correcto'
	# Prepara los context de insercion
	def get_context_data(self,**kwargs):
		context = super(CrearrolView, self).get_context_data(**kwargs)
			# # Controla si el usuario puede asignar el valor a la propiedad: nombre del modelo
			# context['puede_asignar_nombre'] = roles.PuedeAsignar('nombre',self.request.user.username)
			# # Controla si el usuario puede asignar el valor a la propiedad: descripcion del modelo
			# context['puede_asignar_descripcion'] = roles.PuedeAsignar('descripcion',self.request.user.username)
		return context

# Este modelo es independiente y esta vista
# es la utilizada para el borrado de un registro
# ya grabado en la Base de Datos
class BorrarrolView(DeleteView):
	# Define le modelo a borrar
	model = rol
	# Define el HTML de borrado
	template_name = 'seguridad/rol_confirm_delete.html'

	# Procedimiento de retorno por borrado exitoso
	def get_success_url(self):
		# Retorna al HTML de lista de registros del modelo
		return reverse_lazy('seguridad:listar_rol') + '?correcto'
	# Prepara los context de borrado
	def get_context_data(self,**kwargs):
		context = super(BorrarrolView, self).get_context_data(**kwargs)
		# Recupera el modelo a borrar y envia su id
		modelo_current = rol.objects.get(id=self.object.id)
		context['nombreborrar'] = str(modelo_current.nombre)
			# # Controla si el usuario puede borrar registros al modelo
			# context['puede_borrar'] = roles.PuedeBorrar('rol',self.request.user.username)
		return context

from reportlab.platypus import SimpleDocTemplate, Paragraph, Table,TableStyle, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape, A4

# Importamos la clase Flowable
from reportlab.platypus import Flowable

# Definimos nuestra clase linea que hereda de Flowable
class linea(Flowable):

    # Inicializamos la clase Flowable con los datos que llegan desde el que llama la clase  
    # definimos h que el la altura de la linea como 0 ya que la linea no tiene volumen  
    def __init__(self,w,h=0):
        Flowable.__init__(self)
        self.width = w
        self.height = h

    # dibujamos la linea en el canvas
    # No se especifica ni x ni y porque platypus se encarga de ponerla donde la necesitemos
    def draw(self):
        self.canv.line(0, self.height, self.width, self.height)


def ReporterolView(request):

	reportsize = letter
	nombre = 'rol'
	orientacion = portrait
	margenes = [20,20,20,20]
	font_titulo = 'Helvetica'
	font_titulo_size = 10
	font_columnas = 'Helvetica'
	font_columnas_size = 10
	font = 'Helvetica'
	font_size = 10
	font_encabezado = 'Helvetica'
	font_encabezado_size = 16

	doc = SimpleDocTemplate(nombre + '.pdf', pagesize=orientacion(reportsize),leftMargin=margenes[0],
		rigthMargin=margenes[1],
		topMargin=margenes[2],
		bottomMargin=margenes[3])

	doc.font = font_encabezado
	doc.fontSize = font_encabezado_size

	historia = []

	maxpuntos = 612 - doc.leftMargin - doc.rightMargin
	# 792,612,841,595

	# estilos

	tbl_estilo_titulo = TableStyle([('FONT', (0, 0), (-1, -1), font_titulo),
							('FONTSIZE', (0, 0), (-1, -1), font_titulo_size),
							('VALIGN',(0,0),(1,-1),'MIDDLE')])

	tbl_estilo_texto = TableStyle([('VALIGN',(0,0),(1,-1),'MIDDLE')])

	ps_columnas = ParagraphStyle(name = 'Normal', fontSize = font_columnas_size, fontName=font_columnas)
	ps_texto = ParagraphStyle(name = 'Normal', fontSize = font_size, fontName=font)

	# titulo
	historia.append(Spacer(1,15))
	data = [['Lista de registros']]
	tbl = Table(data)
	tbl.setStyle(EstiloTitulo('Helvetica',10))
	historia.append(tbl)
	historia.append(Spacer(1,15))
	# columnas
	data =[['',Paragraph('Rol', ParrafoEstiloColumnas('Helvetica',10)),Paragraph('Descripcion', ParrafoEstiloColumnas('Helvetica',10)),'']]
	tbl = Table(data, colWidths=[0,100,100,maxpuntos-200-0])
	tbl.setStyle(EstiloColumnas(1))
	historia.append(tbl)
	for reg_rol in rol.objects.all():
		# datos
		data =[['',Paragraph(reg_rol.nombre, ParrafoEstiloTexto('Helvetica',10)),Paragraph(reg_rol.descripcion, ParrafoEstiloTexto('Helvetica',10)),'',]]
		tbl = Table(data, colWidths=[0,100,100,maxpuntos-200-0])
		tbl.setStyle(tbl_estilo_texto)
		historia.append(tbl)
		if modelo_rol.objects.filter(rol = reg_rol).count() > 0:
			# titulo
			historia.append(Spacer(1,15))
			data = [['Lista de registros']]
			tbl = Table(data)
			tbl.setStyle(EstiloTitulo('Helvetica',10))
			historia.append(tbl)
			historia.append(Spacer(1,15))
			# columnas
			data =[['',Paragraph('Modelo', ParrafoEstiloColumnas('Helvetica',10)),Paragraph('Lista', ParrafoEstiloColumnas('Helvetica',10)),Paragraph('Inserta', ParrafoEstiloColumnas('Helvetica',10)),Paragraph('Edita', ParrafoEstiloColumnas('Helvetica',10)),Paragraph('Borra', ParrafoEstiloColumnas('Helvetica',10)),'']]
			tbl = Table(data, colWidths=[20,100,100,100,100,100,maxpuntos-500-20])
			tbl.setStyle(EstiloColumnas(1))
			historia.append(tbl)
			for reg_modelo_rol in modelo_rol.objects.filter(rol=reg_rol):
				# datos
				data =[['',Paragraph(reg_modelo_rol.nombre, ParrafoEstiloTexto('Helvetica',10)),Paragraph(reg_modelo_rol.puedelistar, ParrafoEstiloTexto('Helvetica',10)),Paragraph(reg_modelo_rol.puedeinsertar, ParrafoEstiloTexto('Helvetica',10)),Paragraph(reg_modelo_rol.puedeeditar, ParrafoEstiloTexto('Helvetica',10)),Paragraph(reg_modelo_rol.puedeborrar, ParrafoEstiloTexto('Helvetica',10)),'',]]
				tbl = Table(data, colWidths=[20,100,100,100,100,100,maxpuntos-500-20])
				tbl.setStyle(tbl_estilo_texto)
				historia.append(tbl)
			if propiedad_rol.objects.filter(modelo_rol = reg_modelo_rol).count() > 0:
				# titulo
				historia.append(Spacer(1,15))
				data = [['Lista de registros']]
				tbl = Table(data)
				tbl.setStyle(EstiloTitulo('Helvetica',10))
				historia.append(tbl)
				historia.append(Spacer(1,15))
				# columnas
				data =[['',Paragraph('Propiedad', ParrafoEstiloColumnas('Helvetica',10)),Paragraph('Ver', ParrafoEstiloColumnas('Helvetica',10)),Paragraph('Asignar', ParrafoEstiloColumnas('Helvetica',10)),Paragraph('Editar', ParrafoEstiloColumnas('Helvetica',10)),'']]
				tbl = Table(data, colWidths=[40,100,100,100,100,maxpuntos-400-40])
				tbl.setStyle(EstiloColumnas(1))
				historia.append(tbl)
				for reg_propiedad_rol in propiedad_rol.objects.filter(modelo_rol=reg_modelo_rol):
					# datos
					data =[['',Paragraph(reg_propiedad_rol.nombre, ParrafoEstiloTexto('Helvetica',10)),Paragraph(reg_propiedad_rol.puedever, ParrafoEstiloTexto('Helvetica',10)),Paragraph(reg_propiedad_rol.puedeasignarvalor, ParrafoEstiloTexto('Helvetica',10)),Paragraph(reg_propiedad_rol.puedeeditar, ParrafoEstiloTexto('Helvetica',10)),'',]]
					tbl = Table(data, colWidths=[40,100,100,100,100,maxpuntos-400-40])
					tbl.setStyle(tbl_estilo_texto)
					historia.append(tbl)


	doc.build(historia, onFirstPage=encabezado, onLaterPages=encabezado)
	return HttpResponseRedirect('/seguridad/listar_rol')
	

def EstiloColumnas(col):
	estilo = TableStyle([('VALIGN',(col,0),(1,-1),'MIDDLE'),
						('LINEBELOW',(col,0),(-1,0),0.25, colors.gray),
						('LINEABOVE',(col,0),(-1,0),0.25, colors.gray),
						])	

	return estilo

def EstiloTitulo(font,size):
	estilo = TableStyle([('FONT', (0, 0), (-1, -1), font),
							('FONTSIZE', (0, 0), (-1, -1), size),
							('VALIGN',(0,0),(1,-1),'MIDDLE')])	
	return estilo

def EstiloTexto():
	estilo = TableStyle([('VALIGN',(0,0),(1,-1),'MIDDLE')])
	return estilo

def ParrafoEstiloColumnas(font, size):
	estilo = ParagraphStyle(name = 'Normal', fontSize = size, fontName=font)
	return estilo

def ParrafoEstiloTexto(font,size):
	estilo = ParagraphStyle(name = 'Normal', fontSize = size, fontName=font)
	return estilo

def encabezado(canvas,document):
	cd = os.getcwd()
	logo = cd + "/core/static/core/img/logo.png"
	im_auto = Image(logo, 15,15)

	data = [[im_auto,'Medicina General']]
	tblstyle = TableStyle([('LINEBELOW', (0, 0), (-1, -1), 0.5, colors.black),
							('FONT', (0, 0), (-1, -1), document.font),
							('FONTSIZE', (0, 0), (-1, -1), document.fontSize),
							('VALIGN',(1,0),(1,0),'MIDDLE'),
							('ALIGN', (1, 0), (1, 0), 'CENTER'),
							('BOTTOMPADDING', (1, 0), (1, 0), 15)
							])
	t = Table(data,colWidths=[30,582])
	t.setStyle(tblstyle)
	t.wrapOn(canvas,document.leftMargin,792 - (document.topMargin) * 0.6)
	t.drawOn(canvas, document.leftMargin,792 - (document.topMargin) * 0.6) 	

# Este modelo es independiente por lo que
# se elabora una lista de sus registros
class ListarusuariorolView(ListView):
	# Definir el modelo a utilizar
	model = usuariorol
	# Especificar el template HTML
	template_name = 'seguridad/usuariorol_list.html'

	# Prepara los context para el HTML
	def get_context_data(self,**kwargs):
		context = super(ListarusuariorolView, self).get_context_data(**kwargs)
		context['lista'] = usuariorol.objects.all()
		context['unico'] = '0'
			# # Controla si el usuario puede ver la propiedad: usuario del modelo
			# context['puede_ver_usuario'] = roles.PuedeVerPropiedad('usuario',self.request.user.username)
			# # Controla si el usuario puede listar los registros del modelo
			# if not roles.PuedeListar('usuariorol',self.request.user.username):
			# 	context['lista'] = None
			# # Controla si el usuario puede insertar registros al modelo
			# context['puede_insertar'] = roles.PuedeInsertar('usuariorol',self.request.user.username)
			# # Controla si el usuario puede editar registros al modelo
			# context['puede_editar'] = roles.PuedeEditar('usuariorol',self.request.user.username)
			# # Controla si el usuario puede borrar registros al modelo
			# context['puede_borrar'] = roles.PuedeBorrar('usuariorol',self.request.user.username)
		return context

# Este modelo es independiente y esta vista
# es la utilizada para la edicion de un registro
# ya grabado en la Base de Datos
class EditarusuariorolView(UpdateView):
	# Define el modelo
	model = usuariorol
	# Define el formulario
	form_class = usuariorolForm
	# Define el HTML de edicion
	template_name = 'seguridad/usuariorol_update_form.html'

	# Procedimiento de salida despues de actualizacion exitosa
	def get_success_url(self):
		# Retorna al HTML de edicion con la comunicacion de correcta actualizacion
		return reverse_lazy('seguridad:editar_usuariorol', args=[self.object.id]) + '?correcto'

	# Prepara los context para el HTML de edicion
	def get_context_data(self,**kwargs):
		context = super(EditarusuariorolView, self).get_context_data(**kwargs)
		# Recupera el modelo a ser editado y envia su id
		usuariorol = (self.object)
		context["usuariorol"] = usuariorol
		modelo_current = (self.object)
		context['usuariorol_id'] = modelo_current.id
		rolusuario_lista = rolusuario.objects.filter(usuariorol = usuariorol)
		context['listarolusuario'] =  rolusuario_lista
			# # Controla si el usuario puede listar registros del modelo: rolusuario
			# if not roles.PuedeListar('rolusuario',self.request.user.username):
			# 	context['listarolusuario'] = None
			# # Controla si el usuario puede ver el valor a la propiedad: rol del modelo
			# context['puede_ver_rol'] = roles.PuedeVerPropiedad('rol',self.request.user.username)
			# # Controla si el usuario puede insertar registros al modelo: rolusuario
			# context['puede_insertar_rolusuario'] = roles.PuedeInsertar('rolusuario',self.request.user.username)
			# # Controla si el usuario puede editar registros al modelo
			# context['puede_editar_rolusuario'] = roles.PuedeEditar('rolusuario',self.request.user.username)
			# # Controla si el usuario puede borrar registros al modelo
			# context['puede_borrar_rolusuario'] = roles.PuedeBorrar('rolusuario',self.request.user.username)

		# Envia el context con la identificacion que se dio al borrado
		context['nombre'] = str(modelo_current.usuario)
		# Envia el context con el numero de modelos dependientes
		context['numerorolusuario'] = rolusuario.objects.filter(usuariorol=usuariorol).count()
			# # Controla si el usuario puede editar el valor a la propiedad: usuario del modelo
			# context['puede_editar_usuario'] = roles.PuedeEditarPropiedad('usuario',self.request.user.username)
		return context

# Este modelo es independiente y esta vista
# es la utilizada para la insercion de un nuevo registro
# en la Base de Datos
class CrearusuariorolView(CreateView):
	# Define el modelo cuyo registro se inserta
	model = usuariorol
	# Define el formulario de controles
	form_class = usuariorolForm
	# Define el HTML de insercion
	template_name = 'seguridad/usuariorol_form.html'

	# Procedimiento de retorno por insercion exitosa
	def get_success_url(self):
		# Retorna al HTML de la lista de registros del modelo
		return reverse_lazy('seguridad:listar_usuariorol') + '?correcto'
	# Prepara los context de insercion
	def get_context_data(self,**kwargs):
		context = super(CrearusuariorolView, self).get_context_data(**kwargs)
			# # Controla si el usuario puede asignar el valor a la propiedad: usuario del modelo
			# context['puede_asignar_usuario'] = roles.PuedeAsignar('usuario',self.request.user.username)
		return context

# Este modelo es independiente y esta vista
# es la utilizada para el borrado de un registro
# ya grabado en la Base de Datos
class BorrarusuariorolView(DeleteView):
	# Define le modelo a borrar
	model = usuariorol
	# Define el HTML de borrado
	template_name = 'seguridad/usuariorol_confirm_delete.html'

	# Procedimiento de retorno por borrado exitoso
	def get_success_url(self):
		# Retorna al HTML de lista de registros del modelo
		return reverse_lazy('seguridad:listar_usuariorol') + '?correcto'
	# Prepara los context de borrado
	def get_context_data(self,**kwargs):
		context = super(BorrarusuariorolView, self).get_context_data(**kwargs)
		# Recupera el modelo a borrar y envia su id
		modelo_current = usuariorol.objects.get(id=self.object.id)
		context['nombreborrar'] = str(modelo_current.usuario)
			# # Controla si el usuario puede borrar registros al modelo
			# context['puede_borrar'] = roles.PuedeBorrar('usuariorol',self.request.user.username)
		return context

from reportlab.platypus import SimpleDocTemplate, Paragraph, Table,TableStyle, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape, A4

# Importamos la clase Flowable
from reportlab.platypus import Flowable

# Definimos nuestra clase linea que hereda de Flowable
class linea(Flowable):

    # Inicializamos la clase Flowable con los datos que llegan desde el que llama la clase  
    # definimos h que el la altura de la linea como 0 ya que la linea no tiene volumen  
    def __init__(self,w,h=0):
        Flowable.__init__(self)
        self.width = w
        self.height = h

    # dibujamos la linea en el canvas
    # No se especifica ni x ni y porque platypus se encarga de ponerla donde la necesitemos
    def draw(self):
        self.canv.line(0, self.height, self.width, self.height)


def ReporteusuariorolView(request):

	reportsize = letter
	nombre = 'usuariorol'
	orientacion = portrait
	margenes = [20,20,20,20]
	font_titulo = 'Helvetica'
	font_titulo_size = 10
	font_columnas = 'Helvetica'
	font_columnas_size = 10
	font = 'Helvetica'
	font_size = 10
	font_encabezado = 'Helvetica'
	font_encabezado_size = 16

	doc = SimpleDocTemplate(nombre + '.pdf', pagesize=orientacion(reportsize),leftMargin=margenes[0],
		rigthMargin=margenes[1],
		topMargin=margenes[2],
		bottomMargin=margenes[3])

	doc.font = font_encabezado
	doc.fontSize = font_encabezado_size

	historia = []

	maxpuntos = 612 - doc.leftMargin - doc.rightMargin
	# 792,612,841,595

	# estilos

	tbl_estilo_titulo = TableStyle([('FONT', (0, 0), (-1, -1), font_titulo),
							('FONTSIZE', (0, 0), (-1, -1), font_titulo_size),
							('VALIGN',(0,0),(1,-1),'MIDDLE')])

	tbl_estilo_texto = TableStyle([('VALIGN',(0,0),(1,-1),'MIDDLE')])

	ps_columnas = ParagraphStyle(name = 'Normal', fontSize = font_columnas_size, fontName=font_columnas)
	ps_texto = ParagraphStyle(name = 'Normal', fontSize = font_size, fontName=font)

	# titulo
	historia.append(Spacer(1,15))
	data = [['Lista de registros']]
	tbl = Table(data)
	tbl.setStyle(EstiloTitulo('Helvetica',10))
	historia.append(tbl)
	historia.append(Spacer(1,15))
	# columnas
	data =[['',Paragraph('Usuario', ParrafoEstiloColumnas('Helvetica',10)),'']]
	tbl = Table(data, colWidths=[0,100,maxpuntos-100-0])
	tbl.setStyle(EstiloColumnas(1))
	historia.append(tbl)
	for reg_usuariorol in usuariorol.objects.all():
		# datos
		data =[['',Paragraph(reg_usuariorol.usuario, ParrafoEstiloTexto('Helvetica',10)),'',]]
		tbl = Table(data, colWidths=[0,100,maxpuntos-100-0])
		tbl.setStyle(tbl_estilo_texto)
		historia.append(tbl)
		if rolusuario.objects.filter(usuariorol = reg_usuariorol).count() > 0:
			# titulo
			historia.append(Spacer(1,15))
			data = [['Lista de registros']]
			tbl = Table(data)
			tbl.setStyle(EstiloTitulo('Helvetica',10))
			historia.append(tbl)
			historia.append(Spacer(1,15))
			# columnas
			data =[['',Paragraph('Rol', ParrafoEstiloColumnas('Helvetica',10)),'']]
			tbl = Table(data, colWidths=[20,100,maxpuntos-100-20])
			tbl.setStyle(EstiloColumnas(1))
			historia.append(tbl)
			for reg_rolusuario in rolusuario.objects.filter(usuariorol=reg_usuariorol):
				# datos
				data =[['',Paragraph(str(reg_rolusuario.rol.nombre), ParrafoEstiloTexto('Helvetica',10)),'',]]
				tbl = Table(data, colWidths=[20,100,maxpuntos-100-20])
				tbl.setStyle(tbl_estilo_texto)
				historia.append(tbl)


	doc.build(historia, onFirstPage=encabezado, onLaterPages=encabezado)
	return HttpResponseRedirect('/seguridad/listar_usuariorol')
	

def EstiloColumnas(col):
	estilo = TableStyle([('VALIGN',(col,0),(1,-1),'MIDDLE'),
						('LINEBELOW',(col,0),(-1,0),0.25, colors.gray),
						('LINEABOVE',(col,0),(-1,0),0.25, colors.gray),
						])	

	return estilo

def EstiloTitulo(font,size):
	estilo = TableStyle([('FONT', (0, 0), (-1, -1), font),
							('FONTSIZE', (0, 0), (-1, -1), size),
							('VALIGN',(0,0),(1,-1),'MIDDLE')])	
	return estilo

def EstiloTexto():
	estilo = TableStyle([('VALIGN',(0,0),(1,-1),'MIDDLE')])
	return estilo

def ParrafoEstiloColumnas(font, size):
	estilo = ParagraphStyle(name = 'Normal', fontSize = size, fontName=font)
	return estilo

def ParrafoEstiloTexto(font,size):
	estilo = ParagraphStyle(name = 'Normal', fontSize = size, fontName=font)
	return estilo

def encabezado(canvas,document):
	cd = os.getcwd()
	logo = cd + "/core/static/core/img/logo.png"
	im_auto = Image(logo, 15,15)

	data = [[im_auto,'Medicina General']]
	tblstyle = TableStyle([('LINEBELOW', (0, 0), (-1, -1), 0.5, colors.black),
							('FONT', (0, 0), (-1, -1), document.font),
							('FONTSIZE', (0, 0), (-1, -1), document.fontSize),
							('VALIGN',(1,0),(1,0),'MIDDLE'),
							('ALIGN', (1, 0), (1, 0), 'CENTER'),
							('BOTTOMPADDING', (1, 0), (1, 0), 15)
							])
	t = Table(data,colWidths=[30,582])
	t.setStyle(tblstyle)
	t.wrapOn(canvas,document.leftMargin,792 - (document.topMargin) * 0.6)
	t.drawOn(canvas, document.leftMargin,792 - (document.topMargin) * 0.6) 	





# Este modelo es dependiente de rol
# Vista que es utilizada para la edicion del
# modelo modelo_rol cuyos registros y se encuentran
# grabados en la Base de Datos
class Editarmodelo_rolView(UpdateView):
	# El modelo que se edita
	model = modelo_rol
	# El formulario para la edicion
	form_class = modelo_rolForm
	# El HTML que se despliega ante el usuario
	template_name = 'seguridad/modelo_rol_update_form.html'

	# El procedimiento de salida de la edicion
	def get_success_url(self):
		# El modelo modelo_rol es independiente
		# Despues de editar el modelo se vuelve al HTML de edicion
		# con el mensaje de actualizacion correcta del registro
		try:
			if self.request.GET["esquema"] != "sin_treeview":
				return reverse_lazy('seguridad:editar_rol', args=[self.request.GET['id_raiz']]) + '?correcto'
		except:
				return reverse_lazy('seguridad:editar_rol', args=[self.request.GET['rol_id']]) + '?correcto'

	# Se preparan los context para enviarlos al HTML de edicion
	def get_context_data(self,**kwargs):
		context = super(Editarmodelo_rolView, self).get_context_data(**kwargs)
		# Se recupera el registro de modelo_rol que se edita
		modelo_current = (self.object)
		# Se envian al HTML el id del modelo y su campo que lo identifica
		# Este campo fue el que se definio como identificador de borrado del modelo
		context['modelo_rol_id'] = modelo_current.id
		context['nombre'] = str(modelo_current.nombre)
		# Se envia al HTML la lista de los modelos dependientes de modelo_rol
		propiedad_rol_propiedad_rol = propiedad_rol.objects.filter(modelo_rol = modelo_current)
		context['listapropiedad_rol'] =  propiedad_rol_propiedad_rol

		# Se recupera el modelo padre y se envia su id
		context['rol_id'] = modelo_current.rol.id

# Se envia al HTML el numero de modelos dependientes de modelo_rol
		context['numeropropiedad_rol'] = propiedad_rol.objects.filter(modelo_rol=modelo_current).count()

		modelo_x_modelo_rol = modelo_current
		modelo_x_rol = rol.objects.get(id=modelo_x_modelo_rol.rol.id)
		context["rol"] = modelo_x_rol

		try:
			context["esquema"] = self.request.GET["esquema"]
		except:
			context["esquema"] = "sin_treeview"
			# # Controla si el usuario puede editar el valor a la propiedad: nombre del modelo
			# context['puede_editar_nombre'] = roles.PuedeEditarPropiedad('nombre',self.request.user.username)
			# # Controla si el usuario puede editar el valor a la propiedad: puedelistar del modelo
			# context['puede_editar_puedelistar'] = roles.PuedeEditarPropiedad('puedelistar',self.request.user.username)
			# # Controla si el usuario puede editar el valor a la propiedad: puedeinsertar del modelo
			# context['puede_editar_puedeinsertar'] = roles.PuedeEditarPropiedad('puedeinsertar',self.request.user.username)
			# # Controla si el usuario puede editar el valor a la propiedad: puedeeditar del modelo
			# context['puede_editar_puedeeditar'] = roles.PuedeEditarPropiedad('puedeeditar',self.request.user.username)
			# # Controla si el usuario puede editar el valor a la propiedad: puedeborrar del modelo
			# context['puede_editar_puedeborrar'] = roles.PuedeEditarPropiedad('puedeborrar',self.request.user.username)
		return context

# Este modelo es dependiente de rol
# Esta vista es utilizada para el registro de nuevos
# registros del modelo modelo_rol
class Crearmodelo_rolView(CreateView):
	# Se define el modelo cuyo registro de inserta
	model = modelo_rol
	# El formulario para el nuevo registro
	form_class = modelo_rolForm
	# El HTML para el nuevo registro
	template_name = 'seguridad/modelo_rol_form.html'

	# El procedimiento de salida de la insercion
	def get_success_url(self):
		# Despues de la insercion del registro, el control
		# retorna al HTML de edicion del modelo padre
		return reverse_lazy('seguridad:editar_rol', args=[self.request.GET['rol_id']]) + '?correcto'

	# Procedimiento para el clik de insercion
	def post(self,request,*args,**kwargs):
		# Se recupera el formulario con los controles ya llenos
		form = self.form_class(request.POST)
		# Se recupera el registro del modelo padre 
		rol_post = rol.objects.get(id = request.GET['rol_id'])
		if form.is_valid():
		# El formulario es valido, no existen incongruencias
		# Se graba el registro en la base de datos pero 
		# la grabacion se mantiene pendiente, sin commit 
			modelo_rol= form.save(commit=False)
			# Se asigna a modelo_rol la dependencia con el modelo padre
			modelo_rol.rol = rol_post
			# Se graba el registro definitivamente en la base de datos 
			modelo_rol.save()
			# Se leva el control al procedimiento de salida por grabacion exitosa
			return HttpResponseRedirect(self.get_success_url())
		else:
			# Se leva el control al HTML de insercion grabacion no exitosa
			return self.render_to_response(self.get_context_data(form=form))

	def get_context_data(self,**kwargs):
		context = super(Crearmodelo_rolView, self).get_context_data(**kwargs)
		# Se recupera el objeto padre y se envia su id
		context['rol_id'] = self.request.GET['rol_id']
		return context

# Este modelo es dependiente de rol
# Esta vista es utilizada para el borrado de
# registros del modelo modelo_rol
class Borrarmodelo_rolView(DeleteView):
	# Se define el modelo a borrar
	model = modelo_rol
	# El template HTML para desplegar la opcion de borrado
	template_name = 'seguridad/modelo_rol_confirm_delete.html'

	# El procedimiento de salida del borrado
	def get_success_url(self):
		# El control vuelve a la edicion del modelo padre
		return reverse_lazy('seguridad:editar_rol', args=[self.request.GET['rol_id']]) + '?correcto'

	# Se preparan los contextos para el HTML de borrado
	def get_context_data(self,**kwargs):
		context = super(Borrarmodelo_rolView, self).get_context_data(**kwargs)
		# Se recupera el modelo y se envia el nombre definido para el borrado
		modelo_current = modelo_rol.objects.get(id=self.object.id)
		context['nombreborrar'] = str(modelo_current.nombre)
		# Se recupera el modelo padre y se envia su id
		context['rol_id'] = modelo_current.rol.id

		return context

# Este modelo es dependiente de modelo_rol
# Vista que es utilizada para la edicion del
# modelo propiedad_rol cuyos registros y se encuentran
# grabados en la Base de Datos
class Editarpropiedad_rolView(UpdateView):
	# El modelo que se edita
	model = propiedad_rol
	# El formulario para la edicion
	form_class = propiedad_rolForm
	# El HTML que se despliega ante el usuario
	template_name = 'seguridad/propiedad_rol_update_form.html'

	# El procedimiento de salida de la edicion
	def get_success_url(self):
		# El modelo propiedad_rol es dependiente
		# Despues de editar el modelo se vuelve al HTML de edicion
		# con el mensaje de actualizacion correcta del registro
		try:
			if self.request.GET["esquema"] == "sin_treeview":
				return reverse_lazy('seguridad:editar_rol', args=[self.request.GET['id_raiz']]) + '?correcto'
		except:
				return reverse_lazy('seguridad:editar_modelo_rol', args=[self.request.GET['modelo_rol_id']]) + '?correcto' + '&rol_id=' + str(self.request.GET['rol_id'])

	# Se preparan los context para enviarlos al HTML de edicion
	def get_context_data(self,**kwargs):
		context = super(Editarpropiedad_rolView, self).get_context_data(**kwargs)
		# Se recupera el registro de propiedad_rol que se edita
		modelo_current = (self.object)
		# Se envian al HTML el id del modelo y su campo que lo identifica
		# Este campo fue el que se definio como identificador de borrado del modelo
		context['propiedad_rol_id'] = modelo_current.id
		context['nombre'] = str(modelo_current.nombre)

		context['modelo_rol_id'] = modelo_current.modelo_rol.id
		# Se recupera el modelo abuelo y se envia su id
		modelo_rol_modelo_rol = modelo_rol.objects.get(id=modelo_current.modelo_rol.id)
		context['rol_id'] = modelo_rol_modelo_rol.rol.id


		modelo_x_propiedad_rol = modelo_current
		modelo_x_modelo_rol = modelo_rol.objects.get(id=modelo_x_propiedad_rol.modelo_rol.id)
		context["modelo_rol"] = modelo_x_modelo_rol
		modelo_x_rol = rol.objects.get(id=modelo_x_modelo_rol.rol.id)
		context["rol"] = modelo_x_rol

		try:
			context["esquema"] = self.request.GET["esquema"]
		except:
			context["esquema"] = "sin_treeview"
			# # Controla si el usuario puede editar el valor a la propiedad: nombre del modelo
			# context['puede_editar_nombre'] = roles.PuedeEditarPropiedad('nombre',self.request.user.username)
			# # Controla si el usuario puede editar el valor a la propiedad: puedever del modelo
			# context['puede_editar_puedever'] = roles.PuedeEditarPropiedad('puedever',self.request.user.username)
			# # Controla si el usuario puede editar el valor a la propiedad: puedeasignarvalor del modelo
			# context['puede_editar_puedeasignarvalor'] = roles.PuedeEditarPropiedad('puedeasignarvalor',self.request.user.username)
			# # Controla si el usuario puede editar el valor a la propiedad: puedeeditar del modelo
			# context['puede_editar_puedeeditar'] = roles.PuedeEditarPropiedad('puedeeditar',self.request.user.username)
		return context

# Este modelo es dependiente de modelo_rol
# Esta vista es utilizada para el registro de nuevos
# registros del modelo propiedad_rol
class Crearpropiedad_rolView(CreateView):
	# Se define el modelo cuyo registro de inserta
	model = propiedad_rol
	# El formulario para el nuevo registro
	form_class = propiedad_rolForm
	# El HTML para el nuevo registro
	template_name = 'seguridad/propiedad_rol_form.html'

	# El procedimiento de salida de la insercion
	def get_success_url(self):
		# Despues de la insercion del registro, el control
		# retorna al HTML de edicion del modelo padre
		return reverse_lazy('seguridad:editar_modelo_rol', args=[self.request.GET['modelo_rol_id']]) + '?correcto' + '&rol_id=' + str(self.request.GET['rol_id'])

	# Procedimiento para el clik de insercion
	def post(self,request,*args,**kwargs):
		# Se recupera el formulario con los controles ya llenos
		form = self.form_class(request.POST)
		# Se recupera el registro del modelo padre 
		modelo_rol_post = modelo_rol.objects.get(id = request.GET['modelo_rol_id'])
		if form.is_valid():
		# El formulario es valido, no existen incongruencias
		# Se graba el registro en la base de datos pero 
		# la grabacion se mantiene pendiente, sin commit 
			propiedad_rol= form.save(commit=False)
			# Se asigna a propiedad_rol la dependencia con el modelo padre
			propiedad_rol.modelo_rol = modelo_rol_post
			# Se graba el registro definitivamente en la base de datos 
			propiedad_rol.save()
			# Se leva el control al procedimiento de salida por grabacion exitosa
			return HttpResponseRedirect(self.get_success_url())
		else:
			# Se leva el control al HTML de insercion grabacion no exitosa
			return self.render_to_response(self.get_context_data(form=form))

	# Se preparan los context para enviarlos al HTML de insercion
	def get_context_data(self,**kwargs):
		context = super(Crearpropiedad_rolView, self).get_context_data(**kwargs)
		# Se recupera el objeto padre y se envia su id
		obj = modelo_rol.objects.get(id=self.request.GET['modelo_rol_id'])
		context['modelo_rol_id'] = obj.id
		# Se recupera el modelo abuelo y se envia su id
		rol_rol = rol.objects.get(id=obj.rol.id)
		context['rol_id'] = rol_rol.id
		return context

# Este modelo es dependiente de modelo_rol
# Esta vista es utilizada para el borrado de
# registros del modelo propiedad_rol
class Borrarpropiedad_rolView(DeleteView):
	# Se define el modelo a borrar
	model = propiedad_rol
	# El template HTML para desplegar la opcion de borrado
	template_name = 'seguridad/propiedad_rol_confirm_delete.html'

	# El procedimiento de salida del borrado
	def get_success_url(self):
		# El control vuelve a la edicion del modelo padre
		return reverse_lazy('seguridad:editar_modelo_rol', args=[self.request.GET['modelo_rol_id']]) + '?correcto'

	# Se preparan los contextos para el HTML de borrado
	def get_context_data(self,**kwargs):
		context = super(Borrarpropiedad_rolView, self).get_context_data(**kwargs)
		# Se recupera el modelo y se envia el nombre definido para el borrado
		modelo_current = propiedad_rol.objects.get(id=self.object.id)
		context['nombreborrar'] = str(modelo_current.nombre)
		context['modelo_rol_id'] = modelo_current.modelo_rol.id
		# Se recupera el modelo abuelo y se envia su id
		modelo_rol_modelo_rol = modelo_rol.objects.get(id=modelo_current.modelo_rol.id)
		context['rol_id'] = modelo_rol_modelo_rol.rol.id

		return context

# Este modelo es dependiente de usuariorol
# Vista que es utilizada para la edicion del
# modelo rolusuario cuyos registros y se encuentran
# grabados en la Base de Datos
class EditarrolusuarioView(UpdateView):
	# El modelo que se edita
	model = rolusuario
	# El formulario para la edicion
	form_class = rolusuarioForm
	# El HTML que se despliega ante el usuario
	template_name = 'seguridad/rolusuario_update_form.html'

	# El procedimiento de salida de la edicion
	def get_success_url(self):
		# El modelo rolusuario es independiente
		# Despues de editar el modelo se vuelve al HTML de edicion
		# con el mensaje de actualizacion correcta del registro
		try:
			if self.request.GET["esquema"] != "sin_treeview":
				return reverse_lazy('seguridad:editar_usuariorol', args=[self.request.GET['id_raiz']]) + '?correcto'
		except:
				return reverse_lazy('seguridad:editar_usuariorol', args=[self.request.GET['usuariorol_id']]) + '?correcto'

	# Se preparan los context para enviarlos al HTML de edicion
	def get_context_data(self,**kwargs):
		context = super(EditarrolusuarioView, self).get_context_data(**kwargs)
		# Se recupera el registro de rolusuario que se edita
		modelo_current = (self.object)
		# Se envian al HTML el id del modelo y su campo que lo identifica
		# Este campo fue el que se definio como identificador de borrado del modelo
		context['rolusuario_id'] = modelo_current.id
		context['nombre'] = str(modelo_current.rol.nombre)

		# Se recupera el modelo padre y se envia su id
		context['usuariorol_id'] = modelo_current.usuariorol.id


		modelo_x_rolusuario = modelo_current
		modelo_x_usuariorol = usuariorol.objects.get(id=modelo_x_rolusuario.usuariorol.id)
		context["usuariorol"] = modelo_x_usuariorol

		try:
			context["esquema"] = self.request.GET["esquema"]
		except:
			context["esquema"] = "sin_treeview"
		# Controla si el usuario puede editar el valor a la propiedad: rol del modelo
		context['puede_editar_rol'] = roles.PuedeEditarPropiedad('rol',self.request.user.username)
		return context

# Este modelo es dependiente de usuariorol
# Esta vista es utilizada para el registro de nuevos
# registros del modelo rolusuario
class CrearrolusuarioView(CreateView):
	# Se define el modelo cuyo registro de inserta
	model = rolusuario
	# El formulario para el nuevo registro
	form_class = rolusuarioForm
	# El HTML para el nuevo registro
	template_name = 'seguridad/rolusuario_form.html'

	# El procedimiento de salida de la insercion
	def get_success_url(self):
		# Despues de la insercion del registro, el control
		# retorna al HTML de edicion del modelo padre
		return reverse_lazy('seguridad:editar_usuariorol', args=[self.request.GET['usuariorol_id']]) + '?correcto'

	# Procedimiento para el clik de insercion
	def post(self,request,*args,**kwargs):
		# Se recupera el formulario con los controles ya llenos
		form = self.form_class(request.POST)
		# Se recupera el registro del modelo padre 
		usuariorol_post = usuariorol.objects.get(id = request.GET['usuariorol_id'])
		if form.is_valid():
		# El formulario es valido, no existen incongruencias
		# Se graba el registro en la base de datos pero 
		# la grabacion se mantiene pendiente, sin commit 
			rolusuario= form.save(commit=False)
			# Se asigna a rolusuario la dependencia con el modelo padre
			rolusuario.usuariorol = usuariorol_post
			# Se graba el registro definitivamente en la base de datos 
			rolusuario.save()
			# Se leva el control al procedimiento de salida por grabacion exitosa
			return HttpResponseRedirect(self.get_success_url())
		else:
			# Se leva el control al HTML de insercion grabacion no exitosa
			return self.render_to_response(self.get_context_data(form=form))

	def get_context_data(self,**kwargs):
		context = super(CrearrolusuarioView, self).get_context_data(**kwargs)
		# Se recupera el objeto padre y se envia su id
		context['usuariorol_id'] = self.request.GET['usuariorol_id']
		return context

# Este modelo es dependiente de usuariorol
# Esta vista es utilizada para el borrado de
# registros del modelo rolusuario
class BorrarrolusuarioView(DeleteView):
	# Se define el modelo a borrar
	model = rolusuario
	# El template HTML para desplegar la opcion de borrado
	template_name = 'seguridad/rolusuario_confirm_delete.html'

	# El procedimiento de salida del borrado
	def get_success_url(self):
		# El control vuelve a la edicion del modelo padre
		return reverse_lazy('seguridad:editar_usuariorol', args=[self.request.GET['usuariorol_id']]) + '?correcto'

	# Se preparan los contextos para el HTML de borrado
	def get_context_data(self,**kwargs):
		context = super(BorrarrolusuarioView, self).get_context_data(**kwargs)
		# Se recupera el modelo y se envia el nombre definido para el borrado
		modelo_current = rolusuario.objects.get(id=self.object.id)
		context['nombreborrar'] = str(modelo_current.rol.nombre)
		# Se recupera el modelo padre y se envia su id
		context['usuariorol_id'] = modelo_current.usuariorol.id

		return context







# # General de Reportes
# def Acomoda(datos,datos_reporte,primeralinea,titulo=False,datos_titulo=[]):

#     numeroLineas = datos_reporte[0]
#     pagina = datos_reporte[2]
#     salto = datos_reporte[1]
#     maxlineas = datos_reporte[3]

#     nuevapagina = False
#     if pagina == 1:
#         # encabezado
#         Encabezado(datos,pagina)
#         salto = 0
#         pagina += 1
#     if numeroLineas >= maxlineas:
#         nuevapagina = True
#         numeroLineas = 0
#         maxlineas = 50
#         datos.append([0])
#     if nuevapagina:
#         # encabezado
#         Encabezado(datos,pagina)
#         salto = 0
#         pass
#     if titulo:
#         numeroLineas += 1
#         salto += 0.5    	
#         datos.append([1,['Helvetica-Bold',9,colors.black],[datos_titulo[0][1],primeralinea-salto],datos_titulo[0][0],'c'])
#         numeroLineas += 1
#         salto += 0.4
#         # Fecha
#         if datos_titulo[1][0]:
#             datos.append([3,['Helvetica',8,colors.red],[datos_titulo[1][1],primeralinea-salto],'c'])
#             salto += 0.5
#             numeroLineas += 1
#         # Linea superior de columnas
#         datos.append([4,[datos_titulo[2],primeralinea-salto,datos_titulo[3],primeralinea-salto,datos_titulo[4]]])    
#         salto += 0.4
#         # Columnas
#         pos = 0
#         for col in range(0,len(datos_titulo[5]),2):
#             datos.append([1,['Helvetica-Bold',9,colors.black],[datos_titulo[5][col],primeralinea-salto],datos_titulo[5][col+1],'l'])
#             pos+=2
#         salto += 0.2
#         # Linea inferior de columnas
#         datos.append([4,[datos_titulo[2],primeralinea-salto,datos_titulo[3],primeralinea-salto,datos_titulo[4]]])    
#         numeroLineas += 2
#         salto += 0.5

#     datos_reporte[0] =  numeroLineas
#     datos_reporte[1] = salto 
#     datos_reporte[2] = pagina 
#     datos_reporte[3] = maxlineas 

# def Encabezado(datos,pagina):

#     anchologo=@anchologo
#     altologo=@altologo
#     posxlogo=@posxlogo
#     posylogo=@posylogo
#     posxnombre=@posxnombre
#     posynombre=@posynombre
#     iniciolineax=@iniciolineax
#     finallineax=@finallineax
#     iniciolineay=@iniciolineay
#     grosorlinea=@grosorlineaencabezado
#     piex=@piex
#     piey=@piey
#     lineapiex = @lineapiex
#     lineapiey=@lineapiey
#     nombre = 'clinica'

#     logo = None
#     try:
#         cd = os.getcwd()
#         logo = cd + '/core/static/core/img/logo.png'
#     except:
#         pass     

#     datos.append([2,logo,[posxlogo,posylogo],[anchologo,altologo]])       
#     datos.append([1,['Helvetica',20,colors.black],[posxnombre,posynombre],nombre,'c'])
#     datos.append([4,[iniciolineax,iniciolineay,finallineax, iniciolineay,grosorlinea]])
#     # Pie
#     datos.append([1,['Helvetica',8,colors.black],[piex,piey],'Pag. ' + str(pagina),'c'])
#     datos.append([4,[iniciolineax,lineapiey,lineapiex,lineapiey,grosorlinea]])     


