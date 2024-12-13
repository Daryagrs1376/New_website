from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, AllowAny


class IsNotAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_authenticated

class NewsSearchView(APIView):
    @permission_classes([AllowAny])  
    def get(self, request):
        return Response({"message": "News search works!"})

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.reporter == request.user
    
class IsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff