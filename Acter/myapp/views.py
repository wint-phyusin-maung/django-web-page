from django.shortcuts import render,HttpResponse
from .models import MyTodo
from .models import MyN5Course

# Create your views here.

def home(request):
    return render(request, "home.html")


def todos(request):
    todos = MyTodo.objects.all()
    return render(request,"todos.html", {"todos": todos})

def n5course(request):
    n5chapters = MyN5Course.objects.all()
    return render(request,"n5course.html",{"n5courses": n5chapters})