from django.db import models
from aula.models import Article, Magazine, Person
from .base_model import BaseModel


class Publication (BaseModel):
    article = models.ForeignKey(Article, on_delete=models.RESTRICT)
    magazine = models.ForeignKey(Magazine, on_delete=models.RESTRICT)
    editor = models.ForeignKey (Person, on_delete=models.RESTRICT)
    date = models.DateField()
    obs = models.TextField()