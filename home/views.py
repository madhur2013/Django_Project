from multiprocessing import context
from django.shortcuts import render,HttpResponse
from django.contrib import messages
# from datetime import datetime
from home.models import Contact
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
    #return HttpResponse("This is aboutpage")
def welcome(request):
    return HttpResponse("WELCOME")
def services(request):
    context={"variable": " Your Flavoured "}
    messages.success(request, "Your icecraem selected ")
    return render(request,'services.html',context)
    #return HttpResponse("This is Services page")
def contact(request):
    if request.method=="POST":
       name=request.POST.get('name')
       email=request.POST.get('email')
       phone=request.POST.get('phone')
       contact=Contact(name=name,email=email,phone=phone)
       contact.save()
       messages.success(request, "Your Icecream Order has been registered!")
    return render(request,'contact.html')

    #return HttpResponse("This is Contact page")





