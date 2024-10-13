from django.shortcuts import render


def lista_empleados(request):
    empleados = ["Juan Pérez", "Ana Gómez", "Pedro Sánchez", "Lucía Fernández"]
    return render(request, "empleados.html", {"empleados": empleados})
