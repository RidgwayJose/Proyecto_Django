from itertools import product
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

# Create your models here.

class Product(models.Model):
  cod_product = models.IntegerField()
  description = models.CharField(max_length=150)
  create = models.DateTimeField(auto_now_add=True)
  category = models.CharField(max_length=150)
  image =models.ImageField(upload_to='portfolio/images/')
  price = models.FloatField()
  stock = models.IntegerField()
  
  def __str__(self):
      return self.description
    
