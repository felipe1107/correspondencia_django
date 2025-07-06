from django import forms
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor

class EntradaForm(forms.ModelForm):
    class Meta:
        model = CorrespondenciaEntrada
        fields = '__all__'
        widgets = {
            'fecha_recepcion': forms.DateInput(attrs={'type': 'date'}),
        }

class SalidaForm(forms.ModelForm):
    class Meta:
        model = CorrespondenciaSalida
        fields = '__all__'
        widgets = {
            'fecha_envio': forms.DateInput(attrs={'type': 'date'}),
        }

class GestorForm(forms.ModelForm):
    class Meta:
        model = Gestor
        fields = '__all__'
