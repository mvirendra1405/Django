from django.shortcuts import render
from django.views.generic import FormView,CreateView,ListView,DeleteView,UpdateView

from .models import Emp,Empform
# Create your views here.
def home(request):
    return render(request,'home.html')


class EmpRegister(FormView):
    form_class=Empform
    template_name='addemp.html'


class addemp(CreateView):
    model=Emp
    fields='__all__'
    success_url='/'

class emp_list(ListView):
    model=Emp
    template_name='emplist.html'

class delete1_emp(DeleteView):
    model=Emp
    success_url='/elist'

class delete2_emp(DeleteView):
    template_name='delete.html'
    model=Emp
    success_url='/elist' 

class edit_emp(UpdateView):
    template_name='update.html'
    model=Emp
    fields='__all__'
    success_url='/elist'    