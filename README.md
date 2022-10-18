# proyecto_Dagma

INSTALAR REQUIREMENTS.TXT = pip install -r requirements.txt

Esta es una api desarrollada en Django rest framework, esta es un loguin que tiene validacion via token esta puede crear usuarios desde http://localhost:8000/user/ y los valores que se deben de mandar son:

{
    "password": "",
    "is_superuser": false,
    "username": "",
    "first_name": "",
    "last_name": "",
    "email": "",
    "is_staff": false,
    "is_active": false,
    "groups": [],
    "user_permissions": []
}

Aparte de esto tambien tiene la funcionalidad mediante la url http://localhost:8000/api/token/ de consultar el token de un usuario ya creado
