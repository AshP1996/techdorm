from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Todo
from .serializers import TodoSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'admin':
            return True
        elif request.method in permissions.SAFE_METHODS:
            return True
        else:
            return False

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]

    @action(detail=True, methods=['get'])
    def get(self, request, pk=None):
        todo = self.get_object()
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def getall(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def put(self, request, pk=None):
        todo = self.get_object()
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    @action(detail=True, methods=['post'])
    def create(self, request, pk=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk=None):
        todo = self.get_object()
        todo.delete()
        return Response({'message': 'Todo deleted successfully'})
