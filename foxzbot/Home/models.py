from django.db import models

class Settings(models.Model):
    app = models.TextField(max_length=20)
    key = models.TextField(max_length=50)
    value = models.TextField(max_length=50)
    readOnly = models.BooleanField(default=False)
    visible = models.BooleanField(default=False)
    class Meta:
        unique_together = ('app', 'key')

    def __str__(self):
        return f"{self.app}.{self.key}"