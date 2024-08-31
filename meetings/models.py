from django.db import models

# Create your models here.
class Meeting(models.Model):
    nombre = models.CharField(max_length=200)
    reuniones = models.JSONField()