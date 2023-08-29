# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Proyecto, ProyectoTexto, ProyectoObjeto
from django.core.exceptions import ValidationError
from .models import Seccion, Fila, Columna

JUSTIFICACION_CHOICES = (
   ('i', 'Izquierda'),
   ('d', 'Derecha'),
   ('c', 'Centro'),
	)

JUSTIFICACION_V_CHOICES = (
   ('s', 'Superior'),
   ('c', 'Centro'),
   ('i', 'Inferior'),
	)

JUSTIFICACION_S_CHOICES = (
   ('start', 'Izquierda'),
   ('end', 'Derecha'),
   ('center', 'Centro'),
	)

JUSTIFICACION_SV_CHOICES = (
   ('start', 'Superior'),
   ('center', 'Centro'),
   ('end', 'Inferior'),
	)

class ProyectoForm(forms.ModelForm):

	class Meta:
		model = Proyecto
		
		fields = ('nombre',
				  'descripcion',
				  'conseguridad',
				  'conetiquetaspersonalizacion',
				  'separacionsecciones',
				  'conbusqueda',
				  'conroles',
				  'imagentitulo',
				  'imagentitulowidth',
				  'imagentituloheight',
				  'justificacionverticaltitulo',
				  'justificacionhorizontaltitulo',
				  'titulo',
				  'fonttitulo',
				  'colortitulo',
				  'avatar',
				  'avatarheight',
				  'avatarwidth',
				  'justificacionhorizontallogo',
				  'justificacionverticallogo',
				  'fontmenu',
				  'colormenu',
				  'colorfondomenu',
				  'justificacionmenu',
				  'imagenvolver',
				  'textovolver',
				  'fonttextovolver',
				  'colortextovolver',

				#   'imagenpaginaprincipal',
				#   'colorpaginaprincipal',
				#   'segundocolorpaginaprincipal',
				#   'degradehaciaarriba',
				#   'altofilaenizcede',
				#   'colorfilaenizcede',
				#   'altocolumnaenizquierda',
				#   'colorcolumnaenizquierda',
				#   'numerocolumnaenizquierda',
				#   'altocolumnalogo',
				#   'colorcolumnalogo',
				#   'numerocolumnalogo',
				#   'altocolumnatitulo',
				#   'colorcolumnatitulo',
				#   'numerocolumnatitulo',
				#   'altocolumnalogin',
				#   'colorcolumnalogin',
				#   'numerocolumnalogin',
				#   'altocolumnaenderecha',
				#   'colorcolumnaenderecha',
				#   'numerocolumnaenderecha',
				#   'altofilabume',
				#   'colorfilabume',
				#   'altocolumnabumeizquierda',
				#   'colorcolumnabumeizquierda',
				#   'numerocolumnabumeizquierda',
				#   'altocolumnabusqueda',
				#   'colorcolumnabusqueda',
				#   'numerocolumnabusqueda',
				#   'altocolumnamenu',
				#   'colorcolumnamenu',
				#   'numerocolumnamenu',
				#   'altocolumnabumederecha',
				#   'colorcolumnabumederecha',
				#   'numerocolumnabumederecha',
				#   'altofilamedio',
				#   'colorfilamedio',
				#   'altocolumnamedioizquierda',
				#   'colorcolumnamedioizquierda',
				#   'numerocolumnamedioizquierda',
				#   'altocolumnamediocentro',
				#   'colorcolumnamediocentro',
				#   'numerocolumnamediocentro',
				#   'altocolumnamedioderecha',
				#   'colorcolumnamedioderecha',
				#   'numerocolumnamedioderecha',
				#   'altofilapie',
				#   'colorfilapie',
				#   'altocolumnapie',
				#   'colorcolumnapie',
				#   'menuscontiguos',
				#   'imagenmedio',
				#   'textomedio',
				#   'fonttextomedio',
				#   'colortextomedio',
				#   'enborde',
				#   'encolorborde',
				#   'enanchoborde',
				#   'bumeborde',
				#   'bumecolorborde',
				#   'bumeanchoborde',
				#   'cenborde',
				#   'cencolorborde',
				#   'cenanchoborde',
				#   'usabaseparticular',
   				  # 'primeralinea',
    			  # 'maxlineas',
    			  # 'anchologo',
    			  # 'altologo',
    			  # 'posxlogo',
    			  # 'posylogo',
    			  # 'posxnombre',
    			  # 'posynombre',
    			  # 'iniciolineax',
    			  # 'finallineax',
    			  # 'iniciolineay',
    			  # 'grosorlinea',
    			  # 'piex',
    			  # 'piey',
    			  # 'lineapiex',
    			  # 'lineapiey',

)

		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre del Proyecto'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Descripcion'}),
			'conseguridad': forms.CheckboxInput(),
			'conetiquetaspersonalizacion': forms.CheckboxInput(),
			'separacionsecciones': forms.NumberInput(attrs={'class':'form-control'}),
			'conroles': forms.CheckboxInput(),
			'conbusqueda': forms.CheckboxInput(),
			'imagentitulo': forms.ClearableFileInput(attrs={'class':'form-control'}),
			'imagentitulowidth': forms.NumberInput(attrs={'class':'form-control'}),
			'imagentituloheight': forms.NumberInput(attrs={'class':'form-control'}),
			'justificacionverticaltitulo': forms.Select(attrs={'class':'form-control'},choices=JUSTIFICACION_V_CHOICES),
			'justificacionhorizontaltitulo': forms.Select(attrs={'class':'form-control'},choices=JUSTIFICACION_CHOICES),
			'titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Titulo del Proyecto'}),
			'fonttitulo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Font del titulo'}),
			'colortitulo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Color del titulo'}),
			'avatar': forms.ClearableFileInput(attrs={'class':'form-control'}),
			'avatarwidth': forms.NumberInput(attrs={'class':'form-control'}),
			'avatarheight': forms.NumberInput(attrs={'class':'form-control'}),
			'justificacionhorizontallogo': forms.Select(attrs={'class':'form-control'},choices=JUSTIFICACION_CHOICES),
			'justificacionverticallogo': forms.Select(attrs={'class':'form-control'},choices=JUSTIFICACION_V_CHOICES),
			'fontmenu': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Font del Menu'}),
			'colormenu': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Color del Menu'}),
			'justificacionmenu': forms.Select(attrs={'class':'form-control'},choices=JUSTIFICACION_CHOICES),
			'colorfondomenu': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
			'imagenvolver': forms.ClearableFileInput(attrs={'class':'form-control'}),
			'textovolver': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Texto de volver'}),
			'fonttextovolver': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Font del texto volver'}),
			'colortextovolver': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Color del texto volver'}),

			# 'imagenpaginaprincipal': forms.ClearableFileInput(attrs={'class':'form-control'}),
			# 'colorpaginaprincipal': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
			# 'segundocolorpaginaprincipal': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
			# 'imagenmedio': forms.ClearableFileInput(attrs={'class':'form-control'}),
			# 'degradehaciaarriba': forms.CheckboxInput(),
            # 'usabaseparticular': forms.CheckboxInput(attrs={ 'class':'font_control'}),
			# 'colortextomedio': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Color del titulo'}),
			# 'altofilaenizcede': forms.NumberInput(attrs={'class':'form-control'}),
			# 'colorfilaenizcede': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Color del titulo'}),
			# 'altocolumnaenizquierda': forms.NumberInput(attrs={'class':'form-control'}),
			# 'colorcolumnaenizquierda': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Color del titulo'}),
			# 'numerocolumnaenizquierda': forms.NumberInput(attrs={'class':'form-control'}),
			# 'altocolumnalogo': forms.NumberInput(attrs={'class':'form-control'}),
			# 'colorcolumnalogo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Color del titulo'}),
			# 'numerocolumnalogo': forms.NumberInput(attrs={'class':'form-control'}),
			# 'altocolumnatitulo': forms.NumberInput(attrs={'class':'form-control'}),
			# 'colorcolumnatitulo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Color del titulo'}),
			# 'numerocolumnatitulo': forms.NumberInput(attrs={'class':'form-control'}),
			# 'altocolumnalogin': forms.NumberInput(attrs={'class':'form-control'}),
			# 'colorcolumnalogin': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Color del titulo'}),
			# 'numerocolumnalogin': forms.NumberInput(attrs={'class':'form-control'}),
			# 'altocolumnaenderecha': forms.NumberInput(attrs={'class':'form-control'}),
			# 'colorcolumnaenderecha': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Color del titulo'}),
			# 'numerocolumnaenderecha': forms.NumberInput(attrs={'class':'form-control'}),
			# 'altofilabume': forms.NumberInput(attrs={'class':'form-control'}),
			# 'colorfilabume': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Color del titulo'}),
			# 'altocolumnabumeizquierda': forms.NumberInput(attrs={'class':'form-control'}),
			# 'colorcolumnabumeizquierda': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Color del titulo'}),
			# 'numerocolumnabumeizquierda': forms.NumberInput(attrs={'class':'form-control'}),
			# 'altocolumnabusqueda': forms.NumberInput(attrs={'class':'form-control'}),
			# 'colorcolumnabusqueda': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Color del titulo'}),
			# 'numerocolumnabusqueda': forms.NumberInput(attrs={'class':'form-control'}),
			# 'altocolumnamenu': forms.NumberInput(attrs={'class':'form-control'}),
			# 'colorcolumnamenu': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Color del titulo'}),
			# 'numerocolumnamenu': forms.NumberInput(attrs={'class':'form-control'}),
			# 'altocolumnabumederecha': forms.NumberInput(attrs={'class':'form-control'}),
			# 'colorcolumnabumederecha': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Color del titulo'}),
			# 'numerocolumnabumederecha': forms.NumberInput(attrs={'class':'form-control'}),
			# 'altofilamedio': forms.NumberInput(attrs={'class':'form-control'}),
			# 'colorfilamedio': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Color del titulo'}),
			# 'altocolumnamedioizquierda': forms.NumberInput(attrs={'class':'form-control'}),
			# 'colorcolumnamedioizquierda': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Color del titulo'}),
			# 'numerocolumnamedioizquierda': forms.NumberInput(attrs={'class':'form-control'}),
			# 'altocolumnamediocentro': forms.NumberInput(attrs={'class':'form-control'}),
			# 'colorcolumnamediocentro': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Color del titulo'}),
			# 'numerocolumnamediocentro': forms.NumberInput(attrs={'class':'form-control'}),
			# 'altocolumnamedioderecha': forms.NumberInput(attrs={'class':'form-control'}),
			# 'colorcolumnamedioderecha': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Color del titulo'}),
			# 'numerocolumnamedioderecha': forms.NumberInput(attrs={'class':'form-control'}),
			# 'altofilapie': forms.NumberInput(attrs={'class':'form-control'}),
			# 'colorfilapie': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Color del titulo'}),
			# 'altocolumnapie': forms.NumberInput(attrs={'class':'form-control'}),
			# 'colorcolumnapie': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Color del titulo'}),
			# 'textomedio': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Texto de seccion central'}),
			# 'menuscontiguos': forms.CheckboxInput(),
			# 'encolorborde': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
			# 'enanchoborde': forms.NumberInput(attrs={'class':'form-control'}),
			# 'enborde': forms.CheckboxInput(),
			# 'bumecolorborde': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
			# 'bumeanchoborde': forms.NumberInput(attrs={'class':'form-control'}),
			# 'bumeborde': forms.CheckboxInput(),
			# 'cencolorborde': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
			# 'cenanchoborde': forms.NumberInput(attrs={'class':'form-control'}),
			# 'cenborde': forms.CheckboxInput(),

   			# 'primeralinea': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		# 'maxlineas':forms.NumberInput(attrs={'class':'form-control'}),
    		# 'anchologo': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		# 'altologo': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		# 'posxlogo': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		# 'posylogo': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		# 'posxnombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		# 'posynombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		# 'iniciolineax': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		# 'finallineax': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		# 'iniciolineay': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		# 'grosorlinea': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		# 'piex': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		# 'piey': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		# 'lineapiex': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		# 'lineapiey': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
		}
		labels = {
			'nombre':'', 
			'descripcion':'',
			'avatar':'',
			# 'imagenpaginaprincipal': '',
			# 'colorpaginaprincipal':'', 
			# 'segundocolorpaginaprincipal':'', 
			'colorfondomenu':'', 
			# 'degradehaciaarriba':'', 
			'conseguridad':'', 
			'conetiquetaspersonalizacion':'',
			'conbusqueda':'',
			'imagentitulo':'',
			'imagentitulowidth':'',
			'imagentituloheight':'',
			'justificacionhorizontallogo': '',
			'justificacionverticallogo': '',
			'justificacionhorizontaltitulo': '',
			'justificacionverticallogo': '',
		}

	def clean(self):
		nombre = self.cleaned_data['nombre']
		if ' ' in nombre:
		    raise forms.ValidationError('El nombre no debe tener espacios')


