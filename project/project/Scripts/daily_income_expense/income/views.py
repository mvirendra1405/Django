from django.shortcuts import render,redirect
from .models import Income,IncomeForm

# Create your views here.

def add_income(request):
    if request.method=='POST':
        f=IncomeForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=IncomeForm
        context={'form':f}
        return render(request,'addincome.html',context)
    

def income_list(request):
    incl=Income.objects.all()
    context={'incl':incl}
    return render(request,'incomelist.html',context)
