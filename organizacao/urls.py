from django.urls import path
from . import views

urlpatterns = [
    path('painel/', views.adm_painel, name="Painel"),

    # RECURSOS
    path('painel/recursos', views.adm_recursos_listar, name="Recursos"),
    path('painel/cadastrar-recurso', views.adm_cad_recurso, name='Cadastrar recurso'),

    # PARTICIPANTES - Atividades
    path('painel/participantes', views.adm_participantes_listar, name="Participantes"),
    path('painel/atividades', views.adm_atividades_listar, name="Atividades"),

]
