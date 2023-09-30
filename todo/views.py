from django.shortcuts import render

from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    
@api_view(['GET'])
def GetRoutes(request) :
    
    routes = [
        {
            'Endpoint' : '/todo/',
            'method' : 'GET',
            'body' : None,
            'descripcion' : 'descripcion de la tarea' 
        },
        {
            'Endpoint' : '/todo/id',
            'method' : 'GET',
            'body' : None,
            'descripcion' : 'numero de la tarea'    
        },
        {
            'Endpoint' : '/todo/crear',
            'method' : 'POST',
            'body' : {'body':""},
            'descripcion' : 'Crea nueva tarea'  
        },
        {
            'Endpoint' : '/todo/id/actualizar',
            'method' : 'PUT',
            'body' : {'body' : ""},
            'descripcion' : 'Modifica una tarea existente' 
        },
        {
            'Endpoint' : '/todo/id/eliminar',
            'method' : 'DELETE',
            'body' : None,
            'descripcion' : 'Elimina una tarea existente' 
        },
        
    ]
    return Response(routes)

@api_view(['GET'])
def getTodo(request):
    todos = Todo.objects.all() 
    serializer = TodoSerializer(todos, many=True)
    return Response('serializer.data')
