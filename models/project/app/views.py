from django.shortcuts import render
from .views import *
from app.models import Student
from .forms import StudentForm

# Create your views here.

def landing(req):
    fm=StudentForm()
    return render (req,'newform.html',{'form':fm})

def register(req):
    return render(req,'register.html')

def registerData(req):
    n=req.POST.get('name')
    a=req.POST.get('age')
    Student.objects.create(name=n,age=a)
    return render (req,'register.html')
     

def savedata(req):
    if req.method=='POST':
        form=StudentForm(req.POST or None)
        print(form)