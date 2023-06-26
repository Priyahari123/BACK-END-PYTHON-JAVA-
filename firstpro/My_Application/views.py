from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from .models import info
from django.contrib import messages 





# Create your views here.
def home(request):
    data=info.objects.all()
    
    if(data!=''):
        return render(request,"home.html",{'datas':data})
    else:
        return render(request,'home.html')
def read(request):
    if request.method=='POST':
        username=request.POST['Name']
        email=request.POST['Email']
        password=request.POST['password']
        re_password=request.POST['re_password']
        address=request.POST['Address']
       
       
       
        obj=info()
        obj.username=username
        obj.email=email
        obj.password=password
        obj.re_password=re_password
        obj.address=address
        if info.objects.filter(username=username).exists():
            return HttpResponse(username+" Already Exists!!!!!.")    
       
        obj.save()
        data=info.objects.all()
        return redirect("home")
        
    return render(request,"home.html")





