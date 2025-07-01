from django import forms
from .models import CorrespondenciaEntrada, Gestor

class EntradaForm(forms.ModelForm):
    class Meta:
        model = CorrespondenciaEntrada
        exclude = [
            "numero_documento",
            "fecha_recepcion",
        ]
        widgets = {
            "asunto": forms.TextInput(attrs={"class": "form-control"}),
            "gestor": forms.Select(attrs={"class": "form-select"}),
            "archivo_adjunto": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

class DocumentManagerForm(forms.ModelForm):
    class Meta:
        model = Gestor
        fields = ["nombre"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
        }
