
from django.db import models;
from .enums import generos, unidadDosis;
from django.utils.timezone import now;
import uuid;

class Mascota (models.Model):
    idMascota = models.UUIDField(primary_key=True, default=uuid.uuid4);
    nombre = models.CharField(max_length=50);
    raza = models.CharField(max_length=50);
    genero = models.CharField(max_length=1, choices= generos.choices);
    especie = models.CharField(max_length=50);
    idPlan = models.ForeignKey("SeguroMedico", on_delete= models.RESTRICT);
    fCreacion = models.DateField(default=now);

class Vacunacion (models.Model):
    idMascota = models.ForeignKey("Mascota", on_delete= models.RESTRICT);
    vacuna = models.CharField(max_length=10);
    dosis = models.FloatField();
    unidadDosis = models.CharField(max_length=2, choices= unidadDosis.choices);
    fCreacion = models.DateField(default=now);

class SeguroMedico (models.Model):
    idPlan = models.CharField(max_length=10,primary_key=True);
    plan = models.CharField(max_length=20);