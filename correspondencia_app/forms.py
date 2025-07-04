from django import forms
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor

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
            'observaciones'
        ]
        widgets = {
            'fecha_recepcion': forms.DateInput(attrs={'type': 'date'}),
            'estado': forms.Select(choices=[
                ('pendiente', 'Pendiente'),
                ('procesado', 'Procesado'),
                ('finalizado', 'Finalizado'),
            ])
        }

class CorrespondenciaSalidaForm(forms.ModelForm):
    class Meta:
        model = CorrespondenciaSalida
        fields = [
            'numero_documento',
            'fecha_recepcion',
            'remitente',
            'destinatario',
            'asunto',
            'departamento_origen',
            'estado',
            'archivo_adjunto',
            'observaciones'
        ]
        widgets = {
            'fecha_recepcion': forms.DateInput(attrs={'type': 'date'}),
            'estado': forms.Select(choices=[
                ('pendiente', 'Pendiente'),
                ('procesado', 'Procesado'),
                ('finalizado', 'Finalizado'),
            ])
        }

class GestorForm(forms.ModelForm):
    class Meta:
        model = Gestor
        fields = ['nombre', 'correo']
