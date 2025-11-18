from django.shortcuts import render

# Create your views here.    
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
    
def radio(req):
    return render(req,'radio.html')

def radio1(req):
    print("hello !!!!!!!!")