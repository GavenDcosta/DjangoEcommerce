from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
  path('', views.home, name='weather'),
  path('home', views.about, name='home'),
  path('about', views.about, name='about'),
  path('services', views.services, name='services'),
  path('contact', views.contact, name='contact'),
  path('contact', views.contact, name='contact'),
  path('login', views.loginUser, name='login'),
  path('logout', views.logoutUser, name='logout'),
  path('register', views.register, name='register'),
  path('registerUser', views.registerUser, name='registerUser'),
  path('category/<str:value>',views.category,name="Seasons"),
  path('cart', views.cart, name='cart'),
  path('checkout', views.checkout, name='checkout'),
  path('update_item', views.updateItem, name='update_item')
]
