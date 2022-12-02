from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('inscricao', views.inscricao, name='inscricao'),
    path('inscricao/grupo', views.grupo, name='grupo'),

]
