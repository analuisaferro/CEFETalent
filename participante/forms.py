from django import forms
from django.forms import ModelChoiceField, ModelForm, ModelMultipleChoiceField, ValidationError
from .models import *


class MultipleChoiceAnyField(ModelMultipleChoiceField):
    """A MultipleChoiceField with no validation."""

    def _check_values(self, value):
        """
        Given a list of possible PK values, return a QuerySet of the
        corresponding objects. Raise a ValidationError if a given value is
        invalid (not a valid PK, not in the queryset, etc.)
        """
        key = self.to_field_name or 'pk'
        # deduplicate given values to avoid creating many querysets or
        # requiring the database backend deduplicate efficiently.
        try:
            value.remove('on')
        except:
            pass

        try:
            value = frozenset(value)
        except TypeError:
            # list of lists isn't hashable, for example
            raise ValidationError(
                self.error_messages['invalid_list'],
                code='invalid_list',
            )
        for pk in value:
            try:
                self.queryset.filter(**{key: pk})
            except (ValueError, TypeError):
                raise ValidationError(
                    self.error_messages['invalid_pk_value'],
                    code='invalid_pk_value',
                    params={'pk': pk},
                )
        qs = self.queryset.filter(**{'%s__in' % key: value})

        pks = {str(getattr(o, key)) for o in qs}
        for val in value:
            if str(val) not in pks:
                raise ValidationError(
                    self.error_messages['invalid_choice'],
                    code='invalid_choice',
                    params={'value': val},
                )

        return qs


class ChoiceAnyField(ModelChoiceField):
    """A MultipleChoiceField with no validation."""

    def to_python(self, value):
        if value in self.empty_values:
            return None

        try:
            key = self.to_field_name or 'pk'

            if isinstance(value, self.queryset.model):
                value = getattr(value, key)
            value = self.queryset.get(**{key: value})
        except (ValueError, TypeError, self.queryset.model.DoesNotExist):
            raise ValidationError(
                self.error_messages['invalid_choice'], code='invalid_choice')
        return value


class Atividade_form(ModelForm):

    class Meta:
        model = Atividade
        fields = ['titulo', 'descricao', 'duracao',
                  'tipos_atividade', 'formato_atividade', 'recursos']

    tipos_atividade = MultipleChoiceAnyField(
        queryset=Tipo_Atividade.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    formato_atividade = ChoiceAnyField(
        queryset=Formato_Atividade.objects.all(),
        widget=forms.RadioSelect
    )

    recursos = forms.ModelMultipleChoiceField(
        queryset=Recurso.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Recursos necessários para sua atividade"
    )

    titulo = forms.CharField(max_length=64, min_length=5, widget=forms.TextInput(
        attrs={'onkeydown': "mascara(this,icapitalize)", 'onload': 'mascara(this,icapitalize)'}))

    def clean_titulo(self):
        return self.cleaned_data['titulo'].capitalize()

    def clean_formato_atividade(self):
        formato_atividade = self.cleaned_data['formato_atividade']

        try: 
            if not formato_atividade.nome.isnumeric():
                formato_atividade.nome = formato_atividade.nome.capitalize()
        except Exception as e:
            pass 
        return formato_atividade

    def clean_outro_tipos_atividade(self):
        return self.cleaned_data['outro_tipos_atividade'].capitalize()


class Participante_form(ModelForm):

    class Meta:
        model = Participante
        exclude = []

    celular = forms.CharField(label="Celular", max_length=15, widget=forms.TextInput(
        attrs={'onkeydown': "mascara(this,icelular)", 'onload': 'mascara(this,icelular)'}))

    # matricula = forms.CharField(label="Número de Matricula", max_length=13, min_length=13, widget=forms.TextInput(
    #     attrs={'onkeydown': "mascara(this,iuppercase)", 'onload': 'mascara(this,iuppercase)'}))

    def clean_celular(self):
        telefone = self.cleaned_data["celular"]
        telefone = telefone.replace("(", '')
        telefone = telefone.replace(")", '')
        telefone = telefone.replace("-", '')
        telefone = telefone.replace(" ", '')
        if len(telefone) == 10:
            if telefone[2:3] != '2':
                raise ValidationError('Insira um número de celular válido ')
        else:
            if len(telefone) != 11:
                raise ValidationError('Insira um número de celular válido ')
        return telefone

    def clean_email(self):
        email = self.cleaned_data["email"]

        if email.find('@') == -1:
            raise ValidationError('Insira um e-mail válido')

        return email.lower()

    # def clean_matricula(self):
    #     matricula = self.cleaned_data["matricula"].upper()

    #     if matricula.find('TINFNF') == -1 and matricula.find('TADMNF') == -1:
    #         raise ValidationError('Insira uma matrícula válida')

    #     if len(matricula) != 13:
    #         raise ValidationError('Insira uma matrícula válida')

    #     n_numbers = sum(c.isdigit() for c in matricula)
    #     if n_numbers != 7:
    #         raise ValidationError('Insira uma matrícula válida')

    #     return matricula

class Integrante_form(Participante_form):
    atividade = forms.ModelChoiceField(
        queryset=Atividade.objects.all(),
        widget=forms.RadioSelect,
        label="Atividade em que você é integrante"
    )

    # def clean_nome(self):
    #     print('cade minha validacao')
    #     nome = self.cleaned_data['nome']

    #     participante = None
    #     try:
    #         participante = Participante.objects.get(
    #             email=self.cleaned_data['email'])
    #     except Exception as e:
    #         pass

    
    #     atividade = Atividade.objects.get(
    #         pk=self.cleaned_data['atividade'])  

    #     print(atividade)
    #     print(participante)

    #     if atividade.participantes.filter(pk=participante.pk).exists(): # type: ignore

    #         raise ValidationError({"atividade":"Você já está cadastrado nessa atividade"})

    #     return nome