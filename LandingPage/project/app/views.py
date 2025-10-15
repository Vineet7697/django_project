from django.shortcuts import render

# Create your views here.


def landingpage(req):
    return render(req,'landingpage.html')

def home(req):
    return render(req,'home.html')