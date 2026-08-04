from .import views 
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('ai/', views.ai, name = 'ai'),
    path('products/', views.products, name = 'products'),
    path('cart/', views.cart, name = 'cart'),
    path('profile/', views.profile, name = 'profile'),
    path('contact/', views.contact, name = 'contact'),
    path('', include('store.urls')),
]
