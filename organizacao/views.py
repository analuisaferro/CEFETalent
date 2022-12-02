from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *

# Create your views here.

def adm_painel(request):
    return render(request, 'adm_painel.html')

def adm_recursos_listar(request):
    recursos= Recurso.objects.all()
    context = {
        'recursos':recursos
    }
    return render(request, 'adm_recursos_listar.html', context)

def adm_cad_recurso(request):
    form_recursos = Recurso_form()
    context = {
    'form_recursos': form_recursos,
    }
    if request.method == "POST":
        form = Recurso_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recurso cadastrado!')
            return redirect('Recursos')
    return render(request, 'adm_recursos_cad.html', context)

