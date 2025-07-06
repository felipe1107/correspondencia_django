from django import forms
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor

class EntradaForm(forms.ModelForm):
    class Meta:
        model = CorrespondenciaEntrada
        fields = '__all__'

class SalidaForm(forms.ModelForm):
    class Meta:
        model = CorrespondenciaSalida
        fields = '__all__'

class GestorForm(forms.ModelForm):
    class Meta:
        model = Gestor
        fields = '__all__'
