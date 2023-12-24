from rest_framework import serializers
from .models import User

# Método para serializar apenas os dados da Model User:
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User # Indica qual é a model a ser serializada
    fields = '__all__' # Quais campos serão serializados
    # fields = ['user_nickname', 'user_tasks'] Exemplo caso queira serializar campos específicos
