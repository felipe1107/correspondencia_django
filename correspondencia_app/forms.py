# correspondencia_app/forms.py
from django import forms
from .models import CorrespondenciaEntrada, DocumentManager

class EntradaForm(forms.ModelForm):
    class Meta:
        model = CorrespondenciaEntrada
        # Pon aquí los campos que realmente tenga tu modelo:
        fields = [
            'numero_documento',
            'fecha_recepcion',
            'remitente',
            'destinatario',
            'departamento_destino',
            'asunto',
            'estado',
            'observaciones',
            # si tienes un campo de archivo, descomenta la siguiente línea:
            # 'archivo_adjunto',
        ]
        widgets = {
            'fecha_recepcion': forms.DateInput(attrs={'type': 'date'}),
        }

class DocumentManagerForm(forms.ModelForm):
    class Meta:
        model = DocumentManager
        fields = [
            'nombre',
            'email',
            'telefono',
            # añade aquí cualquier otro campo de tu modelo
        ]
