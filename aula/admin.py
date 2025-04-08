from django.contrib import admin
from .models import Passport, Person, Reporter, Article, Magazine, Publication

admin.site.register ((Passport, Person, Reporter, Article, Magazine, Publication))

# Register your models here.
