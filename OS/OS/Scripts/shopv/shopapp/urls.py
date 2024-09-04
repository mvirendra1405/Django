"""
URL configuration for shopv project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

app_name="shopapp"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.home, name='home'),
    path('adduser',v.add_user),
    path('login',v.login_view),
    path('logout',v.logout_view),
    path('productlist',v.product_list,name='product_list'),
    path('cartlist',v.cart_list,name='cart_list'),
    path('addtocart/<int:pk>',v.add_to_cart),
    path('delete/<int:pk>',v.delete_cart.as_view()),
    path('search_product',v.search),
    path('update_cart/<int:item_id>/<str:action>/',v.update_cart,name='update_cart'),
    path('footer/',v.footer),
]
