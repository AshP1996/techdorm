from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Admins have full access
        if request.user.role == 'admin':
            return True
        
        # Users can only view the list of todo items
        if request.user.role == 'user' and view.action in ['list', 'retrieve']:
            return True
        
        # Otherwise, access is denied
        return False
