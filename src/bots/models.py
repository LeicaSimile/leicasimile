from django.db import models

# Create your models here.
class Bot(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()

    def __str__(self):
        return self.name
        