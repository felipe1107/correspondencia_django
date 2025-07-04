from django import forms
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CorrespondenciaEntradaForm(forms.ModelForm):
    class Meta:
        model = CorrespondenciaEntrada
        fields = '__all__'

class CorrespondenciaSalidaForm(forms.ModelForm):
    class Meta:
        model = CorrespondenciaSalida
        fields = '__all__'

class GestorForm(forms.ModelForm):
    class Meta:
        model = Gestor
        fields = '__all__'

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
