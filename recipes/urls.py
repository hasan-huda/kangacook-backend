# recipes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('', views.getRecipes, name="recipes"),
    path('create/', views.getRecipes, name="create-recipe"),
    path('<str:pk>/', views.getRecipe, name="recipe"),
    path('<str:pk>/update/', views.updateRecipe, name="update-recipe"),
    path('<str:pk>/delete/', views.deleteRecipe, name="delete-recipe"),
]