from django import forms
from paciente.models import Paciente


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', ]


class RelatorioForm(forms.Form):
    data_inicial = forms.DateTimeField()
    data_final = forms.DateTimeField()
