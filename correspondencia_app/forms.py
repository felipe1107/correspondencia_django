from django import forms
from .models import CorrespondenciaEntrada, DocumentManager

class EntradaForm(forms.ModelForm):
    class Meta:
        model  = CorrespondenciaEntrada
        fields = [
            'numero_documento',
            'fecha_recepcion',
            'remitente',
            'destinatario',
            'asunto',
            'departamento_destino',
            'estado',
            'gestor',            # nuevo campo
            'archivo_adjunto',
            'observaciones',
        ]

class DocumentManagerForm(forms.ModelForm):
    class Meta:
        model  = DocumentManager
        fields = ['nombre', 'email', 'telefono', 'archivo']