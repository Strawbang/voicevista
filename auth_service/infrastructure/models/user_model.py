from django.db import models

class UserModel(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128) 
    
    def __str__(self):
        return self.username