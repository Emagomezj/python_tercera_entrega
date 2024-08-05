from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    
class Books(models.Model):
    name = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    year = models.DateField()
    editorial = models.CharField(max_length=40)
    edition = models.CharField(max_length=40)
    available = models.BooleanField()
    
class users_libraries(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    books = models.ManyToManyField(Books)
    available = models.BooleanField()