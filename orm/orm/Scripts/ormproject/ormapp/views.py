from django.shortcuts import render,redirect
from .models import empform

# Create your views here.
def home(request):
    return render(request,'home.html')

def addemp(request):
    if request.method=='POST':
        f=empform(request.POST)
        f.save()
        return redirect('/')

    else:
        f=empform
        context={'form':f}
        return render(request,'addemp.html',context)