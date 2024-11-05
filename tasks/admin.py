from django.contrib import admin

from tasks.models import Tarefas


# Register your models here.

class TarefasAdmin(admin.ModelAdmin):
    ...


admin.site.register(Tarefas, TarefasAdmin)
