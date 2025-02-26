from django.db import models

# Create your models here.
class BikeModel(models.Model):
    name=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    price=models.IntegerField()
    mileage=models.IntegerField()
    image=models.ImageField(upload_to='image/')