from django.urls import path
from todo import views as todo_views

urlpatterns = [
    path('todos/get/<int:id>/', todo_views.get_todo, name='get_todo'),
    path('todos/getall/', todo_views.get_all_todos, name='get_all_todos'),
    path('todos/create/', todo_views.create_todo, name='create_todo'),
    path('todos/put/<int:id>/', todo_views.update_todo, name='update_todo'),
    path('todos/delete/<int:id>/', todo_views.delete_todo, name='delete_todo'),
]
