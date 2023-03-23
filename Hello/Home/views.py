from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from Home.models import Contact
from django.contrib import messages  #django messages framework
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from .models import *
from django.http import JsonResponse
import json

# Create your views here.
def index(request):
     if request.user.is_anonymous:
         return render(request, 'login.html')
     else:
        order, created = Order.objects.get_or_create(customer=request.user, completed=False)     #to create an order or check if it already exists,...Creating an object or quering one
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items           
        context = {
            'items': items,
            'order':order,
            'cartItems':cartItems
            }
        return render(request, 'about.html', context)
        
    
def home(request):
        return render(request, 'weather.html')    

def about(request):
    if request.user.is_anonymous:
        return render(request, 'login.html')
    else:
        return render(request, 'about.html')


def checkout(request):
    if request.user.is_anonymous:
        return render(request, 'login.html')
    else:
        return render(request, 'checkout.html')    

def services(request):
    if request.user.is_anonymous:
        return render(request, 'login.html')
    else:
        return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        text = request.POST.get('text')
        contact = Contact(name=name, email=email, phone=phone, text=text, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been sent!')
    if request.user.is_anonymous:
        return render(request, 'login.html')
    else:
        return render(request, 'contact.html')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect("/home")
            
        else:    
            messages.error(request, 'User does not exist')
            return render(request, 'login.html')
            
    return render(request, 'login.html')
 

def logoutUser(request):
    logout(request)
    messages.success(request, 'Successfully Logged out')
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def registerUser(request):
   if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')    
        
        user = User.objects.create_user(username, email, password)
        user.save()
        messages.success(request, 'Registeration successful')
        return render(request, 'login.html')
   else:
        messages.error(request, 'Something went wrong')
        return render(request, 'login.html')   
        
        
        
def category(request, value):
    cards=Product.objects.filter(category=value) 
    context = {
        "data": cards,
    }
    if request.user.is_anonymous:
        return render(request, 'login.html')
    else:
        return render(request, 'index.html', context)    
       
        
        
        
def cart(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(customer=request.user, completed=False)     #to create an order or check if it already exists,...Creating an object or quering one
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items           
        context = {
            'items': items,
            'order':order,
            'cartItems':cartItems
            }
        return render(request, 'cart.html', context)    
    else:
        return render(request, 'login.html')
    
    
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    print('Action', action)
    print('productId', productId)
    
    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=request.user, completed=False)
    
    orderItem, create = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)    
    
    orderItem.save()    
    
    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse('Item was added', safe=False)    
             
# def index (request):
    
#     a=Product.objects.filter(category="Monsoon")
#     if request.user.is_authenticated:
#         cart, created = Cart.objects.get_or_create(user=request.user, completed=False)    
#     # context = {"products":product, "cart": cart}
#     return render(request,'index.html',{'objects':a})

# def home(request):
#     return redirect('index')        