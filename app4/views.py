from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"app4/home.html")

def profile(request):
    name="rocky"
    return render(request,"app4/profile.html",{'name':name})
