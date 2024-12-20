from django import forms

from tasks.models import Tarefa


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome', 'custo', 'data_limite']
        widgets = {'nome': forms.TextInput(attrs={'class': 'span-2'}),
                   'custo': forms.NumberInput(attrs={'class': 'span-2'}),
                   'data_limite': forms.DateInput(attrs={'class': 'span-2','type': 'date'}),
                   }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if Tarefa.objects.filter(nome=nome).exists():
            raise forms.ValidationError("já existe uma tarefa com esse nome")

        else:
            return nome


