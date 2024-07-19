from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .models import Recipe
from .serializers import RecipeSerializer
from . import serializers
from .utils import updateRecipe, getRecipeDetail, deleteRecipe, getRecipesList, createRecipe
# Create your views here.


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
            'Endpoint': '/recipes/id',
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
            'Endpoint': '/recipes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing recipe with data sent in post request'
        },
        {
            'Endpoint': '/recipes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting recipe'
        },
    ]
    return Response(routes)


# /recipes GET
# /recipes POST
# /recipes/<id> GET
# /recipes/<id> PUT
# /recipes/<id> DELETE

@api_view(['GET', 'POST'])
def getRecipes(request):

    if request.method == 'GET':
        return getRecipesList(request)

    if request.method == 'POST':
        return createRecipe(request)


@api_view(['GET', 'PUT', 'DELETE'])
def getRecipe(request, pk):

    if request.method == 'GET':
        return getRecipeDetail(request, pk)

    if request.method == 'PUT':
        return updateRecipe(request, pk)

    if request.method == 'DELETE':
        return deleteRecipe(request, pk)


