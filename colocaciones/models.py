from django.db import models
from django.utils import timezone
# Create your models here.

class Agencia(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
            return self.title

