from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .models import Product,Cart
from django.contrib.auth.models import User
from django.views.generic import DeleteView
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



def add_to_cart(request,pid):
    product_id=Product.objects.get(id=pid)
    uid=request.session.get('uid')
    user_id=User.objects.get(id=uid)
    c=Cart()
    c.Product=product_id
    c.user=user_id
    c.save()
    return redirect('/plist')


def cart_list(request):
    uid=request.session.get('uid')
    user_id=User.objects.get(id=uid)
    cl=Cart.objects.filter(user_id=uid)
    context={'cl':cl}
    return render(request,'cartlist.html',context)

class delete_cart(DeleteView):
    template_name='delete.html'
    model=Cart
    success_url='/cartlist'


def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)  # Example query, modify as needed
    total_bill = 0
    for item in cart_items:
        item.sub_total = item.Product.p_price * item.Product.p_quantity
        total_bill += item.sub_total
    context = {
        'cl': cart_items,
        'total_bill': total_bill,
    }
    return render(request, 'cart.html', context)
