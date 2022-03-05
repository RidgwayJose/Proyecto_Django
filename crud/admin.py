from django.contrib import admin
from crud.models import Product

@admin.register(Product)
class Admin(admin.ModelAdmin):
  search_fields = ['id', 'name']
  list_display = ['f_id', 'name', 'brand', 'create']
  ordering = ['id']
  list_filter= ['name', 'brand','category']  

# Register your models here.
#admin.site.register(Product)