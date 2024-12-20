from django.db import models

# Create your models here.

class Tarefa(models.Model):
    nome = models.CharField(unique=True,max_length=255,null=False)
    custo = models.DecimalField(max_digits=10,decimal_places=2,null=False)
    data_limite = models.DateField()
    ordem_apresentacao = models.IntegerField(unique=True,null=True, blank=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if self.ordem_apresentacao is None:

            super().save(*args, **kwargs)
            self.ordem_apresentacao = self.id
        super().save(*args, **kwargs)

