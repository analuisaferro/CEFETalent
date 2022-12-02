from django.urls import path
from . import views

urlpatterns = [
    path('paineladmin/', views.adm_painel, name="Painel de administração"),
    # RECURSOS
    path('paineladmin/recursos', views.adm_recursos_listar, name="Recursos"),
    path('paineladmin/cadastrar-recurso', views.adm_cad_recurso, name='Cadastrar recurso'),

    # PARTICIPANTES - APRESENTAÇÃO
    path('paineladmin/participantes', views.adm_participantes_listar, name="Participantes"),
    path('paineladmin/apresentacoes', views.adm_apresentacoes_listar, name="Apresentações"),

]
