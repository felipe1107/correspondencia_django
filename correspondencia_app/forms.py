from django import forms
from .models import CorrespondenciaEntrada, Gestor

class EntradaForm(forms.ModelForm):
    class Meta:
        model = CorrespondenciaEntrada
        # ajusta los campos que necesites en el formulario de entrada
        fields = [
            'asunto',
            'gestor',
            'archivo_adjunto',
        ]

class GestorForm(forms.ModelForm):
    class Meta:
        model = Gestor
        # ajusta los campos que necesites en el formulario de gestor
        fields = [
            'nombre',
        ]
