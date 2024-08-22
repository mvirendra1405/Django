from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    context={'bal':get_balance(request)}
    return render(request,'home.html',context)

def register_view(request):
    if request.method=='POST':
        f=UserCreationForm(request.POST)
        f.save()
        return redirect('/')

    else:
        f=UserCreationForm
        context={'form':f}
        return render(request,'reg.html',context)
    
from .models import loginform
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
            f=loginform
        context={'form':f}
        return render(request,'login.html',context)



    else:
        f=loginform
        context={'form':f}
        return render(request,'login.html',context)
    

def logout_view(request):
    logout(request)
    return redirect('/')    

from income.models import income
from expense.models import Expense
def get_balance(request):
    uid=request.session.get('uid')
    incl=income.objects.filter(user=uid)
    expl=Expense.objects.filter(user=uid)

    total_income=0
    total_expense=0

    for i in incl:
        total_income=total_income+i.income
    for i in expl:
        total_expense=total_expense+i.expense

    return total_income - total_expense        
    
