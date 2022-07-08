from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


def createCustomer(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:

        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for' + username)
                return redirect('/loginpage')


        context={'form':form}
        return render(request,'register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('Home')
            else:
                messages.info(request, "Username or Password is INCORRECT")

        context={}
        return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('Login')


@login_required(login_url='Login')
def Home(request):
    return render(request,'index.html')




@login_required(login_url='Login')
def Cart(request):
    orders = Order.objects.all()
    context = {'orders':orders}


    return render(request,'cart.html', context)

@login_required(login_url='Login')
def CreateOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        status = "Pending"
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cart')

    context = {'form':form}
    return render(request,'order.html', context)

@login_required(login_url='Login')
def CreateReview(request):
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/review')

    context = {'form':form}
    return render(request,'reviewform.html', context)

@login_required(login_url='Login')
def Products(request):
    products = Product.objects.all()

    context = {'products':products}
    return render(request,'products.html', context)

@login_required(login_url='Login')
def ReviewPage(request):
    reviews = Review.objects.all()

    context = {'reviews':reviews}
    return render(request,'review.html', context)


def OwnerLogin(request):

    return render(request,'ownerlogin.html')

def OwnerDashboard(request):
    order = Order.objects.all()
    product = Product.objects.all()
    product_count = product.count()
    order_count = order.count()
    delivered = order.filter(status='Delivered').count()
    pending = order.filter(status='Pending').count()

    context = {'count':order_count, 'delivered_count':delivered,'pending_count':pending, 'product_count':product_count}

    return render(request,'owner1.html',context)

def OwnerProduct(request):
    products = Product.objects.all()

    context = {'products':products}
    return render(request,'owner2.html', context)

def OwnerOrder(request):
    order = Order.objects.all()


    context = {'order':order}
    return render(request,'owner3.html', context)

def AddProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ownerproduct')

    context = {'form':form}
    return render(request,'addproduct.html', context)

def UpdateProduct(request,pk):

    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('/ownerproduct')

    context = {'form':form}
    return render(request,'addproduct.html', context)

def DeleteProduct(request,pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('/ownerproduct')
    context = {'item':product}
    return render(request,'deleteProduct.html', context)

def UpdateOrder(request,pk):

    order = Order.objects.get(id=pk)
    form = UpdateFormOrder(instance=order)

    if request.method == 'POST':
        form = UpdateFormOrder(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/ownerorder')

    context = {'form':form}
    return render(request,'addproduct.html', context)

def DeleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/ownerorder')
    context = {'item':order}
    return render(request,'deleteOrder.html', context)

