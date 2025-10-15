from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def render1(req):
    # return render(req,'render1.html')
    # or
    return render(req,'render1.html',context=None)


def render2(req):
    data = {
            'name':"Neeraj",
            'age':37,
            'qualification':"M.Tech"
    }
    # return render(req,'render2.html',data)
    # Or
    return render(req,'render2.html',context=data)


def render3(req):
    data = {
        'name':"Neeraj",
        'age':37,
        'qualification':"M.Tech"
    }
    return render(req,'render3.html',
 {'data':data},content_type='text/HTML',status=201,using=None)
    
    
def render4(req):
    data = {
        'name':"Neeraj",
        'age':37,
        'qualification':"M.Tech"
    }
    return render(req,['render4.html','render3.html'],{'data':data})