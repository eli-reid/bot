from django.db import models


class Roles(models.Model):
    role = models.TextField(max_length=20)
    shortHand = models.TextField(max_length=4)
    
class User(models.Model):
    CHOICE: list = []
    name = models.TextField(max_length=20)
    room = models.TextField(max_length=30)

    for role in Roles.objects.all():
        CHOICE.append((role.pk, role.role))

    role = models.TextField(choices=CHOICE, default='d')
