"""
URL configuration for daily_income_expense project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addexpense',v.add_expense,name='addexp'),
    path('expenselist',v.expense_list,name='explist'),
    path('delete1/<int:expid>',v.delete_exp),
    path('expense_search',v.expense_search,name='expense_search'),
    path('exp/<str:ext2>',v.sort_by_expensetype,name='ext1')
    
]
