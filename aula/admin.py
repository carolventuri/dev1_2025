from django.contrib import admin
from .models import Passport, Person, Reporter, Article, Magazine

admin.site.register ((Passport, Person, Reporter, Article, Magazine))

# Register your models here.
