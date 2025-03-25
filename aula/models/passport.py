from .base_model import BaseModel
from django.db import models
from .person import Person


class Passport(BaseModel):
    number = models.CharField(
        max_length=20, null=False, blank=False,
        help_text="Escreva aqui o numero do passaporte",
        verbose_name="Numero:",
    )
    issue_date = models.DateField(
        null=False, blank=False,
        help_text="Escreva aqui a data do passaporte",
        verbose_name="Issue date:",
    )
    expiration_date = models.DateField(
        null=False, blank=False,
        help_text="Escreva aqui a data de expiração passaporte",
        verbose_name="Expiration date:",
    )
    owner = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"Número: {self.number} Issue date: {self.issue_date} Expiration Date: {self.expiration_date}"
