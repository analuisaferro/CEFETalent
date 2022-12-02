from django.urls import path
from . import views

urlpatterns = [
    path('paineladmin/', views.adm_painel, name="Painel de administração"),
    path('paineladmin/recursos', views.adm_recursos_listar, name="Recursos"),
    path('paineladmin/cadastrar-recurso', views.adm_cad_recurso, name='Cadastrar recurso')
]
