from django.urls import path
from .views import RegistroView, ProfileUpdate,EmailUpdate

#@[p_urls_seguridad_01]

registration_patterns = ([
#@[p_models_seguridad_02]
	path('registro/',RegistroView.as_view(), name='registro'),
	path('profile/',ProfileUpdate.as_view(), name='profile'),
	path('profile/email/',EmailUpdate.as_view(), name='profile_email'),
], 'registration')

#@[p_models_seguridad_03]
 
