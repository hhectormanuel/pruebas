from django.db import models

# Create your models here.


class Usuario(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=70)
    edad = models.IntegerField()
