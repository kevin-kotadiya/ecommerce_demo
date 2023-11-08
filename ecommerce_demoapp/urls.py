"""ecommerce_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path
from ecommerce_demoapp import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('testimonial/',views.testimonial),
    path('product/',views.product_fun, name='product'),
    path('signinpage/',views.signin_page, name='signin_page'),
    path('signuppage/',views.signup_page, name='signup_page'),
    path('logout/',views.logout1, name='logout'),
    path('cart/',views.cart_page, name='cart_page'),
    path('addtocart/',views.addtocart, name='addtocart'),
    path('change_quantity/',views.change_quantity,name='change_quantity')
]
