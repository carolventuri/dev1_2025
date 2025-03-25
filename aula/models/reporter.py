from .base_model import BaseModel
from django.db import models

class Reporter(BaseModel):
    name = models.CharField(
        max_length=100, null=False, blank=False,
        help_text="Escreva aqui o nome do reporter.",
        verbose_name="Nome:",
    )
    email = models.EmailField(
        max_length=100, null=False, blank=False,
        help_text="Escreva aqui o email.",
        verbose_name="Email:",
    )
    cpf = models.CharField(
        max_length=11, null=False, blank=False,
        help_text="Escreva aqui o CPF.",
        verbose_name="CPF:",
    )


    def __str__(self):
        return self.name
