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

        copy = request.POST.copy()

        print('cheguei aqui')

        if "outro_tipos_atividade" in request.POST:
            try:
                outro_tipo = Tipo_Atividade.objects.create(
                    nome=request.POST['outro_tipos_atividade'])
            except:
                outro_tipo = Tipo_Atividade.objects.get(
                    nome=request.POST['outro_tipos_atividade'])

            print(copy['tipos_atividade'])

            if copy['tipos_atividade'] == "on" or not copy['tipos_atividade']:
                copy['tipos_atividade'] = outro_tipo
            else:
                copy.update(
                    {'tipos_atividade': [copy['tipos_atividade'], outro_tipo]})

        print('passei do tipos')
        if "outro_formato_atividade" in request.POST:
            try:
                outro_formato = Formato_Atividade.objects.create(
                    nome=request.POST['outro_formato_atividade'])
            except:
                outro_formato = Formato_Atividade.objects.get(
                    nome=request.POST['outro_formato_atividade'])

            copy['formato_atividade'] = outro_formato

        form_participante = Participante_form(copy)
        form_atividade = Atividade_form(copy)

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
