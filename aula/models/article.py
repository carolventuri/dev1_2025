from aula.models.magazine import Magazine
from .base_model import BaseModel
from django.db import models
from .reporter import Reporter

class Article(BaseModel):
    title = models.CharField(
        max_length=100, null=False, blank=False,
        help_text="Escreva aqui o título do Artigo.",
        verbose_name="Nome:",
    )
    pub_date = models.DateField(
        null=False, blank=False,
        help_text="Escreva aqui a data de publicação",
        verbose_name="Data publicação:",
    )
    reporter = models.ForeignKey(Reporter, models.RESTRICT)
    magazines = models.ManyToManyField(
        Magazine, null=True, blank=True, through="Publication", through_fields=("article", "reporter")
    )
    

    def __str__(self):
        return f"{self.title} by {self.reporter.name if self.reporter is not None else 'Anonimo' }