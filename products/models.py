from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    image = models.CharField(max_length=2500)