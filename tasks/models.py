from django.db import models
from django import forms 


class Task(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
