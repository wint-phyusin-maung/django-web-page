from django.shortcuts import render,HttpResponse
from .models import MyTodo

# Create your views here.

def home(request):
    return render(request, "home.html")


def todos(request):
    todos = MyTodo.objects.all()
    return render(request,"todos.html", {"todos": todos})