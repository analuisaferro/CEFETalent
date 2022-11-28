from django.shortcuts import render
from .forms import *

# Create your views here.

def paineladmin(request):
    return render(request, 'adm_painel.html')

def adm_recursos(request):
    form_recursos = Recurso_form()
    context = {
        'form_recursos':form_recursos,
    }
    return render(request, 'adm_recursos.html')

