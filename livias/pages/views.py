from itertools import product
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *

# Create your views here.
def home(request):
    products= Shop.objects.all()
    context={
        'products': products,
    }

    return render(request, 'livias.html', context)

def contact(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        message = request.POST['message']

        new_contact = Contact.objects.create(contact_name=name, contact_email=email, contact_phonenumber=phonenumber, message=message)
        return redirect('home')


def shop(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        amount = request.POST['amount']
        image = request.POST['image']

        new_product = Shop.objects.create(product_name=name, product_description=description, product_amount=amount, product_image=image)

    return render(request, '')

def faq(request):
    if request.method == 'POST':
        question = request.POST['question']
        answer = request.POST['answer']

        new_faq = FAQ.objects.create(question=question, answer=answer)

    return render(request, '')

def about(request):
    return render(request, '')


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login(request, user)
            return redirect('dashboard')

        else: 
            return redirect('signin')

    return render(request, 'dashboard/sign-in.html')

def signup(request):
    return render(request, 'dashboard/sign-up.html')

def logout(request):
    return redirect('home')