from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# TODO: add a view (Actually not allowed for lab #2)
def hello(request):
    return HttpResponse("<h1> Lab #2: A simple CRUD with HTTP. <br> Hello World!</h1>")