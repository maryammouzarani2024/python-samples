from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True #everybody even anonymous user can make get,head and option requests
        else:
            return bool(request.user and request.user.is_staff)