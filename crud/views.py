from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Product
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .forms import ProductForm
# Create your views here.
"""
 * def home(request):
 * products = Product.objects.all()
 * return render(request, 'home.html', {'producto': products})
_summary_
"""
class ProductListView(ListView):
  model = Product
  template_name = 'home.html'
  context_object_name = 'Productos'
  queryset = Product.objects.filter(category = 'Lacteos')
'''
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['titulo'] = 'Poncho'
      return context
'''
class ProductUpdateView(UpdateView):
    model = Product
    template_name = "crear.html"
    form_class = ProductForm
    success_url = reverse_lazy('listProduct')

class ProductCreateView(CreateView):
    model = Product
    template_name = "crear.html"
    form_class = ProductForm
    success_url = reverse_lazy('listProduct')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "product_confirm_delete.html"
    form_class = ProductForm
    
    def post(self, request, pk):
      product = Product.objects.get(id=pk)
      product.estado = False
      product.save()
      return redirect('listProduct')

'''
def edit_product(request, id):
  product  = Product.objects.get(id=id)
  return render(request,'editar.html', {'Producto' : product})
'''

'''  
def eliminar_producto(request,id):
    product= Product.objects.get(id=id)
    product.delete()
    
    return redirect('/')
'''
#class ModelDeleteView(DeleteView):
#    model = Product
#    template_name = 'home.html'
