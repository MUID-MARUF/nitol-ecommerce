from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product
from store.models import Category

def home(request):
    products = Product.objects.all()[:12]  # limit for homepage
    return render(request, 'home/home.html', {'products': products})

def about(request):
    return render(request, 'about/about.html')

def ai(request):
    return render (request, 'ai/ai.html')

def products(request):
    category_id = request.GET.get('category')  # get from URL

    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    categories = Category.objects.all()

    return render(request, 'products/products.html', {
        'products': products,
        'categories': categories
    })

def cart(request):
    return render (request, 'cart/cart.html')

def profile(request):
    return render(request, 'profile/profile.html')

def contact(request):
    return render(request, 'contact/contact.html')
