from django.shortcuts import render,redirect
from .models import Product,customer
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    data=Product.objects.all()
    return render(request,'homepage.html',{'data':data})
def loginpage(request):
    return render(request,'login.html')
def registration(request):
    return render(request,'registration.html')
def doregistration(request):
    if request.method == 'POST':
        First_name=request.POST['fname']
        Last_name=request.POST['lname']
        Email=request.POST['email']
        password=request.POST['password']
        Cpassword=request.POST['cpassword']
        if password == Cpassword:
            check=User.objects.filter(email=Email)
            if check:
                messages.info(request,'Email Already Exists')
                return redirect(registration)
            data=User()
            data.username=Email
            data.first_name=First_name
            data.last_name=Last_name
            data.email=Email
            data.set_password(password)
            data.save()
            data2=customer()
            data2.user_id=data
            data2.address
            data2.save()
            return redirect('homepage')
        messages.info(request,'Password dosent match')
        return redirect(registration)
    return redirect(registration)
def dologin(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(username=email,password=password)
        if not user:
            messages.info(request,'worng email id or password')
            return redirect('loginpage')
        login(request,user)
        return redirect('homepage')
@login_required(login_url='loginpage')
def cart(request):
    return render(request,'cart.html')
@login_required(login_url='loginpage')
def logout(request):
    auth.logout(request)
    return redirect('loginpage')
@login_required(login_url='loginpage')
def profile(request):
    data=User.objects.get(id=request.user.id)
    data2=customer.objects.get(user_id=request.user.id)
    return render(request,'profile.html',{'data':data,'data2':data2})