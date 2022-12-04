from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Prefetch
from .forms import *
from participante.models import Participante, Atividade, Formato_Atividade
# Create your views here.

@login_required
def adm_painel(request):
    return render(request, 'adm_painel.html')

@login_required
def adm_recursos_listar(request):
    recursos= Recurso.objects.all()
    context = {
        'recursos':recursos
    }
    return render(request, 'adm_recursos_listar.html', context)

@login_required
def adm_editar_recurso(request, id):
    recurso= Recurso.objects.get(id=id)
    form_recurso=Recurso_form(instance=recurso)
    print(form_recurso)
    if request.method=='POST':
        form_recurso=Recurso_form(request.POST, instance=recurso)
        if form_recurso.is_valid():
            form_recurso.save()
            messages.success(request, 'Dados atualizados com sucesso!')
            return redirect('organizacao:Recursos')
    context={
        'form_recurso':form_recurso,
        'recurso':recurso,
    }
    return render(request, 'adm_recurso_editar.html', context)

@login_required
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
            return redirect('organizacao:Recursos')
    return render(request, 'adm_recursos_cad.html', context)

@login_required
def adm_participantes_listar(request):
    participantes=Participante.objects.all()
    context = {
        'participantes': participantes
    }
    return render(request, 'adm_participantes_listar.html', context)

@login_required
def adm_atividades_listar(request):
    queryset=Atividade.objects.all()
    context = {'atividades': queryset}
    return render(request, 'adm_atividades_listar.html', context)

@login_required
def adm_atividade_detalhes(request, id):
    atividade=Atividade.objects.get(id=id)
    print(atividade)
    context = {
        'atividade':atividade,
    }
    return render (request, 'adm_atividade_detalhes.html', context)