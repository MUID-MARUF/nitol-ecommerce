from django.shortcuts import render, redirect
from django.contrib.auth.forms import User
from django.contrib.auth import login, logout, authenticate

# Signup View
def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check password match
        if password != confirm_password:
            return render(request, 'auth/signup.html', {
                'error': 'Passwords do not match'
            })

        # Check if user exists
        if User.objects.filter(username=email).exists():
            return render(request, 'auth/signup.html', {
                'error': 'User already exists'
            })

        # Create user
        user = User.objects.create_user(
            username=email,   # using email as username
            email=email,
            password=password,
            first_name=name
        )

        login(request, user)
        return redirect('/')
    return render(request, 'auth/signup.html')

#Login View
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # authenticate user (remember: username = email)
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'auth/login.html', {
                'error': 'Invalid email or password'
            })

    return render(request, 'auth/login.html')

#Logout View
def logout_view(request):
    logout(request)
    return redirect('/')