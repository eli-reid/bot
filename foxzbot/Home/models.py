from django.db import models

class Settings(models.Model):
    app = models.CharField(max_length=20)
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=100, blank=True)
    readOnly = models.BooleanField(default=False)
    visible = models.BooleanField(default=False)
    inputType = models.CharField(max_length=20)
    class Meta:
        unique_together = ('app', 'key')

    def __str__(self):
        return f"{self.app}.{self.key}"