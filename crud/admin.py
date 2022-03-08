from django.contrib import admin
from crud.models import Product
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ProductoResource(resources.ModelResource):
  class Meta:
    model = Product

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
  search_fields = ['id', 'name']
  list_display = ['f_id', 'name', 'brand', 'create']
  ordering = ['id']
  list_filter= ['name', 'brand','category', 'status']
  resources_class = ProductoResource  

# Register your models here.
#admin.site.register(Product)