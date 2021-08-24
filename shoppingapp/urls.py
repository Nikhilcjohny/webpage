from django.urls import path

from shoppingapp import views

urlpatterns = [
    path('',views.fun, name='fun')
]
