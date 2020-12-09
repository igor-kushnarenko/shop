from django.shortcuts import render


def index(request):
	return render(request, 'web/index.html')


def shop(request):
	return render(request, 'web/shop.html')