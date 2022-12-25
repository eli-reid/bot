from django.db import models

class Settings(models.Model):
    timestamp = models.DateTimeField(auto_created=True)
    access_token = models.TextField(max_length=100)
    expires = models.BigIntegerField()
    refresh_token = models.TextField(max_length=200)
    scope = models.TextField(max_length=200)
    token_type = models.TextField(max_length=50)
