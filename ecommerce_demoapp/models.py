from django.db import models

# Create your models here.

class user_data(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class product(models.Model):
    image = models.ImageField(upload_to='productimage')
    product_name = models.CharField(max_length=255)
    price = models.BigIntegerField()

class cart(models.Model):
    user_id = models.BigIntegerField()
    product_id = models.BigIntegerField()
    quantity = models.BigIntegerField()
    price = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
