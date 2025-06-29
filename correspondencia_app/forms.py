from django import forms
from .models import CorrespondenciaEntrada, DocumentManager

class EntradaForm(forms.ModelForm):
    class Meta:
        model  = CorrespondenciaEntrada
        fields = [
            # 'numero_documento' y 'fecha_recepcion' no aparecen aquí
            'remitente',
            'destinatario',
            'asunto',
            'departamento_destino',
            'estado',
            'gestor',
            'archivo_adjunto',
            'observaciones',
        ]
        widgets = {
            'remitente': forms.TextInput(attrs={'class': 'form-control'}),
            'destinatario': forms.TextInput(attrs={'class': 'form-control'}),
            'asunto': forms.TextInput(attrs={'class': 'form-control'}),
            'departamento_destino': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'gestor': forms.Select(attrs={'class': 'form-select'}),
            'archivo_adjunto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class DocumentManagerForm(forms.ModelForm):
    class Meta:
        model  = DocumentManager
        fields = ['nombre', 'email', 'telefono', 'archivo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'archivo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
