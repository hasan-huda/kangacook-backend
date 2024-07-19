from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('recipes/', views.getRecipes, name="recipes"),
    path('recipes/create/', views.createRecipe, name="create-recipe"),
    path('recipes/<str:pk>/', views.getRecipe, name="recipe"),
    path('recipes/<str:pk>/update/', views.updateRecipe, name="update-recipe"),
    path('recipes/<str:pk>/delete/', views.deleteRecipe, name="delete-recipe"),
]