from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from .models import Addprofile



# Create your views here.
def home(request):
    data=Addprofile.objects.all()
    return render(request,"home.html",{'data':data})


def register(request):
    if request.method == "POST":
        Name=request.POST['Name']
        email_id=request.POST['email_id']
        password=request.POST['password']
        password1=request.POST['password1']

        obj=Addprofile()
        obj.Name=Name
        obj.email_id=email_id
        obj.password=password
        obj.password1=password1
        if password == password1:
            if Addprofile.objects.filter(Name=Name).exists():
                
                messages.warning(request,'Username already exists !!!')
                return redirect("login")
            obj.is_staff=True
            obj.is_superuser =True
            obj.save()
            data=Addprofile.objects.all()
            messages.success(request,'Your account hasbeen succesfully created!!!')
            return redirect('login')
        else:
            messages.warning(request,'Password Mismatching!!!')
            return redirect('register')
           
       


    return render(request,"register.html")

def profile(request):
    return render(request,"profile.html")
    




