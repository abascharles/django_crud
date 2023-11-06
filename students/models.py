from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    image = models.ImageField(upload_to='students/images', default='profile.png')

    def __str__(self):
        return self.name
