from rest_framework import serializers
from .models import Todo


# class TodoSerializer(serializers.Serializer):
#     class Meta:
#         model = Todo
#         fields = '__all__'


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'date', 'done']