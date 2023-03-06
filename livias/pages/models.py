from django.db import models
from cgitb import text
from email.policy import default
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    contact_name = models.CharField(User, blank=False, null=False, max_length=20) 
    contact_email = models.EmailField(null=False, blank=False)
    contact_phonenumber = models.CharField(max_length = 15)
    message = models.TextField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact_name

class Shop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=20, blank=False, null=False)
    product_description = models.CharField(max_length=15000)
    product_amount = models.IntegerField()
    product_image = models.ImageField(upload_to = 'shop_images')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    
    def __str__(self): 
        return self.product_name

class FAQ(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=80)
    answer = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question