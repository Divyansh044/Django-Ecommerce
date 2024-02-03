from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib import messages

#email import
from django.core.mail import send_mail
from django.conf import settings
from django.core import mail
from django. core.mail.message import EmailMessage

# Create your views here.
def signup(request):

    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Password doest not match")              
            return render(request,'auth/signup.html')
        try:
            if User.objects.get(username=email):
                messages.warning(request,"Email is already Used")
                return render(request,'auth/signup.html')
        
        except Exception as identifier:
            pass
        
        except Exception as identifier:
            pass

        
        myuser=User.objects.create_user(email,email,password)
        myuser.save()
        messages.info(request,"Signup Successfull!!! Please Login")
        return redirect('/divauth/login/')
    
    return render(request,'auth/signup.html')


def login(request):
    if request.method=="POST":
        username=request.POST['email']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username,password=userpassword)

        if myuser is not None:
            auth_login(request,myuser)
            messages.success(request,'Login Success')
            return render(request,'index.html')
        
        else:
            messages.error(request,"Email or password is wrong")
            return redirect('/divauth/login')

    return render(request,'auth/login.html')