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
    reporter = models.ForeignKey(Reporter, models.CASCADE)

    def __str__(self):
        return self.title