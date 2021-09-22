from django.shortcuts import render, redirect
from .models import Products
from django.views.generic import DetailView


def index(request):
    return render(request, 'web/index.html')


def shop(request):
    products = Products.objects.all()
    data = {
        'products': products
    }
    return render(request, 'web/shop.html', data)


class ProductViews(DetailView):
    model = Products
    template_name = 'web/product_view.html'
    context_object_name = 'product'
