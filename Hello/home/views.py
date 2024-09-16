from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    context={
        'variable1':'Sachin gupta',
        'variable2':'Rohan kamble'
    }
    return render(request,'index.html',context)

def index2(request):
    return render(request,'index2.html')

def about(request):
    return render(request,'about.html')
    # return HttpResponse("this is about page")

def services(request):
    return render(request,'services.html')
    # return HttpResponse("this is services page")

def contact(request):
    if request.method=="POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        phone =request.POST.get('phone')
        desc =request.POST.get('desc')
        print(name)

        contact = Contact(name =name,email=email,phone_no=phone,desc=desc)
        contact.save()
        messages.success(request, "Your message is sucessfully saved")
    return render(request,'contact.html')

def display(request):
    return HttpResponse("This is display Page")
