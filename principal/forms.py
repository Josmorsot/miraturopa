from django import forms
from principal.models import *

class DirectorForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput, label="Nombre")
    apellidos = forms.CharField(widget=forms.TextInput, label="Apellidos")
    
class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario