from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Prefetch
from .forms import *
from participante.models import Participante, Atividade, Formato_Atividade
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

def adm_participantes_listar(request):
    participantes=Participante.objects.all()
    context = {
        'participantes': participantes
    }
    return render(request, 'adm_participantes_listar.html', context)

def adm_apresentacoes_listar(request):
    queryset=Atividade.objects.prefetch_related('participantes').all()
    atividades = []
    for atv in queryset:
        atividades.append({
        'titulo': atv.titulo,
        'descricao': atv.descricao,
        # 'formato': atv.formato_atividade.nome,
        'duracao': atv.duracao,
        'participantes': atv.participantes})
    print(atividades)
    context = {}
    return render(request, 'adm_apresentacoes_listar.html', context)
