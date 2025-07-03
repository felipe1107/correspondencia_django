# correspondencia_app/forms.py
from django import forms
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor

class CorrespondenciaEntradaForm(forms.ModelForm):
    class Meta:
        model = CorrespondenciaEntrada
        fields = [
            'numero_documento', 'remitente', 'destinatario', 'fecha_recepcion',
            'estado', 'archivo_adjunto', 'observaciones', 'departamento_destino',
            'gestor'
        ]

class CorrespondenciaSalidaForm(forms.ModelForm):
    class Meta:
        model = CorrespondenciaSalida
        fields = [
            'numero_documento', 'destinatario', 'fecha_envio',
            'estado', 'archivo_adjunto', 'observaciones', 'departamento_origen',
            'gestor'
        ]

class GestorForm(forms.ModelForm):
    class Meta:
        model = Gestor
        fields = ['nombre', 'telefono', 'correo']
