from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'#['id' ,'description', 'category', 'stock', 'price']
        labels = {
          'id' :'Codigo del Producto',
          'name' : 'Nombre del Producto',
          'category': 'Categoria',
          'stock': 'Stock',
          'price': 'Precio'
        }
        '''
        widgets ={
          'id': forms.(
            attrs= {
              'class':'form-control',
            }
          )
        }
        '''


  

