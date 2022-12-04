
from django.db import models;
from .enums import generos, parentescos;
from django.utils.timezone import now;

class Familiar (models.Model):
    nombre = models.CharField(max_length=50);
    edad = models.IntegerField();
    genero = models.CharField(max_length=1, choices=generos.choices);
    parentesco = models.CharField(max_length=20, choices=parentescos.choices);
    createdAt = models.DateTimeField(default=now);

    def __str__(self):
        return f'{self.nombre} ({self.parentesco})'