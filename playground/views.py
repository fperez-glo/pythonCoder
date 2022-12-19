# from .models import Familiar;
from .enums import generos;
from django.shortcuts import render;
from .models import Mascota;

# @csrf_protect
def renderMascotas(request):
    mascota_1 = Mascota(nombre='Juan', raza='Tucan', genero=generos.Masculino, especie= 'Ave');
    mascota_1.save();

    data = {"familiares": [
            {"name": mascota_1.nombre, "age": mascota_1.edad, "relationship": mascota_1.parentesco}, 
        ]};

    return render(request, 'familiares.html', data);

