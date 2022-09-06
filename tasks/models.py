from email.policy import default
from django.db import models

# Create your models here.
#blank=True es para hacer que el campo sea opcional
class Task(models.Model):
    title = models.CharField(max_length=100, default='Any')
    description = models.TextField(max_length=255, blank=True)
