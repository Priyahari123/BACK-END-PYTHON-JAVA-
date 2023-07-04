from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout



# Create your views here.
def home(request):
    return render(request,"home.html")


def register(request):
    if request.method == "POST":
        Name=request.POST['Name']
        email_id=request.POST['email_id']
        password=request.POST['password']
        password1=request.POST['password1']
        if password == password1:
            user=User.objects.create_user(username=Name,email=email_id,password=password1)
            user.is_staff = True
            user.is_superuser =True
         
            user.save()
            messages.success(request,'Your account hasbeen succesfully created!!!')
            return redirect('login')
            
        else:
            messages.warning(request,'Password Mismatching!!!')
            return redirect('register')
            


    return render(request,"register.html")

def profile(request):
    return render(request,"profile.html")




