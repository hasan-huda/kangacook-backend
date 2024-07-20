# users/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('', views.users_list, name='users-list'),
    path('create/', views.users_list, name='create-user'),
    path('<str:pk>/', views.user_detail, name='user-detail'),
    path('<str:pk>/update/', views.user_detail, name='update-user'),
    path('<str:pk>/delete/', views.user_detail, name='delete-user'),
    path('email/<str:email>/', views.get_user_id_by_email, name='get-user-id-by-email'),
]