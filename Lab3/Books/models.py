from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    
    def __str__(self):
        return self.name

class ISBN(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    isbn_number = models.CharField(max_length=13, unique=True)

class Book(models.Model):
    title = models.CharField(max_length=50, validators=[MinLengthValidator(10), MaxLengthValidator(50)])
    description = models.TextField()
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    views = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 
    categories = models.ManyToManyField(Category)
    isbn = models.OneToOneField(ISBN, on_delete=models.CASCADE, default=1)  

    def __str__(self):
        return self.title
    

    
    


    

