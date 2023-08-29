from django import forms
from .models import Seccion, Fila, Columna



DEGRADADO_CHOICES = (
   ('left', 'Izquierda'),
   ('right', 'Derecha'),
   ('top', 'Arriba'),
   ('bottom','Abajo')
	)

JUSTIFICACION_CHOICES = (
   ('start', 'Izquierda'),
   ('end', 'Derecha'),
   ('center', 'Centro'),
	)

JUSTIFICACION_V_CHOICES = (
   ('start', 'Superior'),
   ('center', 'Centro'),
   ('end', 'Inferior'),
	)

class SeccionForm(forms.ModelForm):

	class Meta:
		model = Seccion
		
		fields = ('nombre',
				  'color1',
				  'color2',
				  'degradado',
				  'borde',
				  'altura'
				)

		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre de la Seccion'}),
			'color1': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
			'color2': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
			'degradado': forms.Select(attrs={'class':'form-control'},choices=DEGRADADO_CHOICES),
			'borde' : forms.CheckboxInput(attrs={'disabled':False}),
			'altura': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
			# 'altura': forms.NumberInput(attrs={'class':'form-control'}),
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
			'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre de la Fila'}),
			'color1': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
			'color2': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
			'degradado': forms.Select(attrs={'class':'form-control'},choices=DEGRADADO_CHOICES),
			'altura': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
			# 'altura': forms.NumberInput(attrs={'class':'form-control'}),
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
				  'ingresosistema',
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
			'justificacionverticaltexto': forms.Select(attrs={'class':'form-control'},choices=JUSTIFICACION_V_CHOICES),
			'justificacionhorizontaltexto': forms.Select(attrs={'class':'form-control'},choices=JUSTIFICACION_CHOICES),
			'borde' : forms.CheckboxInput(attrs={'disabled':False}),
			'ingresosistema' : forms.CheckboxInput(attrs={'disabled':False}),
			'dimensionesimagen': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Color del texto'}),
			'margeninterno': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Color del texto'}),
		}		