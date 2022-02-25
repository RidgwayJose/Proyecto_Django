from tempfile import template
from django.shortcuts import render
from .models import Product
from django.views.generic import ListView

# Create your views here.
"""
 * def home(request):
 * products = Product.objects.all()
 * return render(request, 'home.html', {'producto': products})
_summary_
"""
class HomeListView(ListView):
  model = Product
  template_name = 'home.html'
  
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['titulo'] = 'CRUD'
      return context
  
  