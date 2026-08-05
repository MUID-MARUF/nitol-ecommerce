from django.db import models
import os
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# -----------------------------
# Product Image Rename Function
# -----------------------------
def product_image_path(instance, filename):
    ext = filename.split('.')[-1]
    name = instance.name.replace(" ", "_").lower()
    unique = uuid.uuid4().hex[:5]
    filename = f"{name}_{unique}.{ext}"
    return os.path.join('products/', filename)


# -----------------------------
# Product Model
# -----------------------------
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to=product_image_path)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# -----------------------------
# Category Model
# -----------------------------
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# -----------------------------
# Profile Model (NEW)
# -----------------------------
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username


# -----------------------------
# Auto Create Profile
# -----------------------------
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()