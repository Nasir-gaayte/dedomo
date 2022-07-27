from django.db import models

# Create your models here.

class Users_model(models.Model):
    
    username= models.CharField(max_length=150, unique=True)
    email= models.EmailField(max_length=250)
    first = models.CharField(max_length=150)
    family = models.CharField(max_length=150, default="")
    note = models.CharField(max_length=900)
    
    def __str__(self):
        return self.username
    
