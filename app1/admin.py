from django.contrib import admin
from .models import *

# Register your models here.

from .models import Customer, Product, Category, Slider
from shopper.models import Cart, Images, Address, Order, Wishlist


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Slider)
admin.site.register(Cart)
admin.site.register(Images)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(Wishlist)
