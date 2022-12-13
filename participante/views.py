from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .forms import *
# import pyrebase

# config={
#     'apiKey': "AIzaSyCKx69jRAY9gvp9lKSy9jnrCi7ZGjr9Qyg",
#     'authDomain': "cefetalent.firebaseapp.com",
#     'databaseURL': "Use Your databaseURL Here",
#     'projectId': "cefetalent",
#     'storageBucket': "cefetalent.appspot.com",
#     'measurementId': "G-0SPV45T3R4",
#     'appId': "1:115169122453:web:c51731144592c1c510e39c",
#     'messagingSenderId': "115169122453",
# }
# firebase=pyrebase.initialize_app(config)
# authe = firebase.auth()
# database=firebase.database()

# Create your views here.


def index(request):

    return render(request, 'base/index.html')


def inscricao(request):

    form_atividade = Atividade_form()
    form_participante = Participante_form()

    if request.method == "POST":

        copy = request.POST.copy()
        participante = None

        if "outro_tipos_atividade" in request.POST:
            try:
                outro_tipo = Tipo_Atividade.objects.create(
                    nome=request.POST['outro_tipos_atividade'])
            except:
                outro_tipo = Tipo_Atividade.objects.get(
                    nome=request.POST['outro_tipos_atividade'])

            if "tipos_atividade" in copy and (request.POST['tipos_atividade'] == "on" or not request.POST['tipos_atividade']):
                copy['tipos_atividade'] = outro_tipo
            else:
                copy.update(
                    {'tipos_atividade': outro_tipo.id})  # type: ignore

        if not request.POST['formato_atividade'].isnumeric():
            try:
                outro_formato = Formato_Atividade.objects.create(
                    nome=request.POST['formato_atividade'])
            except:
                outro_formato = Formato_Atividade.objects.get(
                    nome=request.POST['formato_atividade'])

            copy['formato_atividade'] = outro_formato.id  # type: ignore

        try:
            participante = Participante.objects.get(
                email=request.POST['email'])

        except Exception as e:
            form_participante = Participante_form(request.POST)

        form_atividade = Atividade_form(copy)

        if participante:

            if form_atividade.is_valid():
                atividade = form_atividade.save()

                atividade.participantes.add(participante)
                atividade.save()

                messages.success(request, 'Inscrição realizada com sucesso!')

                return redirect('home')

        if form_atividade.is_valid():
            participante = form_participante.save()

            if form_atividade.is_valid() and form_participante.is_valid():
                atividade = form_atividade.save()

                atividade.participantes.add(participante)
                atividade.save()

                messages.success(request, 'Inscrição realizada com sucesso!')

                return redirect('home')

        form_participante = Participante_form(request.POST)

    context = {
        'form_atividade': form_atividade,
        'form_participante': form_participante
    }

    return render(request, 'cadastro/inscricao.html', context)


def grupo(request):

    form_participante = Integrante_form()

    if request.method == "POST":

        participante = None

        try:
            participante = Participante.objects.get(
                email=request.POST['email'])
            form_participante = Integrante_form(instance=participante)
        except Exception as e:
            form_participante = Integrante_form(request.POST)

        atividade = Atividade.objects.get(
            pk=request.POST['atividade'])  # type: ignore


        # O ideal seria usar atividade como uma guard clause. Porém, devido ao render estar no final
        # justamente para não acontecer de haver vários renders nessa função, não podemos utilizar a 
        # técnica de early return

        # Incrivelmmente, se o participante já estiver no atividades.partcipantes, não tem problema ser adicionado novamente
        
        if participante:
            atividade.participantes.add(participante)
            atividade.save()

            messages.success(request, 'Inscrição realizada com sucesso!')
            return redirect('home')

        if form_participante.is_valid():
            participante = form_participante.save()
            atividade.participantes.add(participante)
            atividade.save()

            messages.success(request, 'Inscrição realizada com sucesso!')
            return redirect('home')

        form_participante = Integrante_form(request.POST)

    context = {
        'form_participante': form_participante
    }

    return render(request, 'cadastro/grupo.html', context)
