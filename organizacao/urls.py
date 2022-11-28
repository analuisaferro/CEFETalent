from django.urls import path
from . import views

urlpatterns = [
    path('paineladmin/', views.paineladmin, name="Painel de administração"),
    path('paineladmin/recursos', views.adm_recursos, name="Recursos")

]
