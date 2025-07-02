from django import forms
from .models import CorrespondenciaSalida

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
            'observaciones',
        ]
