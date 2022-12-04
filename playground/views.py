from django.template import loader;
from django.http import HttpResponse;
from .models import Familiar;
from .enums import generos, parentescos;
from django.shortcuts import render;

# @csrf_protect
def renderFamiliares(request):
    familiar_1 = Familiar(nombre='Juan', edad=20, genero=generos.Masculino, parentesco= parentescos.Hermano);
    familiar_2 = Familiar(nombre='Romina', edad=16, genero=generos.Femenino, parentesco= parentescos.Hermano);
    familiar_3 = Familiar(nombre='Dardo', edad=59, genero=generos.Femenino, parentesco= parentescos.Padre);
    familiar_1.save();
    familiar_2.save();
    familiar_3.save();

    data = {"familiares": [
            {"name": familiar_1.nombre, "age": familiar_1.edad, "relationship": familiar_1.parentesco},
            {"name": familiar_2.nombre, "age": familiar_2.edad, "relationship": familiar_2.parentesco},
            {"name": familiar_3.nombre, "age": familiar_3.edad, "relationship": familiar_3.parentesco},
        ]};

    return render(request, 'familiares.html', data);

