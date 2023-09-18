from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Users, Roles
from .serializers import UsersSerializer, RolesSerializer
from rest_framework import generics

# Create your views here.
# TODO: add a view (Actually not allowed for lab #2)
def index(request):
    return HttpResponse("<h1> Lab #2: A simple CRUD with HTTP. <br> Hello World!</h1>")

class UserListCreateView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    #function to manage the GET request if the queryset is empty
    def list(self, request, *args, **kwargs):
        users = self.get_queryset()
        response = super().list(request, *args, **kwargs)
        if not users.exists():
            response = JsonResponse(status=204, data={})
        return response

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class RoleListCreateView(generics.ListCreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    
    #function to manage the GET request if the queryset is empty
    def list(self, request, *args, **kwargs):
        roles = self.get_queryset()
        response = super().list(request, *args, **kwargs)
        if not roles.exists():
            response = JsonResponse(status=204, data={})
        return response

class RoleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer