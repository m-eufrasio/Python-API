from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json

@api_view(['GET'])
def get_users(request):

# PEGANDO DADOS:
  if request.method == 'GET': # Verificação, não é obrigatório mas é uma boa prática
    users = User.objects.all() # Captura todos os objetos do database User (queryset)

    serializer = UserSerializer(users, many=True) # Serializa os users em json, many é o relationship para o queryset
    return Response(serializer.data) # Retorno dos dados serializados
  
  return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def get_by_nick(request, nick): # O nick é aquele declarado na rota para capturar um usuário específico

# PEGANDO DADOS ESPECÍFICOS:
  try:
    user = User.object.get(pk=nick) # Esse user não é um queryset, é um objeto único
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = UserSerializer(user)

  if request.method == 'PUT': # Caso seja um PUT no qual envio dados pela rota/url

    serializer = UserSerializer(user, data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_202_ACCEPTED)
      
    return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request):

  # ACESSOS:

    if request.method == 'GET':

      try:
        if request.GET['user']: # Verifica se existe um parâmetro chamado user (/user=xxxx)

            user_nickname = request.GET['user'] # Encontra esse parâmetro

            try:
              user = User.objects.get(pk=user_nickname) # Pega o objeto do database
            except:
              return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = UserSerializer(user) # Serializa o objeto para JSON
            return Response(serializer.data) # Retorna o objeto serializado como response

        else:
          return Response(status=status.HTTP_400_BAD_REQUEST)
    
      except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

  # CRIANDO DADOS:
    if request.method == 'POST':

      new_user = request.data # Acessa os dados enviados do frontend

      serializer = UserSerializer(data=new_user) # Nesse ponto é serializado DADOS e não OBJETOS!

      if serializer.is_valid(): # is_valid() é uma função do Serializer que verifica se os dados são válidos
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) # Para validar, retorna os dados e status 201
      
      return Response(status=status.HTTP_400_BAD_REQUEST)
    
  # EDITANDO DADOS
    
    if request.method == 'PUT':

      nickname = request.data['user_nickname']

      try:
        updated_user = User.objects.get(pk=nickname)
      except:
        return Response(status=status.HTTP_404_NOT_FOUND)
      
      serializer = UserSerializer(updated_user, data=request.data)

      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
      
      return Response(status=status.HTTP_400_BAD_REQUEST)
    
  # DELETANDO DADOS

    if request.method == 'DELETE':

      try:
        user_to_delete = User.objects.get(pk=request.data['user_nickname'])
        user_to_delete.delete()
      except:
        return Response(status=status.HTTP_400_BAD_REQUEST)







# def databaseDjango():
#   data = User.objects.get(pk='matheus.eufrasio') # Sempre devolve um objeto;
#   # Filter irá filtrar os registros de acordo com a regra passada:
#   data = User.objects.filter(user_age='23') # Retorna um queryset, que contém varios valores
#   # Exclude faz a mesma coisa que o filter, porém de forma inversa:
#   data = User.objects.exclude(user_age='23') # Retorna objetos que NÃO tem idade 23 (queryset)

#   data.save() # Salva esses objetos
#   data.delete() # Deleta esses objetos
