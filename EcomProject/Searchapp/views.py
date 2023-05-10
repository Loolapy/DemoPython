from django.shortcuts import render
from Kite.models import Product
from django.db.models import Q

# Create your views here.

def SearchResult(request):
    product=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        product=Product.objects.all().filter(Q(name__contains=query) | Q(dic__contains=query))
        return render(request,'search.html',{'query':query,'product':product})