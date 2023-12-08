from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Product,customer,CartItem
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    data=Product.objects.all()
    c=CartItem.objects.filter(user=request.user.id)
    c1=c.count()
    return render(request,'homepage.html',{'data':data,'c':c1})
def loginpage(request):
    return render(request,'login.html')
def registration(request):
    return render(request,'registration.html')
def doregistration(request):
    if request.method == 'POST':
        First_name=request.POST['fname']
        Last_name=request.POST['lname']
        Email=request.POST['email']
        address=request.POST['address']
        locality=request.POST['locality']
        pin=request.POST['postoffice']
        password=request.POST['password']
        Cpassword=request.POST['cpassword']
        if password == Cpassword:
            check=User.objects.filter(email=Email)
            if check:
                messages.warning(request,'Email Already Exists')
                return redirect('registration')
            data=User()
            data.username=Email
            data.first_name=First_name
            data.last_name=Last_name
            data.email=Email
            data.set_password(password)
            data.save()
            data2=customer()
            data2.user_id=data
            data2.address=address
            data2.locality=locality
            data2.pin=pin
            data2.save()
            messages.success(request,'Registration success full')
            return redirect('registration')
        messages.error(request,'Password dosent match')
        return redirect('registration')
    return redirect('registration')
def dologin(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(username=email,password=password)
        if not user:
            messages.error(request,'invalid login')
            return redirect('loginpage')
        login(request,user)
        messages.success(request,'Login successfull')
        return redirect('homepage')
@login_required(login_url='loginpage')
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user.id)
    total_price = sum(item.product.tprice * item.quantity for item in cart_items)
    data3=sum(item.product.price * item.quantity for item in cart_items)
    return render(request,'cart.html',{'data':cart_items,'data2':total_price,'data3':data3})
@login_required(login_url='loginpage')
def logout(request):
    auth.logout(request)
    return redirect('loginpage')
@login_required(login_url='loginpage')
def profile(request):
    data=User.objects.get(id=request.user.id)
    data2=customer.objects.get(user_id=request.user.id)
    return render(request,'profile.html',{'data':data,'data2':data2})
@login_required(login_url='loginpage')
def add_to_cart(request, pk):
    product = Product.objects.get(id=pk)
    cart_item ,created= CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect(homepage)
@login_required(login_url='loginpage')
def remove_from_cart(request,pk):
    cart_item = CartItem.objects.get(id=pk)
    cart_item.delete()
    return redirect('cart')
@login_required(login_url='loginpage')
def add(request,pk):
    data=CartItem.objects.get(id=pk)
    data.quantity=data.quantity+1
    data.save()
    return redirect('cart')
@login_required(login_url='loginpage')
def less(request,pk):
    data=CartItem.objects.get(id=pk)
    data.quantity=data.quantity-1
    data.save()
    if data.quantity == 0:
        data.delete()
    return redirect('cart')
@login_required(login_url='loginpage')
def makepayment(request):
    data=customer.objects.get(user_id=request.user.id)
    data2=CartItem.objects.filter(user=request.user.id)
    totalprice=sum(i.product.price*i.quantity for i in data2)
    return render(request,'makepayment.html',{'data':data,'data2':data2,'tp':totalprice})
def do_payment(request):
    if request.method == 'POST':
        card=request.POST['card']
        cvv=request.POST['cvv']
        data=CartItem.objects.filter(user=request.user.id)
        data.delete()
        messages.success(request,'order succesfull')
        return redirect('homepage')
    return redirect('makepayment')
def payment(request):
    return render(request,'payment.html')
def view_item(request,pk):
    return render(request,'view_item.html')