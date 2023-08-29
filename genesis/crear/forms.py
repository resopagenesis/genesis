from django import forms

from .models import ReporteNuevo

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


class ReporteForm(forms.ModelForm):
	class Meta:
		model = ReporteNuevo
		fields = ('primeralinea',
    			  'maxlineas',
    			  'anchologo',
    			  'altologo',
    			  'posxlogo',
    			  'posylogo',
    			  'posxnombre',
    			  'posynombre',
    			  'iniciolineax',
    			  'finallineax',
    			  'iniciolineay',
    			  'grosorlinea',
    			  'piex',
    			  'piey',
    			  'lineapiex',
    			  'lineapiey',)
		widgets = {
   			'primeralinea': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		'maxlineas':forms.NumberInput(attrs={'class':'form-control'}),
    		'anchologo': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		'altologo': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		'posxlogo': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		'posylogo': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		'posxnombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		'posynombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		'iniciolineax': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		'finallineax': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		'iniciolineay': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		'grosorlinea': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		'piex': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		'piey': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		'lineapiex': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
    		'lineapiey': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
		}

from proyectos.models import Proyecto

class Conf_11Form(forms.ModelForm):

    class Meta:
        model = Proyecto
        
        fields = ('altofilaenizcede','altocolumnaenizquierda', 'colorfilaenizcede','colorcolumnaenizquierda','numerocolumnaenizquierda','enborde','enanchoborde','encolorborde')

        widgets = {
            'altofilaenizcede': forms.NumberInput(attrs={'class':'form-control'}),
            'altocolumnaenizquierda': forms.NumberInput(attrs={'class':'form-control'}),
            'colorfilaenizcede': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
            'colorcolumnaenizquierda': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
            'numerocolumnaenizquierda': forms.NumberInput(attrs={'class':'form-control'}),
            'encolorborde': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
            'enanchoborde': forms.NumberInput(attrs={'class':'form-control'}),
            'enborde': forms.CheckboxInput(),
        }

class Conf_12Form(forms.ModelForm):

    class Meta:
        model = Proyecto
        
        fields = ('avatarheight','avatarwidth','altocolumnalogo','colorcolumnalogo', 'numerocolumnalogo','justificacionhorizontallogo','justificacionverticallogo')

        widgets = {
            'altocolumnalogo': forms.NumberInput(attrs={'class':'form-control'}),
            'numerocolumnalogo': forms.NumberInput(attrs={'class':'form-control'}),
            'colorcolumnalogo': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
            'justificacionhorizontallogo': forms.Select(attrs={'class':'form-control'},choices=JUSTIFICACION_CHOICES),
            'justificacionverticallogo': forms.Select(attrs={'class':'form-control'},choices=JUSTIFICACION_V_CHOICES),
            'avatarwidth': forms.NumberInput(attrs={'class':'form-control'}),
            'avatarheight': forms.NumberInput(attrs={'class':'form-control'}),
        }

class Conf_13Form(forms.ModelForm):

    class Meta:
        model = Proyecto
        
        fields = ('imagentitulowidth','imagentituloheight','altocolumnatitulo','colorcolumnatitulo', 'numerocolumnatitulo','justificacionhorizontaltitulo','justificacionverticaltitulo')

        widgets = {
            'altocolumnatitulo': forms.NumberInput(attrs={'class':'form-control'}),
            'numerocolumnatitulo': forms.NumberInput(attrs={'class':'form-control'}),
            'colorcolumnatitulo': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
            'justificacionhorizontaltitulo': forms.Select(attrs={'class':'form-control'},choices=JUSTIFICACION_CHOICES),
            'justificacionverticaltitulo': forms.Select(attrs={'class':'form-control'},choices=JUSTIFICACION_V_CHOICES),
            'imagentitulowidth': forms.NumberInput(attrs={'class':'form-control'}),
            'imagentituloheight': forms.NumberInput(attrs={'class':'form-control'}),
        }

class Conf_14Form(forms.ModelForm):

    class Meta:
        model = Proyecto
        
        fields = ('altocolumnalogin','colorcolumnalogin','numerocolumnalogin')

        widgets = {
            'altocolumnalogin': forms.NumberInput(attrs={'class':'form-control'}),
            'colorcolumnalogin': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
            'numerocolumnalogin': forms.NumberInput(attrs={'class':'form-control'}),
        }

