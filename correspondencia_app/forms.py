# correspondencia_app/forms.py
from django import forms
from .models import CorrespondenciaEntrada, CorrespondenciaSalida

class EntradaForm(forms.ModelForm):
    class Meta:
        model = CorrespondenciaEntrada
        fields = '__all__'

class SalidaForm(forms.ModelForm):
    class Meta:
        model = CorrespondenciaSalida
        fields = '__all__'
