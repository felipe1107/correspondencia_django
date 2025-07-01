from django import forms
from .models import CorrespondenciaEntrada, DocumentManager

class EntradaForm(forms.ModelForm):
    class Meta:
        model = CorrespondenciaEntrada
        # Excluimos los dos campos que se generan automáticamente
        exclude = ('numero_documento', 'fecha_recepcion')
        widgets = {
            'asunto': forms.TextInput(attrs={'class': 'form-control'}),
            'remitente': forms.TextInput(attrs={'class': 'form-control'}),
            'destinatario': forms.TextInput(attrs={'class': 'form-control'}),
            'gestor': forms.Select(attrs={'class': 'form-select'}),
            'archivo_adjunto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }

class DocumentManagerForm(forms.ModelForm):
    class Meta:
        model = DocumentManager
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            # ajusta según tus campos...
        }
