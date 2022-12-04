from django.urls import path
from . import views

urlpatterns = [
    path('painel/', views.adm_painel, name="Painel"),

    # RECURSOS
    path('painel/recursos', views.adm_recursos_listar, name="Recursos"),
    path('painel/cadastrar-recurso', views.adm_cad_recurso, name='Cadastrar recurso'),
    path('painel/recursos/editar/<id>', views.adm_editar_recurso, name='Editar recurso'),
    path('painel/recursos/excluir/<id>', views.adm_excluir_recurso, name='Excluir recurso'),



    # PARTICIPANTES
    path('painel/participantes', views.adm_participantes_listar, name="Participantes"),

    #ATIVIDADES
    path('painel/atividades', views.adm_atividades_listar, name="Atividades"),
    path('painel/atividades/<id>', views.adm_atividade_detalhes, name="Atividade detalhes"),


]
