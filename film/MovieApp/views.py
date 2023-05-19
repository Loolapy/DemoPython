from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from MovieApp.forms import Movieform
from MovieApp.models import movie


def index(request):
    films=movie.objects.all()
    context={
        'movie_list':films
    }
    return render(request,"index.html",context)

def detail(request,movie_id):
    films=movie.objects.get(id=movie_id)
    return render(request,"details.html",{'movie':films})
def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        dec=request.POST.get('dec',)
        Year=request.POST.get('Year',)
        img=request.FILES['img']
        films=movie(name=name,dec=dec,Year=Year,img=img)
        films.save()
    return render(request,"add.html")
def update(request,id):
    updateall=movie.objects.get(id=id)
    form=Movieform(request.POST or None, request.FILES,instance=updateall)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        film=movie.objects.get(id=id)
        film.delete()
        return redirect('/')
    return render(request,'delete.html')
