# correspondencia_app/forms.py

from django import forms
from .models import Gestor, CorrespondenciaEntrada, CorrespondenciaSalida

class GestorForm(forms.ModelForm):
    class Meta:
        model = Gestor
        fields = ['nombre', 'correo']

class CorrespondenciaEntradaForm(forms.ModelForm):
    class Meta:
        model = CorrespondenciaEntrada
        fields = ['asunto', 'gestor', 'fecha_recepcion', 'archivo_adjunto']

class CorrespondenciaSalidaForm(forms.ModelForm):
    class Meta:
        model = CorrespondenciaSalida
        fields = [
            'numero_documento',
            'fecha_envio',
            'remitente',
            'destinatario',
            'asunto',
            'departamento_origen',
            'estado',
            'archivo_adjunto',
            'observaciones'
        ]
