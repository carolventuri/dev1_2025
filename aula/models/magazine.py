from .base_model import BaseModel
from django.db import models
from ..models import Article

class Magazine(BaseModel):
    name = models.CharField(
        max_length=100, null=False, blank=False,
        help_text="Escreva aqui o nome da Maagazine.",
        verbose_name="Nome:",
    )
    edition = models.IntegerField(
        null=False, blank=False,
        help_text="Escreva aqui o número da edição",
        verbose_name="Edição:",
    )

    article = models.ManyToManyField(Article)

    def __str__(self):
        return self.name