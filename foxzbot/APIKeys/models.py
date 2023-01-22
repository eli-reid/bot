from django.db import models

class APIKeys(models.Model):
    app = models.TextField(max_length=10)
    key = models.TextField(max_length=50)

    class Meta:
        unique_together = ('app', 'key')

    def __str__(self):
        return f"{self.app}.{self.key}"

    def key_gen(self) -> str:
        return