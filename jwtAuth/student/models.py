# models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)         
    roll = models.IntegerField(unique=True)         
    department = models.CharField(max_length=50)    
    result = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.roll})"
