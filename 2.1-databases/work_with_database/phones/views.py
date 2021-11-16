from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    params = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
    }
    href_sort = request.GET.get('sort', 'name')
    phone = Phone.objects.order_by(params.get(href_sort))
    context = {
        'phones': phone
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)
