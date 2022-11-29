from django.db import models

class User(models.Model):
    name = models.TextField()
    time_in_chat = models.TimeField()