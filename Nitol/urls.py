from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('ai/', views.ai, name='ai'),
    path('products/', views.products, name='products'),
    path('cart/', views.cart_view, name='cart'),
    path('profile/', views.profile, name='profile'),
    path('contact/', views.contact, name='contact'),
    path('', include('store.urls')),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update/<int:product_id>/', views.update_cart, name='update_cart'),
]

# Only when DEBUG=True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
