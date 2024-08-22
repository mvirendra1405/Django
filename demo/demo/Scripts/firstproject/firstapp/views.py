from django.shortcuts import render,HttpResponse,redirect
from .models import emp

# Create your views here.
def home(request):
    return render(request,'home.html')

def addemp(request):
    if request.method=='POST':
        name=request.POST.get('myname')
        email=request.POST.get('myemail')
        contact=request.POST.get('mycontact')
        age=request.POST.get('myage')
        address=request.POST.get('myaddress')
        e=emp()
        
        e.name=name
        e.email=email
        e.contact=contact
        e.age=age
        e.address=address
        e.save()
        return redirect('/')



    else:
        return render(request,'addemp.html')