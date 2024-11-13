from django import forms

from tasks.models import Tarefas


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefas
        fields = ['nome', 'custo', 'data_limite']
        widgets = {'nome': forms.TextInput(attrs={'class': 'span-2'}),
                   'custo': forms.NumberInput(attrs={'class': 'span-2'}),
                   'data_limite': forms.DateInput(attrs={'class': 'span-2','type': 'date'}),
                   }
