from django.shortcuts import render ,redirect
from django.urls import reverse
from django.contrib.auth import (
login , authenticate, get_user ,user_logged_in , logout
)
from .forms import *
from .control import *
from blog.models import Task


# Create your views here.
def registration_view(request):
    print("registration method")
    context ={}
    if request.method=="POST":
        print("request method is Post")
        form =Registration_user_form(request.POST)
        if form.is_valid:
            print("the form is valid")
            form.save()
            return redirect("Account:home")
        else:
            context['form']=form
    else:
        form = Registration_user_form()
        context['form']=form
    return render (request , 'register.html' ,context)


def home_view(request):
    context={}

    return render(request , "index.html" , context=context)


def tasks_view(request):
    context ={}
    return render(request , 'kanban.html' , context=context)




def login_view(request):
    user= request.user
    if user.is_authenticated:
        return redirect('Account:home')

    
    if request.method=="POST":
        email=request.POST['email']
        print('email' ,email)
        raw_password=request.POST['password']
        print('password', raw_password)
        account = authenticate(email=email ,password=raw_password)
        print(account)
        if account:
            print("account is true")
            login(request,account)
            context={'user':account}
            return render(request, 'index.html', context=context)
    else:
        form =AccountAuthenticateForm()
    context={"login_form":form}
    return render(request , "login.html" , context)


def tasks_view(request):
    '''  'account/' this is a view of main page  '''
    context={}
    user = request.user
    
    if user.is_authenticated:
        context['user']=user
        
        return render (request, 'kanban.html' , {})
    else:
        return render(request ,'index.html' , context={})
    

def log_out(request):

    
    print("log out")
    logout(request)
    return redirect('Account:home')