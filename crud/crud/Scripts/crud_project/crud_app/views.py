from django.shortcuts import render,redirect
from .models import Emp,Empform,Account,Accountform

# Create your views here.
def home(request):
    return render(request,'home.html')

def addemp(request):
    if request.method=='POST':
        f=Empform(request.POST)
        f.save()
        return redirect('/')
    else:
        f=Empform
        context={'form':f}
        return render(request,'addemp.html',context)
    
def addaccount(request):
    if request.method=='POST':
        f=Accountform(request.POST)
        f.save()
        return redirect('/')
    else:
        f=Accountform
        context={'form':f}
        return render(request,'addaccount.html',context)
    

def emplist(request):
    emp1=Emp.objects.all()
    context={'elist':emp1}
    return render(request,'emplist.html',context)    


def delete1_emp(request):
    eid=request.GET.get('id')
    emp=Emp.objects.get(id=eid)
    emp.delete()
    return redirect('/elist')



def delete2_emp(request,eid):
    emp=Emp.objects.get(id=eid)
    emp.delete()
    return redirect('/elist')


def edit_emp(request,eid):
    emp=Emp.objects.get(id=eid)
    if request.method=='POST':
        f=Empform(request.POST,instance=emp)
        f.save()
        return redirect('/elist')
    else:
        f=Empform(instance=emp)
        context={'form':f}
        return render(request,'addemp.html',context)
    

def acc_details(request):
    acc=Account.objects.all()
    context={'alist':acc}
    return render(request,'acc.html',context)