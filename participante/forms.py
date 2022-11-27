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
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Recursos necessários para sua atividade"
    )

    titulo = forms.CharField(max_length=64 ,min_length=5, widget=forms.TextInput(
        attrs={'onkeydown': "mascara(this,icapitalize)", 'onload': 'mascara(this,icapitalize)'}))

    def clean_titulo(self):
        return self.cleaned_data['titulo'].capitalize()

        


class Participante_form(ModelForm):

    class Meta:
        model = Participante
        exclude = []

    celular = forms.CharField(label="Celular", max_length=15, widget=forms.TextInput(
        attrs={'onkeydown': "mascara(this,icelular)", 'onload': 'mascara(this,icelular)'}))

    matricula = forms.CharField(label="Número de Matricula", max_length=13, min_length=13, widget=forms.TextInput(
        attrs={'onkeydown': "mascara(this,iuppercase)", 'onload': 'mascara(this,iuppercase)'}))

    def clean_celular(self):
        telefone = self.cleaned_data["celular"]
        telefone = telefone.replace("(", '')
        telefone = telefone.replace(")", '')
        telefone = telefone.replace("-", '')
        telefone = telefone.replace(" ", '')
        if len(telefone) == 10:
            if telefone[2:3] != '2':
                raise ValidationError('Insira um número válido ')
        else:
            if len(telefone) != 11:
                raise ValidationError('Insira um número válido ')
        return telefone

    def clean_email(self):
        email = self.cleaned_data["email"]

        if email.find('@') == -1:
            raise ValidationError('Insira um e-mail válido')

        return email

    def clean_matricula(self):
        matricula = self.cleaned_data["matricula"].upper()

        if matricula.find('TINFNF') == -1 and matricula.find('TADMNF') == -1:
            raise ValidationError('Insira uma matrícula válida')

        if len(matricula) != 13:
            raise ValidationError('Insira uma matrícula válida')

        n_numbers = sum(c.isdigit() for c in matricula)
        if n_numbers != 7:
            raise ValidationError('Insira uma matrícula válida')

        return matricula
