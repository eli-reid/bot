from django.db import models

class Command(models.Model):
    command = models.TextField(max_length=200)
    actionRequired = models.BooleanField(default=False) 
    builtIn = models.BooleanField(default=False)
    cooldown = models.TextField(max_length=200)
    data = models.TextField(max_length=200)
    roleRequired = models.TextField(max_length=200)