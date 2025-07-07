from django import forms
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor

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
