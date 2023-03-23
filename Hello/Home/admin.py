from django.contrib import admin
from Home.models import Contact
from Home.models import Product
from Home.models import Order
from Home.models import OrderItem
from Home.models import ShippingAddress
# from Home.models import Winter
# from Home.models import Summer

# Register your models here.
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
# admin.site.register(Winter)
# admin.site.register(Summer)