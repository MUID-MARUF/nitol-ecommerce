from django.db import models
import os
import uuid

#Rename the product image filename respective to products title
def product_image_path(instance, filename):
    ext = filename.split('.')[-1]

    # clean name
    name = instance.name.replace(" ", "_").lower()

    # unique id
    unique = uuid.uuid4().hex[:5]

    filename = f"{name}_{unique}.{ext}"

    return os.path.join('products/', filename)

#Product Table 
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to=product_image_path)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#Category Model
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name