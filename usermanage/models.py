from django.db import models

# Create your models here
class signin(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    #last_login = models.DateTimeField(auto_now=True)
    
    
    
