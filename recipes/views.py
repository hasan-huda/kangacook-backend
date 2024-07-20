# recipes/views.py
from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .utils import getRecipesList, getRecipeDetail, createRecipe, updateRecipe, deleteRecipe

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/recipes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of recipes'
        },
        {
            'Endpoint': '/recipes/<id>/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single recipe object'
        },
        {
            'Endpoint': '/recipes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new recipe with data sent in post request'
        },
        {
            'Endpoint': '/recipes/<id>/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates an existing recipe with data sent in post request'
        },
        {
            'Endpoint': '/recipes/<id>/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing recipe'
        },
    ]
    return Response(routes)

@api_view(['GET', 'POST'])
def getRecipes(request):
    if request.method == 'GET':
        return getRecipesList(request)
    elif request.method == 'POST':
        return createRecipe(request)

@api_view(['GET', 'PUT', 'DELETE'])
def getRecipe(request, pk):
    if request.method == 'GET':
        return getRecipeDetail(request, pk)
    elif request.method == 'PUT':
        return updateRecipe(request, pk)
    elif request.method == 'DELETE':
        return deleteRecipe(request, pk)