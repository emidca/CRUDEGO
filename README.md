# CRUD para EGO - Documentación del proyecto

Mis datos:
Emiliano Di Campli.

- Teléfono: +3516814194
- Localidad: Buenos Aires, Argentina
- GitHub: [malhee](https://github.com/malhee)
- LinkedIn: [Emiliano Di Campli](https://www.linkedin.com/in/emiliano-di-campli-848a57235/)

Este proyecto implementa un CRUD (Create, Read, Update, Delete) para administrar autos utilizando Django y Django REST Framework.

## Rutas de API

- **GET /api/cars/**: Obtiene todos los autos disponibles.
- **GET /api/cars/{id}/**: Obtiene los detalles de un auto específico.
- **POST /api/cars/**: Crea un nuevo auto.
- **PUT /api/cars/{id}/**: Actualiza los detalles de un auto existente.
- **DELETE /api/cars/{id}/**: Elimina un auto existente.

## Acceso al Administrador de Django

El proyecto también proporciona un panel de administración para gestionar los datos de los autos. Para acceder al administrador de Django, sigue estos pasos:

1. Ejecuta el servidor de desarrollo de Django con el comando `python manage.py runserver`.
2. Abre un navegador web y visita `http://localhost:8000/admin`.
3. Ingresa tus credenciales de superusuario para acceder al panel de administración.

## Funciones del CRUD

El CRUD para los autos incluye las siguientes funciones:

- **Listar autos**: La ruta GET `/api/cars/` devuelve una lista de todos los autos disponibles.
- **Obtener detalles de un auto**: La ruta GET `/api/cars/{id}/` devuelve los detalles de un auto específico.
- **Crear un nuevo auto**: La ruta POST `/api/cars/` permite crear un nuevo auto proporcionando los datos requeridos en el cuerpo de la solicitud.
- **Actualizar un auto**: La ruta PUT `/api/cars/{id}/` permite actualizar los detalles de un auto existente.
- **Eliminar un auto**: La ruta DELETE `/api/cars/{id}/` permite eliminar un auto existente.

## Requisitos del proyecto

- Python 3.x
- Django
- Django REST Framework

## Configuración y ejecución

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias necesarias ejecutando `pip install -r requirements.txt`.
3. Aplica las migraciones con el comando `python manage.py migrate`.
4. Crea un superusuario con el comando `python manage.py createsuperuser`.
5. Inicia el servidor de desarrollo de Django con `python manage.py runserver`.

¡Listo! Ahora puedes acceder a la API y al administrador de Django para administrar los autos.
