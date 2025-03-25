from .base_model import BaseModel
from django.db import models

class Person(BaseModel):

    name = models.CharField(
        max_length=100, null=False, blank=False,
        help_text="Escreva aqui o nome da pessoa.",
        verbose_name="Nome:",
    )
    birth_date = models.DateField(
        null=False, blank=False,
        help_text="Escreva aqui a data de nascimento.",
        verbose_name="Data de Nascimento:",
    )
    cpf = models.CharField(
        max_length=11, null=False, blank=False,
        help_text="Escreva aqui o CPF.",
        verbose_name="CPF:",
    )

    def __str__(self):
        return f"Name:{self.name} Birth Date: {self.birth_date} CPF: {self.cpf}"
