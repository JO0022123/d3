from django.shortcuts import render,redirect
from .models import *
from .form import detailsfrom,createForm
from django.contrib import messages
from django.db.models import Q 
from django.contrib.auth import login as auth_login,authenticate,logout as auth_logout
# Create your views here.
def home(request):
    search_post = request.GET.get('search')
    if search_post:
       posts = product_cards.objects.filter(Q(name__icontains=search_post) & Q(category__icontains=search_post))
    else:
    # If not searched, return default posts
       posts = product_cards.objects.all().order_by("-created_at")
    return render(request,"index.html",{"posts":posts})
def about(request):
    stu=student.objects.all()
    return render(request,"about.html",{"stu":stu})
def adddata(request):
    if request.method=="POST":
        email=request.POST['email']
        name=request.POST['name']
        ph=request.POST['ph']
        obj=student.objects.create(email=email,name=name,ph=ph)
        obj.save()
        return redirect("about/")
    else:
        return render(request,"reg/reg.html")
def delete(request,pk):
    c=student.objects.filter(id=pk)
    c.delete()
    return redirect("about")
def edit(request,id):
    obj=student.objects.get(id=id)
    return render(request,"reg/edit.html",{"obj":obj})
def update(request,id):
    obj=student.objects.get(id=id)
    form=detailsfrom(request.POST,instance=obj)
    if form.is_valid:
        form.save()
        obj=student.objects.all()
        return redirect("about")
    return render(request,"reg/edit.html",{"obj":obj})
def card(request):
    cat=product_cards.objects.all()
    return render(request,"card/card.html",{"cat":cat})
def logout(request):
  if request.user.is_authenticated:
    auth_logout(request)
    messages.success(request,"Logged out Successfully")
  return redirect("/")
def signup(request):
     form=createForm()
     if request.method=='POST':
         form=createForm(request.POST)
         if form.is_valid():
             form.save()
             messages.success(request,"reg success!")
             return redirect('login')
     return render(request,'account/reg.html',{'form':form})
def login(request):
    '''if request.user.is_authenticated:
        return redirect("/")
    else:'''
    if request.method=='POST':
        name=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(username=name,password=pwd)
        if user is not None:
            auth_login(request,user)
            messages.success(request,"login successs!")
            return redirect('/')
        else:
            messages.error(request,"invaild username and password")
            redirect('/login')

    return render(request,"account/login.html")
def productlog(request):
    product=Product.objects.all()
    return render(request,"card/product.html",{'product':product})
def product_details(request,pname):
     if(product_cards.objects.filter(name=pname,status=0)):
            products=product_cards.objects.filter(name=pname,status=0).first()
            return render(request,"card/product.html",{"products":products})
     else:
            messages.error(request,"No Such Produtct Found")
            return redirect('card')
def offer(request):
    offer=product_cards.objects.filter(trending=1)
    return render(request,"card/offer.html",{"offer":offer})
def cart_page(request):
  if request.user.is_authenticated:
    cart1=Carts.objects.filter(user=request.user)
    total_price = sum(item.product.selling_price * item.product_qty for item in cart1)
    return render(request,"card/add_card.html",{"cart1":cart1,'total_price': total_price})
  else:
    return redirect("/")
def add_to_cart(request, product_id):
    product = product_cards.objects.get(id=product_id)
    cart_item, created = Carts.objects.get_or_create(product=product,user=request.user)
    cart_item.product_qty += 1
    cart_item.save()
    return redirect('cart_page')
def remove_from_cart(request, item_id):
    cart_item = Carts.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart_page')


