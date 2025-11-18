from django.shortcuts import render

# Create your views here.


def landingpage(req):
    return render(req,'landingpage.html')

def home(req):
    return render(req,'home.html')

def contact(req):
    return render(req,'contact.html')

def register(req):
    return render(req,'register.html')

def service(req):
    return render(req,'service.html')

def about(req):
    return render(req,'about.html')

def select(req):
    return render(req,'select.html')

def select1(req):
    y=req.GET.get('selectoption')
    print("Hello....")
    print(req.method)
    print(req.GET)
    print(y)
    
    

def radio(req):
    return render(req,'radio.html')

def radio1(req):
    y=req.GET.get('selectoption')
    print("Hello....")
    print(req.method)
    print(req.GET)
    print(y)