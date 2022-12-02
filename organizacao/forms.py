from django import forms
from django.forms import ModelChoiceField, ModelForm, ModelMultipleChoiceField, ValidationError
from .models import *

class Recurso_form(ModelForm):
    class Meta:
        model = Recurso
        exclude = []