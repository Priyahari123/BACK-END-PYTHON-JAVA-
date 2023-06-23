from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import information

# Create your views here.
def home(request):
    collect=information.objects.all()
    if(collect!=''):
        return render(request,'home.html',{'mydata':collect})
    else:
        return render(request,'home.html')
def readata(request):
    if request.method=='POST':
        name=request.POST['name']
        phno=request.POST['phno']
        email=request.POST['email']
        obj=information()
        obj.Name=name
        obj.Phno=phno
        obj.Email=email
        obj.save()
        collect=information.objects.all()
        return redirect('home')
    return render(request,'home.html')
    
