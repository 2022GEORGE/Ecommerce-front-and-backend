from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
   path('',views.homepage,name='homepage'),
   path('loginpage',views.loginpage,name='loginpage'),
   path('registration',views.registration,name='registration'),
   path('doregistration',views.doregistration,name='doregistration'),
   path('dologin',views.dologin,name='dologin'),
   path('cart',views.cart,name='cart'),
   path('logout',views.logout,name='logout'),
   path('profile',views.profile,name='profile')
]