from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    #Añadir atributos de user
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #Añadir los demas atributos
    name=models.CharField(max_length=50,null=False);
    age=models.IntegerField(null=False);
    email=models.EmailField(max_length=50,null=False);


    def __str__(self):
        return self.user.username