class Conf_15Form(forms.ModelForm):

    class Meta:
        model = Proyecto
        
        fields = ('altocolumnaenderecha', 'colorcolumnaenderecha','numerocolumnaenderecha')

        widgets = {
            'altocolumnaenderecha': forms.NumberInput(attrs={'class':'form-control'}),
            'colorcolumnaenderecha': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
            'numerocolumnaenderecha': forms.NumberInput(attrs={'class':'form-control'}),
        }

class Conf_21Form(forms.ModelForm):

    class Meta:
        model = Proyecto
        
        fields = ('altofilabume','altocolumnabumeizquierda', 'colorfilabume','colorcolumnabumeizquierda','numerocolumnabumeizquierda','bumeborde','bumeanchoborde','bumecolorborde')

        widgets = {
            'altofilabume': forms.NumberInput(attrs={'class':'form-control'}),
            'altocolumnabumeizquierda': forms.NumberInput(attrs={'class':'form-control'}),
            'colorfilabume': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
            'colorcolumnabumeizquierda': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
            'numerocolumnabumeizquierda': forms.NumberInput(attrs={'class':'form-control'}),
            'bume`colorborde': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
            'bumeanchoborde': forms.NumberInput(attrs={'class':'form-control'}),
            'bumeborde': forms.CheckboxInput(),
        }

class Conf_22Form(forms.ModelForm):

    class Meta:
        model = Proyecto
        
        fields = ('altocolumnabusqueda', 'colorcolumnabusqueda','numerocolumnabusqueda')

        widgets = {
            'altocolumnabusqueda': forms.NumberInput(attrs={'class':'form-control'}),
            'colorcolumnabusqueda': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
            'numerocolumnabusqueda': forms.NumberInput(attrs={'class':'form-control'}),
        }

class Conf_23Form(forms.ModelForm):

    class Meta:
        model = Proyecto
        
        fields = ('altocolumnamenu', 'colorcolumnamenu','numerocolumnamenu')

        widgets = {
            'altocolumnamenu': forms.NumberInput(attrs={'class':'form-control'}),
            'colorcolumnamenu': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
            'numerocolumnamenu': forms.NumberInput(attrs={'class':'form-control'}),
        }

class Conf_24Form(forms.ModelForm):

    class Meta:
        model = Proyecto
        
        fields = ('altocolumnabumederecha', 'colorcolumnabumederecha','numerocolumnabumederecha')

        widgets = {
            'altocolumnabumederecha': forms.NumberInput(attrs={'class':'form-control'}),
            'colorcolumnabumederecha': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
            'numerocolumnabumederecha': forms.NumberInput(attrs={'class':'form-control'}),
        }

class Conf_31Form(forms.ModelForm):

    class Meta:
        model = Proyecto
        
        fields = ('altofilamedio','altocolumnamedioizquierda', 'colorfilamedio','colorcolumnamedioizquierda','numerocolumnamedioizquierda','cenborde','cenanchoborde','cencolorborde')

        widgets = {
            'altofilamedio': forms.NumberInput(attrs={'class':'form-control'}),
            'altocolumnamedioizquierda': forms.NumberInput(attrs={'class':'form-control'}),
            'colorfilamedio': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
            'colorcolumnamedioizquierda': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
            'numerocolumnamedioizquierda': forms.NumberInput(attrs={'class':'form-control'}),
            'cencolorborde': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
            'cenanchoborde': forms.NumberInput(attrs={'class':'form-control'}),
            'cenborde': forms.CheckboxInput(),
        }

class Conf_32Form(forms.ModelForm):

    class Meta:
        model = Proyecto
        
        fields = ('altocolumnamediocentro', 'colorcolumnamediocentro','numerocolumnamediocentro')

        widgets = {
            'altocolumnamediocentro': forms.NumberInput(attrs={'class':'form-control'}),
            'colorcolumnamediocentro': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
            'numerocolumnamediocentro': forms.NumberInput(attrs={'class':'form-control'}),
        }

class Conf_33Form(forms.ModelForm):

    class Meta:
        model = Proyecto
        
        fields = ('altocolumnamedioderecha','colorcolumnamedioderecha','numerocolumnamedioderecha')

        widgets = {
            'altocolumnamedioderecha': forms.NumberInput(attrs={'class':'form-control'}),
            'colorcolumnamedioderecha': forms.TextInput(attrs={'class':'form-control', 'placeholder': ''}),
            'numerocolumnamedioderecha': forms.NumberInput(attrs={'class':'form-control'}),
        }

class WizzardForm(forms.Form):
    nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))