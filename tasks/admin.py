from django.contrib import admin

from tasks.models import Tarefa


# Register your models here.

class TarefaAdmin(admin.ModelAdmin):
    ...


admin.site.register(Tarefa, TarefaAdmin)
