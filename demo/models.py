from django.db import models


# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=16)
    age = models.IntegerField(default=10)
    sex = models.CharField(max_length=32)
