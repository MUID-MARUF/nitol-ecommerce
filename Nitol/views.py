from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product
from store.models import Category

def home(request):
    products = Product.objects.all()[:12]  # limit for homepage
    offered_products = Product.objects.all()[:4]   # first 4
    for_you_products = Product.objects.order_by('?')[:4]  # random

    return render(request, 'home/home.html', {
        'offered_products': offered_products,
        'for_you_products': for_you_products
    })

def about(request):
    return render(request, 'about/about.html')

def ai(request):
    return render (request, 'ai/ai.html')

def products(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')

    products = Product.objects.all()   # ✅ FIRST define

    if category_id:
        products = products.filter(category_id=category_id)

    if query:
        products = products.filter(name__icontains=query)

    categories = Category.objects.all()   # ✅ ADD THIS

    return render(request, 'products/products.html', {
        'products': products,
        'categories': categories,
    })

def cart(request):
    return render (request, 'cart/cart.html')

def profile(request):
    return render(request, 'profile/profile.html')

def contact(request):
    return render(request, 'contact/contact.html')