class ProyectoTextoForm(forms.ModelForm):

	class Meta:
		model = ProyectoTexto
		
		fields = ('titulo',
				  'texto_texto',
				  'lineacontigua'
)

		widgets = {
			'titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
            'texto_texto': forms.Textarea(attrs={'class':'form-control', 'placeholder': ''}),
            'lineacontigua': forms.CheckboxInput(),
		}
		labels = {
			'titulo':'', 
			'texto_texto':'',
			'lineacontigua':''
		}


class ProyectoObjetoForm(forms.ModelForm):

	class Meta:
		model = ProyectoObjeto
		
		fields = ('texto_objeto',)
		widgets = {
            'texto_objeto': forms.Textarea(attrs={'class':'form-control', 'placeholder': ''}),
            # 'textoobjetos': forms.Textarea(attrs={'class':'form-control', 'placeholder': ''}),
		}
		labels = {
			'texto_objeto':''
		}

DEGRADADO_CHOICES = (
   ('left', 'Izquierda'),
   ('right', 'Derecha'),
   ('top', 'Arriba'),
   ('bottom','Abajo')
	)

FUNCION_V_CHOICES = (
   ('l', 'Logo'),
   ('t', 'Titulo'),
   ('b', 'Busqueda'),
   ('m', 'Menu'),
   ('d', 'Datos'),
   ('o', 'Otros'),
   )

