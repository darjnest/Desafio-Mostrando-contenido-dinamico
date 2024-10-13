# Desafío: Mostrando Contenido Dinámico con Django

Este proyecto es parte de un desafío para demostrar cómo mostrar una lista de empleados de manera dinámica en una página web utilizando Django.

## Descripción

El objetivo es crear una aplicación Django que muestre una lista de nombres de empleados almacenada en una lista de Python. La cantidad de empleados es indefinida, y la lista se muestra en un template HTML.

## Requerimientos

- **Crear un proyecto Django** con una aplicación para mostrar la lista de empleados.
- **Generar la vista, URL y template** para mostrar la información en la web.
- **Pasar el listado de empleados** a la vista mediante contexto.

## Tecnologías

- [Python](https://www.python.org/) 3.12+
- [Django](https://www.djangoproject.com/) 4.2+
- Entorno virtual para gestionar dependencias.

## Instalación

1. Clonar este repositorio:

   ```bash
   git clone https://github.com/usuario/desafio-django-empleados.git
   cd desafio-django-empleados
   ```

2. Crear y activar el entorno virtual:

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # macOS/Linux
   myenv\Scripts\activate  # Windows
   ```

3. Instalar las dependencias:

   ```bash
   pip install django
   ```

4. Ejecutar las migraciones:

   ```bash
   python manage.py migrate
   ```

5. Iniciar el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

## Uso

1. Accede a la URL `http://127.0.0.1:8000/empleados/` en tu navegador para ver la lista de empleados.

## Estructura del Proyecto

```bash
desafio-django-empleados/
│
├── empleados_proyecto/        # Carpeta del proyecto principal
│   ├── empleados_proyecto/
│   ├── empleados_app/         # Carpeta de la aplicación
│   │   ├── templates/
│   │   │   └── empleados.html # Template para mostrar empleados
│   │   ├── urls.py            # Definición de las rutas
│   │   └── views.py           # Lógica de la vista
│   └── manage.py              # Script de gestión de Django
└── README.md                  # Documentación del proyecto
```

Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, crea un fork y envía un pull request.
