from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'catalog/home.html', {'products': products})


def contact(request):
    return render(request, 'catalog/contact.html')


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'catalog/product_detail.html', {'product': product})
