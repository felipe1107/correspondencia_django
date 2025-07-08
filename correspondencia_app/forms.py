from django import forms
from .models import EntradaCorrespondencia, SalidaCorrespondencia, Gestor

class EntradaForm(forms.ModelForm):
    class Meta:
        model = EntradaCorrespondencia
        fields = '__all__'

class SalidaForm(forms.ModelForm):
    class Meta:
        model = SalidaCorrespondencia
        fields = '__all__'

class GestorForm(forms.ModelForm):
    class Meta:
        model = Gestor
        fields = '__all__'
