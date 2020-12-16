from django.shortcuts import render
from .models import Products


def index(request):
	return render(request, 'web/index.html')


def shop(request):
	products = Products.objects.all()
	data = {
		'products': products
	}
	return render(request, 'web/shop.html', data)