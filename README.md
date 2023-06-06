# Proyecto Autenticacion Modelos de Programación 2

Esta es una página creada en el lenguaje python para la autenticación de un usuario mediante nombre y contraseña, para su creación se hizo uso de Django Rest Framework y la libreria sqlite3

Django REST framework es un conjunto de herramientas potente y flexible para crear API web, su documentación se puede consultar en el siguiente enlace:

[Django Rest Framework](https://www.django-rest-framework.org/)

Una razón por la cual se empleó Django Rest Framework es porque las sesiones de Django se basan de forma predeterminada en una cookie de sesión almacenada en el cliente, esto facilita el manejo de la autenticación.

Para el registro se empleó el módulo incorporado en Django "UserCreationForm" , el cual se usa para crear un nuevo usuario.
Para el Inicio de Sesión se empleó el módulo incorporado en Django "AuthenticationForm" , el cual se usa para el inicio de sesión de usuario.

También cabe destacar que Django emplea un patrón "Model Template Vista (MTV)", por ello las plantillas hechas en html se pueden encontrar en la carpeta "template"

"sqlite3 — DB-API 2.0 interfaz para bases de datos SQLite" se empleó para trabajar la conexión con la base de datos mediante un modelo DAO, su documentación se puede consultar en el siguiente enlace:

[Sqlite3](https://docs.python.org/es/3/library/sqlite3.html)

En el caso de sqlite3 , se escogió esta libreria debido a su facilidad en la implementación de la misma en el proyecto y que las funcionalidades que proporciona son las suficientes/necesarias para el funcionamiento del proyecto con la base de datos.