class SeccionForm(forms.ModelForm):

   class Meta:
      model = Seccion
      
      fields = ('nombre',
      			'color1',
              'color2',
              'degradado',
              'borde',
              'altura',
			  'imagen'
            )

      widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre de la Seccion'}),
         'color1': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
         'color2': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
         'degradado': forms.Select(attrs={'class':'form-control'},choices=DEGRADADO_CHOICES),
         'borde' : forms.CheckboxInput(attrs={'disabled':False}),
        #  'altura': forms.NumberInput(attrs={'class':'form-control'}),
		 'altura': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
		 'imagen': forms.ClearableFileInput(attrs={'class':'form-control'}),
      }

class FilaForm(forms.ModelForm):

   class Meta:
      model = Fila
      
      fields = ('nombre',
      			'color1',
              'color2',
              'degradado',
              'altura',
              'borde'
            )

      widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre de la Seccion'}),
         'color1': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
         'color2': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
         'degradado': forms.Select(attrs={'class':'form-control'},choices=DEGRADADO_CHOICES),
	     'altura': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
        #  'altura': forms.NumberInput(attrs={'class':'form-control'}),
         'borde' : forms.CheckboxInput(attrs={'disabled':False}),
      }

class ColumnaForm(forms.ModelForm):

   class Meta:
      model = Columna
      
      fields = ('nombre',
      			'color1',
              'color2',
              'degradado',
              'imagen',
              'textocolumna',
              'fonttexto',
              'colortexto',
              'secciones',
              'justificacionverticaltexto',
              'justificacionhorizontaltexto',
              'borde',
              'funcion',
	      	  'dimensionesimagen',
			  'margeninterno'
            )

      widgets = {
         'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre de la Columna'}),
         'textocolumna': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Texto'}),
         'imagen': forms.ClearableFileInput(attrs={'class':'form-control'}),
         'color1': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
         'color2': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
         'fonttexto': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Font del texto'}),
         'colortexto': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Color del texto'}),
         'degradado': forms.Select(attrs={'class':'form-control'},choices=DEGRADADO_CHOICES),
         'secciones': forms.NumberInput(attrs={'class':'form-control'}),
         'justificacionverticaltexto': forms.Select(attrs={'class':'form-control'},choices=JUSTIFICACION_SV_CHOICES),
         'justificacionhorizontaltexto': forms.Select(attrs={'class':'form-control'},choices=JUSTIFICACION_S_CHOICES),
         'borde' : forms.CheckboxInput(),
         'funcion': forms.Select(attrs={'class':'form-control'},choices=FUNCION_V_CHOICES),
         'dimensionesimagen': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Color del texto'}),
         'margeninterno': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Color del texto'}),
      }                     