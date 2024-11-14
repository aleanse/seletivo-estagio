from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse

from tasks.forms import TarefaForm
from tasks.models import Tarefas


def home(request):
    tarefas = Tarefas.objects.all().order_by('ordem_apresentacao')
    return render(request,'home.html',context={'tarefas':tarefas})


def form_adicionar(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Tarefa adicionada com sucesso')
            return redirect('home')
        else:
            return  render(request, 'form-tarefa.html', {'form': form})
    else:
        form = TarefaForm()
        return render(request, 'form-tarefa.html', context={'form':form})


def excluir(request,id):
    tarefa = Tarefas.objects.get(id=id)
    tarefa.delete()
    messages.success(request, 'Tarefa excluida com sucesso')

    return redirect('home')
