from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
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

def add_to_cart(request, product_id):
    qty = int(request.GET.get('qty', 1))

    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += qty
    else:
        cart[str(product_id)] = qty

    request.session['cart'] = cart

    return redirect(request.META.get('HTTP_REFERER', 'products'))

def cart_view(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        subtotal = product.price * quantity
        total += subtotal

        items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })

    return render (request, 'cart/cart.html', {
        'cart_items': items,
        'total': total
    })

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        del cart[str(product_id)]

    request.session['cart'] = cart
    return redirect('cart')

def update_cart(request, product_id):
    cart = request.session.get('cart', {})

    action = request.GET.get('action')

    if str(product_id) in cart:
        if action == 'increase':
            cart[str(product_id)] += 1
        elif action == 'decrease':
            cart[str(product_id)] -= 1

            if cart[str(product_id)] <= 0:
                del cart[str(product_id)]

    request.session['cart'] = cart
    return redirect('cart')

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