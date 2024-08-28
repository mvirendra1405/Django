from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from .models import Product,Cart
from django.contrib.auth.models import User



# Create your views here.

def home(request):
    return render(request,'home.html')

def add_user(request):
    if request.method=='POST':
        f=UserCreationForm(request.POST)
        f.save()
        return redirect('/')

    else:
        f=UserCreationForm
        context={'form':f}
        return render(request,'adduser.html',context)
    

def login_view(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        passw=request.POST.get('password')
        user=authenticate(request,username=uname,password=passw)

        if user is not None:
            request.session['uid']=user.id
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')
    

def logout_view(request):
    logout(request)
    return redirect('/')

def product_list(request):
    pl=Product.objects.all()
    context={'pl':pl}
    return render(request,'productlist.html',context)

def cart_list(request):
    uid=request.session.get('uid')
    cl=Cart.objects.filter(user_id=uid)
    context={'cl':cl}
    return render(request,'cartlist.html',context)

def add_to_cart(request,pid):
    product=Product.objects.get(id=pid)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    c=Cart()
    c.product=product
    c.user=user
    c.save()
    return redirect('/productlist')


    
   

