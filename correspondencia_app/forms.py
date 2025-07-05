from django import forms
from .models import Entrada, Salida, Gestor, Usuario


class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
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


class SalidaForm(forms.ModelForm):
    class Meta:
        model = Salida
        fields = [
            'numero_documento',
            'fecha_envio',
            'remitente',
            'destinatario',
            'asunto',
            'departamento_origen',
            'estado',
            'archivo_adjunto',
            'observaciones',
        ]
