from django.urls import path
from django.contrib import admin

from tasks import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adicionar/', views.form_adicionar, name='form_adicionar'),
    path('excluir/<int:id>/', views.excluir, name='excluir'),
    path('editar_tarefa/<int:id>/',views.editar_tarefa, name='editar')
]
