from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

#@[p_forms_seguridad_01]

class UserCreationFormWithEmail(UserCreationForm):
	email = forms.EmailField(required=True, help_text='Requerido, 254 caracteres como maximo, debe ser valido')
#@[p_forms_seguridad_02]
	class Meta:
#@[p_forms_seguridad_03]
		model = User
		fields = ('username','email','password1', 'password2')
#@[p_forms_seguridad_04]

	def clean_email(self):
#@[p_forms_seguridad_05]
		email = self.cleaned_data.get('email')
#@[p_forms_seguridad_06]
		if User.objects.filter(email=email).exists():
#@[p_forms_seguridad_07]
			raise forms.ValidationError('El email ya esta registrado, prueba con otro')
#@[p_forms_seguridad_08]
		return email

class ProfileForm(forms.ModelForm):
	class Meta:
#@[p_forms_seguridad_09]
		model = Profile
#@[p_forms_seguridad_10]
		fields = ('avatar', 'biografia',)
#@[p_forms_seguridad_11]
		widgets = {
			'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
			'biografia': forms.Textarea(attrs={'class':'form-control mt-3', 'rows': '5', 'placeholder': 'Biografia'}),
		}

class EmailForm(forms.ModelForm):
#@[p_forms_seguridad_12]
	email = forms.EmailField(required=True, help_text='Requerido, 254 caracteres como maximo, debe ser valido')
	
	class Meta:
#@[p_forms_seguridad_13]
	 	model = User
	 	fields = ['email']

	def clean_email(self):
#@[p_forms_seguridad_14]
		email = self.cleaned_data.get('email')
#@[p_forms_seguridad_15]
		if 'email' in self.changed_data:
#@[p_forms_seguridad_16]
			if User.objects.filter(email=email).exists():
#@[p_forms_seguridad_17]
				raise forms.ValidationError('El email ya esta registrado, prueba con otro')
#@[p_forms_seguridad_18]
		return email

#@[p_forms_seguridad_19]
 
