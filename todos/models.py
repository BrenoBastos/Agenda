from django.db import models
from datetime import date
from django.core.exceptions import ValidationError

class Todo(models.Model):
    title = models.CharField(verbose_name="Título",max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(verbose_name="Data de Entrega",null=False, blank=False)
 
    finished_at = models.DateField(null=True)

    class Meta:
        ordering = ["deadline"]
    def clean(self):
        super().clean()
        # Verifique se 'created_at' já foi definido
        if self.created_at and self.deadline and self.deadline > self.created_at.date():
            raise ValidationError('A data de entrega não pode ser posterior à data de início.')
