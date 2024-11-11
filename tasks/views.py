from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from tasks.forms import TarefaForm
from tasks.models import Tarefas


def home(request):
    tarefas = Tarefas.objects.all().order_by('-ordem_apresentacao')
    return render(request,'home.html',context={'tarefas':tarefas})


def form_adicionar(request):
    form = TarefaForm(request.post)


    return render(request,'form-adicionar.html')