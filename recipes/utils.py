from rest_framework.response import Response
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.parsers import JSONParser


def getRecipesList(request):
    recipes = Recipe.objects.all().order_by('-updated')
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)


def getRecipeDetail(request, pk):
    recipes = Recipe.objects.get(id=pk)
    serializer = RecipeSerializer(recipes, many=False)
    return Response(serializer.data)


def createRecipe(request):
    data = request.data
    recipe = Recipe.objects.create(
        title=data.get('title', ''),
        description=data.get('description', ''),
        ingredients=data.get('ingredients', ''),
        instructions=data.get('instructions', ''),
        image_url=data.get('image_url', ''),
        user_email=data.get('user_email', ''),
    )
    serializer = RecipeSerializer(recipe, many=False)
    return Response(serializer.data)

def updateRecipe(request, pk):
    data = request.data
    recipe = Recipe.objects.get(id=pk)
    serializer = RecipeSerializer(instance=recipe, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


def deleteRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    recipe.delete()
    return Response('Recipe was deleted!')