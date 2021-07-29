from akash import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("",views.index, name='akash'),
    path("about",views.about, name='about'),
    path("Service",views.Service, name='Service'),
    path("contact",views.contact, name='contact') 

]