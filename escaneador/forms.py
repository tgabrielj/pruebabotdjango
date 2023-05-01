from django import forms
from .models import Escaneador

class EscaneadorForm(forms.ModelForm):
    class Meta:

        model = Escaneador
        fields = ['en_ejecucion', 'estrategia']
        widgets = {
            'en_ejecucion' : forms.CheckboxInput(attrs = {'class' : 'form-check-input m-auto'}),
            'estrategia' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder':'Write Title'})
            
        } 