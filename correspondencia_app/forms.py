from django import forms
from .models import Gestor, CorrespondenciaEntrada, CorrespondenciaSalida

class GestorForm(forms.ModelForm):
    class Meta:
        model = Gestor
        fields = ['nombre', 'correo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class EntradaForm(forms.ModelForm):
    class Meta:
        model = CorrespondenciaEntrada
        fields = ['asunto', 'gestor', 'fecha_recepcion', 'archivo_adjunto']
        widgets = {
            'asunto': forms.TextInput(attrs={'class': 'form-control'}),
            'gestor': forms.Select(attrs={'class': 'form-control'}),
            'fecha_recepcion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'archivo_adjunto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class SalidaForm(forms.ModelForm):
    class Meta:
        model = CorrespondenciaSalida
        fields = [
            'numero_documento', 'fecha_envio', 'remitente', 'destinatario',
            'asunto', 'departamento_origen', 'estado', 'archivo_adjunto', 'observaciones'
        ]
        widgets = {
            'numero_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_envio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'remitente': forms.TextInput(attrs={'class': 'form-control'}),
            'destinatario': forms.TextInput(attrs={'class': 'form-control'}),
            'asunto': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'departamento_origen': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'archivo_adjunto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
