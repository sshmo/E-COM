"""
This module contains admin models.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from product.models import User, Product, Customer, Comment

admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Comment)