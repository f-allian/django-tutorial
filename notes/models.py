from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Notes(models.Model): #This way Django knows its a model
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True) #True means every time the node is created a time is added to it
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")