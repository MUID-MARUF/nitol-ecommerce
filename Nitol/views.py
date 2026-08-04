from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'about/about.html')

def ai(request):
    return render (request, 'ai/ai.html')

def products(request):
    return render (request, 'products/products.html')

def login(request):
    return render (request, 'auth/login.html')

def signup(request):
    return render (request, 'auth/signup.html')

def cart(request):
    return render (request, 'cart/cart.html')

def profile(request):
    return render(request, 'profile/profile.html')

def contact(request):
    return render(request, 'contact/contact.html')
