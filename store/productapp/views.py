from django.shortcuts import render,HttpResponse,redirect
from productapp.models import Product
# Create your views here.
def homepage(request):

    return HttpResponse('Hello from Homepage of Productapp')

def add_product(request):
    print("Method Name:",request.method)
    if request.method=="GET":
       print("In if GET section")
       return render(request,'product/store_product.html')
    else:
        #fetch data from form
        name=request.POST['pname']
        amt=request.POST['price']
        qty=request.POST['qty']
        cat=request.POST['cat']
        is_avail=request.POST['avail']
       #validations

       #insert record into table
        p=Product.objects.create(name=name,price=amt,qty=qty,cat=cat,is_available=is_avail)
        #print(p)
        p.save()
        return redirect('/productapp/productdash')
    
def product_dashboard(request):
    context={}
    #fetch data from model or table
    p=Product.objects.all() #select * from productapp_product;
    '''print(p)
    print(p[0])
    print(p[1])
    print("Product Name:",p[0].name)
    print("Product Price:",p[0].price)
    print("Product Name:",p[1].name)
    print("Product Price:",p[1].price)
    print("Using Loop:")
    for x in p:
        print(x)
        print(x.name)
        print(x.price)
        print(x.is_available)'''
    context['products']=p
    return render(request,'product/dashboard.html',context)



def delete_product(request,pid):
    #fetch object to be deleted
    p=Product.objects.filter(id=pid)
    print("Object Deleted:",p)
    #delete object
    p.delete()
    #redirect to dashboard
    return redirect('/productapp/productdash')

def update_product(request,pid):
    p=Product.objects.filter(id=pid)
    if request.method=="GET":
       
        #print(p)
        context={}
        context['product']=p
        #return HttpResponse("Data fetched")
        return render(request,'product/editproduct.html',context)
    else:
        uname=request.POST['pname']
        uprice=request.POST['price']
        uqty=request.POST['qty']
        ucat=request.POST['cat']
        uavail=request.POST['avail']
        p.update(name=uname,price=uprice,qty=uqty,cat=ucat,is_available=uavail)
        return redirect('/productapp/productdash')