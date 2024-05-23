from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from drf_yasg.utils import swagger_auto_schema

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'admin':
            return True
        elif request.method in permissions.SAFE_METHODS:
            return True
        else:
            return False

@swagger_auto_schema(method='get', responses={200: TodoSerializer})
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated, IsAdminOrReadOnly])
def get_todo(request, id):
    try:
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TodoSerializer(todo)
    return Response(serializer.data)

@swagger_auto_schema(method='get', responses={200: TodoSerializer(many=True)})
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_todos(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admins to edit objects.
    """
    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the admin user.
        return request.user and request.user.is_staff
        
@swagger_auto_schema(method='post', request_body=TodoSerializer)
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated, IsAdminOrReadOnly])
def create_todo(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=TodoSerializer)
@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated, IsAdminOrReadOnly])
def update_todo(request, id):
    try:
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TodoSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='delete', responses={204: 'No Content'})
@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated, IsAdminOrReadOnly])
def delete_todo(request, id):
    try:
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    todo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
