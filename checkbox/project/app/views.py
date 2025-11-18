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
    
    
def checkbox(req):
    return render(req,'checkbox.html')

def checkbox1(req):
    y=req.GET.get('selectoption')
    print("Hello....")
    print(req.method)
    print(req.GET)
    print(y)
    
   
   
def form(req):
        return render(req,'form.html')
def formdata(req):
    print("hello")
    # print(req.GET)
    # print(req.POST)
 
    # print(req.FILES)
    # print(req.COOKIES)
    # print(req.META)
    n=req.POST.get('name')
    e=req.POST.get('email')
    m=req.POST.get('number')
    f=req.FILES.get('file')
    i=req.FILES.get('image')
    au=req.FILES.get('audio')
    vi=req.FILES.get('video')
    d=req.POST.get('des')
    print(n)
    print(e)
    print(m)
    print(f)
    print(i)
    print(au)
    print(vi)
    print(d)