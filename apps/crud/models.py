from email.policy import default
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from django.contrib import admin

# Create your models here.

class Product(models.Model):
  name = models.CharField(verbose_name='Producto', max_length=150)
  brand = models.CharField(verbose_name='Marca', max_length=30)
  category = models.CharField(verbose_name ='Categoria' ,max_length=150)
  image =models.ImageField(upload_to='portfolio/images/', default= "NULL")
  price = models.FloatField()
  stock = models.IntegerField()
  create = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
  status = models.BooleanField(verbose_name='Estado', default = True)
  
  def __str__(self):
      return self.name
    
  @admin.display(description = 'Codigo')
  def f_id(self):
    return str(self.pk).zfill(6)
