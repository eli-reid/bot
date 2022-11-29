from django.db import models
from random import randint

class Quotes(models.Model):
    created = models.DateField(auto_now_add=True)
    quote = models.TextField(max_length=200)