from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='hello'),
    path('users/', views.UserListCreateView.as_view(), name='users-list-create'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='users-detail'),
    path('roles/', views.RoleListCreateView.as_view(), name='roles-list-create'),
    path('roles/<int:pk>/', views.RoleDetailView.as_view(), name='roles-detail'),
]