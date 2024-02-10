from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib import messages
from django.views.generic import View
#email import
from django.core.mail import send_mail
from django.conf import settings
from django.core import mail
from django. core.mail.message import EmailMessage


# to acitvate the user accounts
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.urls import NoReverseMatch,reverse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
#getting tokens from utlis.py
from .utils import TokenGenerator,generate_token


#emails
from django.core.mail import send_mail,EmailMultiAlternatives
from django.core.mail import BadHeaderError,send_mail 
from django.core import mail
from django.conf import settings
from django.core.mail import EmailMessage

# Create your views here.


#Threading
import threading
class EmailThread(threading.Thread):

    def __init__(self,email_message):
        self.email_message=email_message
        threading.Thread.__init__(self)

    def run(self):
        self.email_message.send()


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

        
        user=User.objects.create_user(email,email,password)
        user.is_active=False
        user.save()
        current_site=get_current_site(request)
        email_subject="Activate your account"
        message=render_to_string('auth/activate.html',{
            'user':user,
            'domain':'127.0.0.1:8000',
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user)
        })

        email_message=EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email],)

        EmailThread(email_message).start()

        messages.info(request,"Activate Your account by Clicking Link on Your Email")
        return redirect('/divauth/login/')
    
    return render(request,'auth/signup.html')


class ActivateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifier:
            user=None

        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.info(request,"Account activated successfully!!!!")
            return redirect('/divauth/login')
        return render(request,'auth/activate_fail.html')


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