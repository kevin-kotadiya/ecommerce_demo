from django.shortcuts import render,redirect
from .form import*
from django.contrib import messages
from django.contrib.auth import login,logout
from .models import*
from django.contrib import sessions

# Create your views here.

def index(request):
    user=request.session.get('user')
    cart_item = cart.objects.filter(user_id = request.session.get('uid'))
    count = cart_item.count
    return render(request,'index.html',{'user':user,'cart_item':cart_item,'count':count})

def about(request):
    user=request.session.get('user')
    cart_item = cart.objects.filter(user_id = request.session.get('uid'))
    count = cart_item.count
    return render(request,'about.html',{'user':user,'cart_item':cart_item,'count':count})

def contact(request):
    cart_item = cart.objects.filter(user_id = request.session.get('uid'))
    count = cart_item.count
    user=request.session.get('user')
    return render(request,'contact.html',{'user':user,'cart_item':cart_item,'count':count})

def testimonial(request):
    cart_item = cart.objects.filter(user_id = request.session.get('uid'))
    count = cart_item.count
    user=request.session.get('user')
    return render(request,'testimonial.html',{'user':user,'cart_item':cart_item,'count':count})

def product_fun(request):
    cart_item = cart.objects.filter(user_id = request.session.get('uid'))
    count = cart_item.count
    user=request.session.get('user')
    uid=request.session.get('uid')
    products = product.objects.all()
    return render(request,'product.html',{'user':user,'products':products,'uid':uid,'cart_item':cart_item,'count':count})

def signin_page(request):
    if request.method == 'POST':
        emailid = request.POST['email']
        password_u = request.POST['password']
        user = user_data.objects.filter(email=emailid,password=password_u)
        user1 = user_data.objects.get(email = emailid)
        if user:
            request.session['user'] = user1.email
            request.session['uid'] = user1.id
            print('login successs!!')
            return redirect('/')
        else:
            messages.error(request,'Please check email and password.')
            return redirect('signin_page')
            # print('login fail..')
    return render(request,'login.html')

def signup_page(request):
    if request.method == 'POST':
        userdata = user_form(request.POST)
        if userdata.is_valid():
            userdata.save()
            messages.success(request,'SignUp successfully!!')
            return redirect('signin_page')
        else:
            print(userdata.errors)
            messages.error(request,'Please enter valid values!!')
            return redirect('signup_page')
    return render(request,'signup.html')

def logout1(request):
    logout(request)
    return redirect('signin_page')

def cart_page(request):
    cart_item = cart.objects.filter(user_id = request.session.get('uid'))
    count = cart_item.count
    cart1 = {}
    subtotal = []
    for i in cart_item:
        subtotal.append(i.price)
    
    total = sum(subtotal)
    if cart_item:
        for o in cart_item:
            product_item = product.objects.filter(id = o.product_id)
            for j in product_item:
                a = {}
                a['price'] = o.price
                a['image'] = j.image
                a['product_name'] = j.product_name
                a['quantity'] = o.quantity
                a['p'] = j.price
                a['product_id'] = j.id
                cart1[o.id] = a
    else:
        return redirect('product')
    
    user = request.session.get('user')
    uid = request.session.get('uid')
    return render(request,'cart.html',{'user':user,'products':cart1,'total':total,'count':count,'uid':uid})

def addtocart(request):
    if request.method == 'POST':

        chekquantity = cart.objects.filter(user_id = request.session.get('uid'), product_id = request.POST['product_id'])
        if chekquantity:
            quantity_update = cart.objects.get(user_id = request.session.get('uid'),product_id = request.POST['product_id'])
            quantity_update.quantity = int(quantity_update.quantity) + 1
            quantity_update.price = int(quantity_update.price) + int(request.POST['price'])
            quantity_update.save()
        else:
            cart_add = cart_form(request.POST)
            if cart_add.is_valid:
                cart_add.save()
                return redirect("product")
            else:
                print(cart_add.errors)
            # car_obj.user_id = request.session.get('uid')
            # car_obj.product_id = request.POST['productid']

def change_quantity(request):
    if request.method == 'POST':
        cart1 = cart.objects.get(user_id = request.POST['uid'],product_id = request.POST['product'])
        if cart1:
            if int( request.POST['quantity']) == 0:
                cart2 = cart.objects.get(user_id = request.POST['uid'], product_id = request.POST['product'])
                cart2.delete()
            else:
                cart1.quantity = request.POST['quantity']
                price = product.objects.get(id=request.POST['product'])
                cart1.price = int(price.price) * int(request.POST['quantity'])
                cart1.save()
                return redirect('cart_page')
            return redirect('cart_page')

        