from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    phone = models.CharField(max_length=122)
    text = models.TextField()
    date = models.DateField()
  
    def __str__(self):                  #to change the name in database from "contactobject1" to the name of the user    
        return self.name
    

class Product(models.Model):
    image = models.ImageField(upload_to='products')
    name = models.CharField(max_length=122)
    price =  price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
    

class Order(models.Model):
    customer = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False, null = True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    
class OrderItem(models.Model):
         product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
         order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
         quantity = models.IntegerField(default=0, null=True, blank=True)
         date_added = models.DateTimeField(auto_now_add=True)
         
         @property
         def get_total(self):
             total = self.product.price * self.quantity
             return total
         
         
class ShippingAddress(models.Model):
         customer = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True) 
         order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)   
         address = models.CharField(max_length=200)
         city = models.CharField(max_length=200)
         state = models.CharField(max_length=200)
         zipcode = models.CharField(max_length=200)
         date_added = models.DateTimeField(auto_now_add=True)
         
         def __str__(self):
             return self.address

# class Winter(models.Model):
#     name = models.CharField(max_length=122)
#     description = models.CharField(max_length=200)
#     price = models.CharField(max_length=10)
    
    

# class Summer(models.Model):
#     name = models.CharField(max_length=122)
#     description = models.CharField(max_length=200)
#     price = models.CharField(max_length=10)        
        
        