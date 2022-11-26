from django import forms
from django.forms import ModelForm, ValidationError
from .models import *


class Atividade_form(ModelForm):

    class Meta:
        model = Atividade
        fields = ['titulo', 'descricao', 'duracao',
                       'tipos_atividade', 'formato_atividade', 'recursos']

    tipos_atividade = forms.ModelMultipleChoiceField(
        queryset=Tipo_Atividade.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    formato_atividade = forms.ModelChoiceField(
        queryset=Formato_Atividade.objects.all(),
        widget=forms.RadioSelect
    )

    recursos = forms.ModelMultipleChoiceField(
        queryset=Recurso.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


class Participante_form(ModelForm):

    class Meta:
        model = Participante
        exclude = []
