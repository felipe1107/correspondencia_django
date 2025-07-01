from django import forms
from .models import CorrespondenciaEntrada, DocumentManager

class EntradaForm(forms.ModelForm):
    class Meta:
        model = CorrespondenciaEntrada
        fields = [
            'asunto',
            'remitente',
            'destinatario',
            'estado',
            'gestor',
            'archivo_adjunto',
        ]

class DocumentManagerForm(forms.ModelForm):
    class Meta:
        model = DocumentManager
        fields = [
            'nombre',
            'email',
            'telefono',
        ]
