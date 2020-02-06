from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.SmallIntegerField()
    salary = models.DecimalField(max_digits=7,decimal_places=2)
    birthday = models.DateField()
