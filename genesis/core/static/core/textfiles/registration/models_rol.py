from django.db import models
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.contrib.auth.models import User


# Modelos Foreign

#@[p_rol_01]	

# Crear los modelo aqui.


class rol(models.Model):

#@[p_rol_02]	

	nombre = models.CharField(max_length=30,default='')
	descripcion = models.TextField(default ='')

#@[p_rol_03]	

	def __str__(self):
		return self.nombre

#@[p_rol_04]	

class modelo_rol(models.Model):

#@[p_rol_05]	

	nombre = models.CharField(max_length=30,default='')
	puedelistar =  models.BooleanField(default=True)
	puedeinsertar =  models.BooleanField(default=True)
	puedeeditar =  models.BooleanField(default=True)
	puedeborrar =  models.BooleanField(default=True)
	rol =  models.ForeignKey(rol, on_delete=models.CASCADE)

#@[p_rol_06]	

	def __str__(self):
		return self.nombre

#@[p_rol_07]	

class propiedad_rol(models.Model):

#@[p_rol_08]	

	nombre = models.CharField(max_length=30,default='')
	puedever =  models.BooleanField(default=True)
	puedeasignarvalor =  models.BooleanField(default=True)
	puedeeditar =  models.BooleanField(default=True)
	modelo_rol =  models.ForeignKey(modelo_rol, on_delete=models.CASCADE)

#@[p_rol_09]	

	def __str__(self):
		return self.nombre

#@[p_rol_10]	

class usuariorol(models.Model):

#@[p_rol_11]	

	usuario = models.CharField(max_length=30,default='')

#@[p_rol_12]	

	def __str__(self):
		return self.usuario

#@[p_rol_13]	

class rolusuario(models.Model):

#@[p_rol_14]	

	rol =  models.ForeignKey(rol, on_delete=models.CASCADE, related_name='%(class)s_rol')
	usuariorol =  models.ForeignKey(usuariorol, on_delete=models.CASCADE)

#@[p_rol_15]	

	def __str__(self):
		return self.rol.nombre

#@[p_rol_16]	



