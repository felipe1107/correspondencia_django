from django import forms
from .models import EntradaCorrespondencia, SalidaCorrespondencia, Gestor

class EntradaForm(forms.ModelForm):
    class Meta:
        model = EntradaCorrespondencia
        exclude = ['numero_documento', 'fecha_recepcion']

    def clean(self):
        cleaned_data = super().clean()
        campos_obligatorios = ['remitente', 'destinatario', 'asunto', 'departamento_destino', 'estado']
        for campo in campos_obligatorios:
            if not cleaned_data.get(campo):
                self.add_error(campo, "Este campo no puede estar vacío.")


class SalidaForm(forms.ModelForm):
    class Meta:
        model = SalidaCorrespondencia
        exclude = ['numero_documento', 'fecha_envio']

    def clean(self):
        cleaned_data = super().clean()
        campos_obligatorios = ['remitente', 'destinatario', 'asunto', 'departamento_origen', 'estado']
        for campo in campos_obligatorios:
            if not cleaned_data.get(campo):
                self.add_error(campo, "Este campo no puede estar vacío.")


class GestorForm(forms.ModelForm):
    class Meta:
        model = Gestor
        fields = ['nombre', 'correo', 'telefono', 'departamento', 'cargo']

    def clean(self):
        cleaned_data = super().clean()
        campos_obligatorios = ['nombre', 'correo', 'telefono', 'departamento', 'cargo']
        for campo in campos_obligatorios:
            if not cleaned_data.get(campo):
                self.add_error(campo, "Este campo es obligatorio.")
