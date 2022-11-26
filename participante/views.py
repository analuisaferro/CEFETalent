from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .forms import *

# Create your views here.


def index(request):
    return render(request, 'base/index.html')


def inscricao(request):

    form_atividade = Atividade_form()
    form_participante = Participante_form()

    if request.method == "POST":
        form_participante = Participante_form(request.POST)
        form_atividade = Atividade_form(request.POST)

        if form_atividade.is_valid() and form_participante.is_valid():
            atividade = form_atividade.save()
            participante = form_participante.save()

            atividade.participantes.add(participante)
            atividade.save()
            
            messages.success(request, 'Inscrição finalizada com sucesso!')

            return redirect('home')

    context = {
        'form_atividade': form_atividade,
        'form_participante': form_participante
    }

    return render(request, 'cadastro/inscricao.html', context)
