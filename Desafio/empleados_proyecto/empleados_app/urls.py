from django.urls import path
from . import views

urlpatterns = [
    path("empleados/", views.lista_empleados, name="lista_empleados"),
]
