from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    def __str__(self):
        return f'{self.name} {self.surname}'

    
class Books(models.Model):
    name = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    year = models.DateField()
    editorial = models.CharField(max_length=40)
    edition = models.CharField(max_length=40)
    available = models.BooleanField()
    def __str__(self):
        return f'{self.name} by {self.author}'
class Users_libraries(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    books = models.ManyToManyField(Books)
    available = models.BooleanField()
    def __str__(self):
        return f"{self.user}'s library"