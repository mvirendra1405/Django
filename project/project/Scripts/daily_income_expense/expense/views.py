from django.shortcuts import render,redirect
from .models import Expense,expenseform
from django.contrib.auth.models import User
# Create your views here.
def add_expense(request):
    uid=request.session.get('uid')
    if request.method=='POST':
        #f=expenseform(request.POST)
        expense=request.POST.get('expense')
        expense_type=request.POST.get('expense_type')
        expense_date=request.POST.get('expense_date')
        description=request.POST.get('description')
        exp=Expense()
        exp.expense=expense
        exp.expense_type=expense_type
        exp.expense_date=expense_date
        exp.description=description
        exp.user=User.objects.get(id=uid)
        exp.save()
        return redirect('/')
    else:
        f=expenseform
        context={'form':f}
        return render(request,'add_expense.html',context)
    

def expense_list(request):
    # uid=request.session.get('uid')
    # expl=expense.objects.all
    # expl=Expense.objects.filter(user=uid)
    # context={'expl':expl}
    # return render(request,'exp_list.html',context)


    uid=request.session.get('uid')
    expl=Expense.objects.filter(user=uid)
    expt=set()
    for i in expl:
        expt.add(i.expense_type)
    context={'expl':expl,'expt':expt}
    return render(request,'exp_list.html',context)    

def delete_exp(request,expid):
    exp1=Expense.objects.get(id=expid)
    exp1.delete()
    return redirect('/')


def expense_search(request):
    uid=request.session.get('uid')
    srch=request.POST.get('srch')
    expl=Expense.objects.filter(user=uid,description__contains=srch)
    context={'expl':expl}
    return render(request,'exp_list.html',context)

    

def sort_by_expensetype(request,ext2):
    uid=request.session.get('uid')
    expl=Expense.objects.filter(user=uid)
    expt=set()
    for i in expl:
        expt.add(i.expense_type)
        expl=Expense.objects.filter(user=uid,expense_type=ext2)
    context={'expl':expl,'expt':expt}
    return render(request,'exp_list.html',context)
