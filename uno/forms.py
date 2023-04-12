from django import forms
from .models import MiModelo

class MiFormulario(forms.ModelForm):
    class Meta:
        model = MiModelo
        fields = ['campo1', 'campo2', 'campo3', 'campo4']