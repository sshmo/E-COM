"""
This module contains database models.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    """ Users model """
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Product(models.Model):
    """ Products model """

    title = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.01)
    image = models.URLField(max_length=200, default=None, blank=True, null=True)
    categury = models.CharField(max_length=64, default=None, blank=True, null=True)
    stock_number = models.IntegerField()
    creation_time = models.DateTimeField(default=timezone.now)
    watchers = models.ManyToManyField(User, default=None, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.categury})"


class Customer(models.Model):
    """ Customer model """

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_customer")
    purchase_time = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer.first_name} {self.customer.last_name}"


class Comment(models.Model):
    """ Comments model """

    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    comment = models.TextField()
    comment_time = models.DateTimeField(default=timezone.now)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_comment")
    
    def __str__(self):
        return f"{self.id} ({self.comment_time})"