from django.urls import path
from django.contrib import admin
from app_cad_usuario import views

urlpatterns=[
    #rota, view responsável, nome de referência
    #usuario.com
    path('', views.home, name='home'),
    #usuario.com/usuarios
    path('usuarios/', views.usuarios, name='listagem_usuarios')
]