from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from .models import Product,Cart,Category
from django.contrib.auth.models import User
from django.views.generic import DeleteView
from django.contrib import messages
import razorpay

from django.conf import settings

def home(request):
    products = Product.objects.all() 
    return render(request, 'home.html', {'products': products})



def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
        elif len(password1) < 8:
            messages.error(request, 'Password must be at least 8 characters long')
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This User is already exists')
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                messages.success(request, 'Account created successfully')
                return redirect('/login')
    
    return render(request, 'login.html')
    


def login_view(request):
    if request.method=='POST':
        uname=request.POST.get('username')    
        passw=request.POST.get('password')  
        if not uname or not passw:
            messages.error(request, 'Username and password are required.')
            return render(request, 'login.html')
          
        user=authenticate(request,username=uname,password=passw)
        if user is not None:
            request.session['uid']=user.id
            login(request,user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password.')
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




from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')  
def add_to_cart(request, pid):
    product_id = Product.objects.get(id=pid)
    uid = request.session.get('uid')
    
    if not uid:
        return redirect('/login')
    user_id = User.objects.get(id=uid)
    if Cart.objects.filter(user_id=uid, Product=product_id).exists():
        return redirect('/plist')

    c = Cart()
    c.Product = product_id
    c.user = user_id
    c.save()
    return redirect('/plist')



def cart_list(request):
    uid=request.session.get('uid')
    user_id=User.objects.get(id=uid)
    cl=Cart.objects.filter(user_id=uid)

        

    total_price = sum((item.Product.p_price) * item.quantity for item in cl)
    final_price = total_price * 100

    if final_price < 100:  
        return render(request, 'cartlist.html', {
            'cl': cl,
            'error': 'Order amount is too low. Please add more items to your cart.'
        })

        

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    payment = client.order.create({'amount': final_price, 'currency': 'INR','payment_capture': '1'})
    print(payment)

        

    request.session['razorpay_order_id'] = payment['id']

    context={'cl':cl,'total_price': total_price,
        'final_price': final_price,'razorpay_key_id': settings.RAZORPAY_KEY_ID,
        'razorpay_order_id': payment['id']}
    

    return render(request,'cartlist.html',context)

def update_cart(request, item_id, action):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)

    if action == 'increase':
        cart_item.quantity += 1
    elif action == 'decrease':
        cart_item.quantity -= 1
        if cart_item.quantity < 1:
            cart_item.delete()
            return redirect('/plist')

    cart_item.save()
    return redirect('/cartlist')


class delete_cart(DeleteView):
    template_name='delete.html'
    model=Cart
    success_url='/cartlist'



def product_search(request):
    # uid = request.session.get('uid')
    search = request.POST.get('search')
    pl = Product.objects.filter(p_name__icontains=search)
    context={'pl':pl}
    return render(request,'productlist.html',context)



def product_list(request):
    categories = Category.objects.all()

    category_id = request.GET.get('category')

    if category_id:
        products = Product.objects.filter(Category_id=category_id)
    else:
        products = Product.objects.all()

    context = {
        'pl': products,
        'categories': categories,
        'selected_category': category_id, 
    }


    return render(request, 'productlist.html', context)


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def success_view(request):
    if request.method=='POST':
        a=request.POST
        print(a)
        return render(request,'success.html')
    else:
        return render(request,'success.html')
    
    uid=request.session.get('uid')
    cl=Cart.objects.filter(user_id=uid)
    cl.delete()


