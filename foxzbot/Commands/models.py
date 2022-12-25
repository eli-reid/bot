from django.db import models

class Command(models.Model):
    command = models.TextField(max_length=200)
    cooldown = models.TextField(max_length=200)
    lastUsed = models.TimeField()
    data = models.TextField(max_length=200)
    roleRequired = models.TextField(max_length=200)
    usage = models.TextField()