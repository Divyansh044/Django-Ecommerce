from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request,'auth/signup.html')