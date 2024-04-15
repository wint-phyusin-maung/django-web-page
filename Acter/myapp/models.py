from django.db import models

# Create your models here.

class MyTodo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    

class MyN5Course(models.Model):
    chapter = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    kanji = models.IntegerField(default=0)