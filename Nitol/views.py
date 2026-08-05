from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
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

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products/productDetails.html', {
        'product': product
    })

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user = request.user

        user.first_name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.save()

        profile = user.profile
        profile.phone = request.POST.get('phone')
        profile.address = request.POST.get('address')

        if request.FILES.get('image'):
            profile.image = request.FILES.get('image')

        profile.save()

        return redirect('/profile/')

    return render(request, 'profile/editProfile.html')