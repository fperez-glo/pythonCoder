from django.db.models import TextChoices

class generos(TextChoices):
    Masculino = "M"
    Femenino = "F"
    Otro = "X"

class parentescos(TextChoices):
    Primo = "Primo"
    Padre = "Padre"
    Madre = "Madre"
    Abuelo = "Abuelo"
    Hermano = "Hermano"
