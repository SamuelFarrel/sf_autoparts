from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField
    amount = models.IntegerField
    description = models.TextField
    car = models.CharField
    production_date = models.DateField
    price = models.IntegerField