from django.shortcuts import render,redirect
from .models import Expense,ExpenseForm

# Create your views here.

def add_expense(request):
    if request.method=='POST':
        f=ExpenseForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=ExpenseForm
        context={'form':f}
        return render (request,'addexpense.html',context)
    
def expense_list(request):
    expl=Expense.objects.all()
    context={'expl':expl}
    return render(request,'expenselist.html',context)
