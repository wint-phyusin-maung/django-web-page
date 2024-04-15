from django.urls import path 
from . import views

urlpatterns = [
    path("", views.home , name="home"),
    path("todos/",views.todos),
    path("n5course/",views.n5course)
]
