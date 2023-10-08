from rest_framework import routers
from .api import TodoViewSet
from . import views
from django.urls import path, include


router = routers.DefaultRouter()
router.register('api/todo', views.TodoViewSet, 'todo')

urlpatterns = [
    path('', include(router.urls)),
]
