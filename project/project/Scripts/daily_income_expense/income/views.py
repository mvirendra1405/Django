from django.shortcuts import render,redirect
from .models import income,incomeform
from django.contrib.auth.models import User
# Create your views here.
def add_income(request):
    uid=request.session.get('uid')
    if request.method=='POST':
        #f=incomeform(request.POST)
        incomee=request.POST.get('income')
        incomee_type=request.POST.get('income_type')
        incomee_date=request.POST.get('income_date')
        description=request.POST.get('description')
        inc=income()
        inc.income=incomee
        inc.income_type=incomee_type
        inc.income_date=incomee_date
        inc.description=description
        inc.user=User.objects.get(id=uid)
        inc.save()
        return redirect('/')
    else:
        f=incomeform
        context={'form':f}
        return render(request,'add_income.html',context)
    

def income_list(request):
    # uid=request.session.get('uid')
    # #incl=income.objects.all
    # incl=income.objects.filter(user=uid)
    # context={'incl':incl}
    # return render(request,'inc_list.html',context)

    uid=request.session.get('uid')
    incl=income.objects.filter(user=uid)
    inct=set()
    for i in incl:
        inct.add(i.income_type)
    context={'incl':incl,'inct':inct}
    return render(request,'inc_list.html',context)    


def delete_inc(request,inid):
    inc=income.objects.get(id=inid)
    inc.delete()
    return redirect('/')



def income_search(request):
    uid=request.session.get('uid')
    srch=request.POST.get('srch')
    incl=income.objects.filter(user=uid,description__contains=srch)
    context={'incl':incl}
    return render(request,'inc_list.html',context)



def sort_by_incometype(request,inct2):
    uid=request.session.get('uid')
    incl=income.objects.filter(user=uid)
    inct=set()
    for i in incl:
        inct.add(i.income_type)
        incl=income.objects.filter(user=uid,income_type=inct2)
    context={'incl':incl,'inct':inct}
    return render(request,'inc_list.html',context)



