from django.db import models

class StreamTimer(models.Model):
    endtime = models.TimeField()
    colorWheel = models.IntegerField()
    
