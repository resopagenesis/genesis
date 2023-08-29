from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from seguridad.models import rol
from seguridad.models import modelo_rol
from seguridad.models import propiedad_rol
from seguridad.models import usuariorol
from seguridad.models import rolusuario







class rolForm(forms.ModelForm):
	class Meta:
		model = rol
		fields = ('nombre','descripcion',)
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control font_control_rol mt-1', 'placeholder': ''}),
			'descripcion': forms.Textarea(attrs={'class':'form-control  font_control_rol mt-1', 'placeholder': ''}),

		}
		labels = {
		'nombre':'Nombre','descripcion':'Descripcion',
		}


class modelo_rolForm(forms.ModelForm):
	class Meta:
		model = modelo_rol
		fields = ('nombre','puedelistar','puedeinsertar','puedeeditar','puedeborrar',)
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control font_control_modelo_rol mt-1', 'placeholder': ''}),
			'puedelistar': forms.CheckboxInput(attrs={'class':'font_control_modelo_rol mt-1', 'placeholder': ''}),
			'puedeinsertar': forms.CheckboxInput(attrs={'class':'font_control_modelo_rol mt-1', 'placeholder': ''}),
			'puedeeditar': forms.CheckboxInput(attrs={'class':'font_control_modelo_rol mt-1', 'placeholder': ''}),
			'puedeborrar': forms.CheckboxInput(attrs={'class':'font_control_modelo_rol mt-1', 'placeholder': ''}),

		}
		labels = {
		'nombre':'Nombre','puedelistar':'Puede listar','puedeinsertar':'Puede insertar','puedeeditar':'Puede editar','puedeborrar':'Puede borrar',
		}


class propiedad_rolForm(forms.ModelForm):
	class Meta:
		model = propiedad_rol
		fields = ('nombre','puedever','puedeasignarvalor','puedeeditar',)
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control font_control_propiedad_rol mt-1', 'placeholder': ''}),
			'puedever': forms.CheckboxInput(attrs={'class':'font_control_propiedad_rol mt-1', 'placeholder': ''}),
			'puedeasignarvalor': forms.CheckboxInput(attrs={'class':'font_control_propiedad_rol mt-1', 'placeholder': ''}),
			'puedeeditar': forms.CheckboxInput(attrs={'class':'font_control_propiedad_rol mt-1', 'placeholder': ''}),

		}
		labels = {
		'nombre':'Nombre','puedever':'Puede ver','puedeasignarvalor':'Puede asignar valor','puedeeditar':'Puede editar',
		}


class usuariorolForm(forms.ModelForm):
	class Meta:
		model = usuariorol
		fields = ('usuario',)
		widgets = {
			'usuario': forms.TextInput(attrs={'class':'form-control font_control_usuariorol mt-1', 'placeholder': ''}),

		}
		labels = {
		'usuario':'Usuario',
		}


class rolusuarioForm(forms.ModelForm):
	class Meta:
		model = rolusuario
		fields = ('rol',)
		widgets = {
			'rol': forms.Select(attrs={'class':'form-control  font_control_rolusuario mt-1'},choices=rol.objects.all()),

		}
		labels = {
		'rol':'Rol',
		}




 


