from django.urls import path

from . import views

app_name = 'checkout'
urlpatterns = [
    path('', views.order_placed, name='checkout'),
    path('paid/',views.paid , name='paid'), 
    ]
