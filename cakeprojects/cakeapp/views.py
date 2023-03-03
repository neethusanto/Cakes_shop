from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CakeForm
from.models import Cake

# Create your views here.

def home(request):
    cake=Cake.objects.all()
    context={
        'cake_list':cake
    }
    return render(request,'home.html',context)

def details(request,cake_id):
    cake=Cake.objects.get(id=cake_id)
    return render(request,'detail.html',{'cake':cake})

def add_cake(request):
    if request.method=='POST':
        cake_name=request.POST.get('cake_name',)
        cake_flavour=request.POST.get('cake_flavour',)
        cake_desc=request.POST.get('cake_desc',)
        cake_price = request.POST.get('cake_price',)
        cake_img = request.FILES['cake_img']
        cake=Cake(cake_name=cake_name,cake_flavour=cake_flavour,cake_desc=cake_desc,cake_price=cake_price,cake_img=cake_img)
        cake.save()

    return render(request,'add.html')

def update(request,id):
    cake=Cake.objects.get(id=id)
    form=CakeForm(request.POST or None,request.FILES,instance=cake)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'cake':cake})



def delete(request,id):
    if request.method=='POST':
        cake=Cake.objects.get(id=id)
        cake.delete()
        return redirect('/')
    return render(request,'delete.html')

