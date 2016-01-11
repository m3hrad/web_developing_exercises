from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render
from webshop.models import Product

def starting_instructions(request):
    return render(request, "webshop/instructions.html", {})

def about(request):
    return HttpResponse("about page")

def productview(request, product_id):
    """
    Write your view implementations for exercise 4 here.
    Remove the current return line below.
    """
    try:
        product = Product.objects.get(pk=product_id)
    except:
        return HttpResponseNotFound("product doesn't exist");
    context = {'product': product}
    return render(request,"webshop/product_view.html", context)

def available_products(request):
    """
    Write your view implementations for exercise 4 here.
    Remove the current return line below.
    """
    products = Product.objects.filter(quantity__gt = 0)
    context = {'products': products}
    return render(request,"webshop/product_list.html",context)
