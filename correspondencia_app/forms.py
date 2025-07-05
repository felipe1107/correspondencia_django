from django import forms
from .models import CorrespondenciaEntrada

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
        widgets = {
            'fecha_recepcion': forms.DateInput(attrs={'type': 'date'}),
            'observaciones': forms.Textarea(attrs={'rows': 3}),
        }
