from django.db import models

# Create your models here.
# https://sqliteviewer.app/

class Student(models.Model):
    email = models.EmailField(max_length=254, default='default@example.com')
    name=models.CharField(max_length=30) # primary_key=True, unique=True
    password = models.CharField(max_length=128)
    img = models.ImageField(upload_to='images/', default='def.png', null=True, blank=True)

    def __str__(self):
        return self.name