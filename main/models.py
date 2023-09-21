from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    car = models.CharField(max_length=255)
    production_date = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)