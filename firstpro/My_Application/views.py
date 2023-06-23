from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import info

# Create your views here.
def home(request):
    data=info.objects.all()
    if(data!=''):
        return render(request,"home.html",{'datas':data})
    else:
        return render(request,'home.html')
def read(request):
    if request.method=='POST':
        name=request.POST['Name']
        email=request.POST['Email']
        address=request.POST['Address']
        obj=info()
        obj.name=name
        obj.email=email
        obj.address=address
        obj.save()
        data=info.objects.all()
        return redirect('home')
    return render(request,"home.html")
