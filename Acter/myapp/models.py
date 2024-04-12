from django.db import models

# Create your models here.

class MyTodo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)