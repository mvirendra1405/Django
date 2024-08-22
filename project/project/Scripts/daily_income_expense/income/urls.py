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
    path('addincome',v.add_income,name='addinc'),
    path('incomelist',v.income_list,name='inclist'),
    path('delete/<int:inid>',v.delete_inc),
    path('income_search',v.income_search,name='income_search'),
    path('income/<str:inct2>',v.sort_by_incometype,name='inct1')
    
    
]