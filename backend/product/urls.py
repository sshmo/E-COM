from django.urls import path
from .views import ListUser, DetailUser, ListProduct, DetailProduct, \
    ListCustomer,DetailCustomer, ListComment, DetailComment


urlpatterns = [
    path('user/<int:pk>/', DetailUser.as_view()),
    path('user', ListUser.as_view()),

    path('product/<int:pk>/', DetailProduct.as_view()),
    path('product', ListProduct.as_view()),

    path('customer/<int:pk>/', DetailCustomer.as_view()),
    path('customer', ListCustomer.as_view()),

    path('comment/<int:pk>/', DetailComment.as_view()),
    path('comment', ListComment.as_view()),
]
