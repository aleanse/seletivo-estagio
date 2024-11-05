from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from tasks.models import Tarefas


def home(request):
    tarefas = Tarefas.objects.all().order_by('-ordem_apresentacao')

    return render(request,'home.html',context={'tarefas':tarefas})
