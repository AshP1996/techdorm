Project Overview
This project provides a Django-based backend with APIs for user authentication and managing a to-do list. The project includes JWT token-based authentication and API documentation via Swagger.

#Superuser Credentials


Username: Admin
Password: Admin


#Authentication API Endpoints

Register
URL: auth/register/
Method: POST
Name: register
Description: Registers a new user.
Request Body:
json

{
  "username": "string",
  "password": "string"
}
Response:
json

{
  "id": "integer",
  "username": "string"
}
Login
URL: auth/login/
Method: POST
Name: login
Description: Authenticates a user and returns a JWT token.
Request Body:
json

{
  "username": "string",
  "password": "string"
}
Response:
json

{
  "token": "string"
}
To-Do API Endpoints
Get To-Do
URL: todos/todos/get/<int:id>/
Method: GET
Name: get_todo
Description: Retrieves a to-do item by its ID.
Response:
json

{
  "id": "integer",
  "title": "string",
  "description": "string",
  "completed": "boolean"
}
Get All To-Dos
URL: todos/todos/getall/
Method: GET
Name: get_all_todos
Description: Retrieves all to-do items.
Response:
json

[
  {
    "id": "integer",
    "title": "string",
    "description": "string",
    "completed": "boolean"
  }
]
Create To-Do
URL: todos/todos/create/
Method: POST
Name: create_todo
Description: Creates a new to-do item.
Request Body:
json

{
  "title": "string",
  "description": "string",
  "completed": "boolean"
}
Response:
json

{
  "id": "integer",
  "title": "string",
  "description": "string",
  "completed": "boolean"
}
Update To-Do
URL: todos/todos/put/<int:id>/
Method: PUT
Name: update_todo
Description: Updates an existing to-do item by its ID.
Request Body:
json

{
  "title": "string",
  "description": "string",
  "completed": "boolean"
}
Response:
json

{
  "id": "integer",
  "title": "string",
  "description": "string",
  "completed": "boolean"
}
Delete To-Do
URL: todos/todos/delete/<int:id>/
Method: DELETE
Name: delete_todo
Description: Deletes a to-do item by its ID.
Response:
json

{
  "detail": "To-Do item deleted successfully"
}
Admin and Swagger Endpoints
Swagger
URL: swagger/
Name: schema-swagger-ui
Description: Provides interactive API documentation via Swagger.
Admin
URL: admin/
Description: Django admin interface.
Running the Project
Django Commands
Install Dependencies

/////////////////////////////////////////////////////////////////////////////

pip install -r requirements.txt
Apply Migrations

/////////////////////////////////////////////////////////////////////////////

python manage.py migrate
Create Superuser

/////////////////////////////////////////////////////////////////////////////

python manage.py createsuperuser
# Follow the prompts to create the superuser
Run the Development Server

/////////////////////////////////////////////////////////////////////////////

python manage.py runserver
Additional Setup
Adding JWT Token Authentication
Install Django REST framework and JWT packages

/////////////////////////////////////////////////////////////////////////////

pip install djangorestframework djangorestframework-jwt
Update settings.py


INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_jwt',
    ...
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

# JWT settings
JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'my_project.utils.my_jwt_response_handler'
}
Create a response handler (optional)



# my_project/utils.py
from rest_framework_jwt.utils import jwt_payload_handler
from rest_framework_jwt.settings import api_settings

def my_jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': {
            'id': user.id,
            'username': user.username
        }
    }
Update urls.py


from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    ...
    path('auth/login/', obtain_jwt_token, name='login'),
    ...
]
Adding Swagger
Install drf-yasg

/////////////////////////////////////////////////////////////////////////////

pip install drf-yasg

Update settings.py

python

INSTALLED_APPS = [
    ...
    'drf_yasg',
    ...
]
Update urls.py

python

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API documentation for the project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    ...
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ...
]

/////////////////////////////////////////////////////////////

Using SQLite as the Database
By default, Django uses SQLite as the database. Ensure your settings.py file is configured as follows:

ENGINE: django.db.backends.sqlite3
NAME: BASE_DIR / "db.sqlite3"
