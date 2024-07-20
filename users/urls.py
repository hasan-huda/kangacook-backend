# users/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('', views.users_list, name='users-list'),
    path('create/', views.createUser, name='create-user'),
    path('<str:pk>/', views.user_detail, name='user-detail'),
    path('<str:pk>/update/', views.updateUser, name='update-user'),
    path('<str:pk>/delete/', views.deleteUser, name='delete-user'),
]