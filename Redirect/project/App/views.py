from django.shortcuts import render,redirect
from django.http import HttpResponsePermanentRedirect,HttpResponseRedirect

# Create your views here.


def home(request): 
    return redirect('about') # redirects to URL pattern named 'about'


def about(req):
     return redirect('https://www.facebook.com/')
 
 

def redirect1(req):
     return redirect('https://www.google.com/')
 
def redirect3(req):
    return redirect('/redirect4/')

def redirect4(req):
    return redirect('https://www.facebook.com/')


def redirect5(req):
    return redirect('redirect6',name='python language'),


def redirect6(req,name):
    return render(req,'redirect.html',{'id':name})

def redirect7_permanently(request): 
    return HttpResponsePermanentRedirect('/redirect4/') # for 301 redirects
    # return redirect('/redirect4/', permanent=True)
