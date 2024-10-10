from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from .models import Product,Cart,Category
from django.contrib.auth.models import User
from django.views.generic import DeleteView
from django.shortcuts import get_object_or_404
import razorpay
from django.contrib import messages

 

# Create your views here.

def home(request):
    return render(request,'home.html')

def add_user(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():  # Check if the form data is valid
            f.save()
            return redirect('/')  # Redirect on successful save
        else:
            context = {'form': f}  # Return form with errors if invalid
            return render(request, 'adduser.html', context)
    else:
        f = UserCreationForm()  # Create a new blank form in GET request
        context = {'form': f}
        return render(request, 'adduser.html', context)


def login_view(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')
        
        # Check if username and password are provided
        if not uname or not passw:
            messages.error(request, 'Username and password are required.')
            return render(request, 'login.html')

        # Authenticate user
        user = authenticate(request, username=uname, password=passw)

        if user is not None:
            # User is authenticated, login the user
            request.session['uid'] = user.id
            login(request, user)
            return redirect('/')
        else:
            # Invalid username or password
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html')

    # GET request - render the login page
    return render(request, 'login.html')
    

def logout_view(request):
    logout(request)
    return redirect('/')

def product_list(request):
    pl=Product.objects.all()
    context={'pl':pl}
    return render(request,'productlist.html',context)

# def cart_list(request):
#     uid=request.session.get('uid')
#     cl=Cart.objects.filter(user_id=uid)
#     context={'cl':cl}
#     return render(request,'cartlist.html',context)

def cart_list(request):
    uid = request.session.get('uid')
    print(uid)
    if uid is None:
        return redirect('/login')  # Replace with your actual login view name
    cl = Cart.objects.filter(user_id=uid)
    #context = {'cl': cl}
    # return render(request, 'cartlist.html', context)
   

    total_price = sum((item.product.p_price) * item.quantity for item in cl)
    final_price = total_price

    if final_price < 100:  
        return render(request, 'cartlist.html', {
            'cl': cl,
            'error': 'Order amount is too low. Please add more items to your cart.'
        })

        

    # client = razorpay.Client(auth=("rzp_test_XfueALcdrR7zEP", "UNIDFx61y6jBZ60L0aSp7Icy"))
    # payment = client.order.create({'amount': final_price, 'currency': 'INR','payment_capture': '1'})
    # print(payment)


        

    #request.session['razorpay_order_id'] = payment['id']

    # context={'cl':cl,'total_price': total_price,
    #     'final_price': final_price,'razorpay_key_id': "rzp_test_XfueALcdrR7zEP",
    #     'razorpay_order_id': payment['id']}
    context={'cl':cl,'total_price': total_price,'final_price': final_price,}
    
    return render(request, 'cartlist.html', context)
    

# def add_to_cart(request,pid):
#     product_id=Product.objects.get(id=pid)
#     uid=request.session.get('uid')
#     user_id=User.objects.get(id=uid)
#     c=Cart()
#     c.product=product_id
#     c.user=user_id
#     c.save()
#     return redirect('/productlist')

# def make_payment(request):
#     import razorpay
#     client = razorpay.Client(auth=("rzp_test_6HxFKNC4hD5eAz", "gljUGx4CR2UfT4zYHNzJjTOy"))

#     data = { "amount": 500, "currency": "INR", "receipt": "order_rcptid_11" }
#     payment = client.order.create(data=data)
#     return render(request, 'pay.html')

def make_payment(request):
    client = razorpay.Client(auth=("rzp_test_FwqkwlgBJIT19m","CZNQOcqUo57esCotfMg2C7P0"))
    
    data = {"amount": 500, "currency": "INR", "receipt": "order_rcptid_11"}
    try:
        payment = client.order.create(data=data)
        return render(request, 'pay.html', {'payment': payment})  # Pass payment info to template
    except Exception as e:
        # Handle error (logging, user notification, etc.)
        return render(request, 'error.html', {'error': str(e)})

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if not request.user.is_authenticated:
        
        return render(request,'msg.html')
    # Logic to add product to the cart
    cart_item, created = Cart.objects.get_or_create(product=product, user=request.user)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('shopapp:cart_list')

def search(request):
    srch=request.POST.get('srch')
    pl=Product.objects.filter(p_name__contains=srch)
    context={'pl':pl} 
    return render(request,"productlist.html",context)

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

class delete_cart(DeleteView):
    template_name='delete.html'
    model=Cart
    success_url=('/cartlist')

# def cart_view(request):
#     cart_items = Cart.objects.filter(user=request.user)
#     total_bill = 0
    
#     for item in cart_items:
#         item.sub_total = item.product.p_price * item.quantity  # Corrected attribute access
#         total_bill += item.sub_total
    
#     context = {
#         'cl': cart_items,
#         'total_bill': total_bill,
#     }
#     return render(request, 'cart.html', context)


def update_cart(request, item_id, action):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    
    if action == 'increase':
        cart_item.quantity += 1
        cart_item.save()
    elif action == 'decrease':
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()  # Save only when the quantity is decreased and not deleted
        else: 
            cart_item.delete()  # Delete the cart item if quantity is 1 or less

    return redirect('/cartlist')




def footer(request):
    return render(request,'footer.html')


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def success_view(request):
    if request.method=='POST':
        a=request.POST
        print(a)
        return render(request,'success.html')
    else:
        return render(request,'success.html')
    
    






