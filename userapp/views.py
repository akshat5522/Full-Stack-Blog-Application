from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from blogapp.models import Blog

def registerView(request):
    if request.method=="POST":
        fname=request.POST.get("firstname")
        lname=request.POST.get("lastname")
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=User.objects.create_user(username=email,first_name=fname,last_name=lname,password=password)
        user.save()
        return redirect("/accounts/login")
    else:
        return render(request, "register.html")

@login_required
def homeView(request):
    blogs=Blog.objects.all() #Blog → your model,objects → Django’s model manager,all() → retrieves every row from the Blog table
    return render(request,"home.html",{"user":request.user,"blogs":blogs})

def loginView(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=authenticate(username=email,password=password)
        if user is not None:
            login(request,user)
            return redirect("/home")
        else:
            return redirect("/accounts/login")
    else:
        return render(request,"login.html")
    
@login_required
def logoutView(request):
    logout(request)
    return redirect("/accounts/login")