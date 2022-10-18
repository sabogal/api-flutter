# **Estructura y comandos**

## **Contenido del Dockerfile**

`Dockerfile`
```
# Imagen de python
FROM python:3.9

# Declaración del entorno
ENV PYTHONUNBUFFERED 1

# creación directorio de trabajo
RUN mkdir /app

# acceder al directorio de trabajo creado
WORKDIR /app

# añadir requirements al directorio de trabajo
ADD requirements.txt /app/

# instalacion de paquetes de python del requirements
RUN pip install -r requirements.txt

# añadir todo lo del directorio al app
ADD . /app/
```

## **Contenido del docker-compose**
`docker-compose.yml`
```
version: '3.5'
services: 
  django_rest:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
```

## Creacion del proyecto base de Django
```
sudo docker-compose run --rm django_rest django-admin startproject main_project .
```

## Activación del Contenedor
```
sudo docker-compose up
```
### detatch mode (segundo plano)
```
sudo docker-compose up -d
```

## En caso de modificacion del requirements.txt, hacer un build de la app
```
sudo docker-compose build
```

## Migracion de modelos a la base de datos
```
sudo docker-compose run --rm django_rest python manage.py migrate
```

## Migración base de datos
```
sudo docker-compose run --rm django_rest python manage.py makemigrations
```

## Creación super usuario
```
sudo docker-compose run --rm django_rest python manage.py createsuperuser
```

## Creación de la App (api)
```
sudo docker-compose run --rm django_rest python manage.py startapp [nombre_app]

```
<!-- 
# Ejecución de pruebas para cada App
```
sudo docker-compose run --rm django_rest python manage.py test app/erp
```

# Ejecución de pruebas desde el archivo principal de la app
```
sudo docker-compose run --rm django_rest python manage.py test perfiles
``` 

 
# Limpiar bases de datos
```
delete from apli_producto; 

delete from sqlite_sequence where name='apli_producto';

UPDATE SQLITE_SEQUENCE SET SEQ=1 WHERE NAME='apli_producto';
``` -->
