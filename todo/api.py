from .models import Todo
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('title')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TodoSerializer