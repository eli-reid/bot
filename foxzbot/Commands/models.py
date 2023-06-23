from typing import Any
from django.db import models

class Command(models.Model):
    command = models.TextField(max_length=200)
    cooldown = models.IntegerField(default=0)
    lastUsed = models.DateTimeField(auto_now=True)
    data = models.TextField(max_length=200)
    roleRequired = models.TextField(max_length=200)
    usage = models.TextField(max_length=200)