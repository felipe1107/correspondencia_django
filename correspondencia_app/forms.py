from django import forms
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor

class CorrespondenciaEntradaForm(forms.ModelForm):
    class Meta:
        model = CorrespondenciaEntrada
        fields = [
            'numero_documento',
            'fecha_recepcion',
            'remitente',
            'destinatario',
            'asunto',
            'departamento_destino',
            'estado',
            'archivo_adjunto',
            'observaciones',
        ]

class CorrespondenciaSalidaForm(forms.ModelForm):
    class Meta:
        model = CorrespondenciaSalida
        fields = [
            'numero_documento',
            'fecha_envio',
            'destinatario',
            'asunto',
            'departamento_destino',
            'estado',
            'archivo_adjunto',
            'observaciones',
        ]

class GestorForm(forms.ModelForm):
    class Meta:
        model = Gestor
        fields = ['nombre']
