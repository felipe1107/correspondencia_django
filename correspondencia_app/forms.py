from django import forms
from .models import CorrespondenciaEntrada, DocumentManager

class EntradaForm(forms.ModelForm):
    class Meta:
        model = CorrespondenciaEntrada
        fields = [
            'numero_documento', 'remitente', 'destinatario',
            'departamento_destino', 'asunto', 'estado',
            'fecha_recepcion', 'observaciones'
        ]

class DocumentManagerForm(forms.ModelForm):
    class Meta:
        model = DocumentManager
        fields = ['nombre', 'email', 'telefono']
