from django.shortcuts import render, get_object_or_404
from ecomapp.models import Category, Product
from django.core.paginator import Paginator,InvalidPage,EmptyPage

# Create your views here.
def allProdCat(request,c_slug=None):
    c_page=None
    productslst=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        productslst=Product.objects.all().filter(category=c_page,available=True)
    else:
        productslst=Product.objects.all().filter(available=True)
    paginator=Paginator(productslst,6)
    try:
        page=int(request.GET.get('page' ,'1'))
    except:
        page=1
    try:
        product=paginator.page(page)
    except (EmptyPage,InvalidPage):
        product=paginator.page(paginator.num_pages)
    return render(request,'category.html',{'category':c_page,'product':product})
def prodetail(request,c_slug,pro_slug):
    try:
        product=Product.objects.get(category__slug=c_slug,slug=pro_slug)
    except Exception as e:
        raise e
    return render(request,"productdt.html",{'product':product})