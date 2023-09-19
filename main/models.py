from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    car = models.CharField(max_length=255)
    production_date = models.DateField(auto_now_add=True)
    price = models.IntegerField()