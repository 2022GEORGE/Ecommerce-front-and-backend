from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    tprice= models.DecimalField(max_digits=10, decimal_places=2,null=True)
    image = models.ImageField(upload_to='products/',null=True)
    category=models.CharField(max_length=20,null=True)
class customer(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=255,null=True)