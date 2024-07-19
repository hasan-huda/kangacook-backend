
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('users/', views.users_list, name='users-list'),
    path('users/create/', views.createUser, name='create-user'),
    path('users/<str:pk>/', views.user_detail, name='user-detail'),
    path('users/<str:pk>/update/', views.updateUser, name='update-user'),
    path('users/<str:pk>/delete/', views.deleteUser, name='delete-user'),
]