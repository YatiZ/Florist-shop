from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request,"home.html",{"web_name":"home page"})

def about_page(request):
    return render(request,"about.html",{"web_name":"about page"})

def contact_page(request):
    return render(request,"contact.html",{"web_name":"contact page"})

def parent_page(request):
    return render(request,"parent.html",{"web_name":"parent page"})