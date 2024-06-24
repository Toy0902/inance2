from django.urls import path
from .views import *
urlpatterns =[
    path('',index,name='index'),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('service/', service, name="service"),
    path('index_detel/<int:id>/', index_detel, name="index_detel"),
    ]