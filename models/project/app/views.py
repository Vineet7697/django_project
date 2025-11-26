from django.shortcuts import render,redirect
from .views import *
from app.models import Student
from .forms import StudentForm,LoginForm

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
        # print(form)
        if form.is_valid():
            # print(form.cleaned_data)
            n=form.cleaned_data['name']
            a=form.cleaned_data.get('age')
            print(n,a)
            form.save()
            # return render(req,'landing.html',{'msg':'registration is done'})
            return redirect('login')
        
def login(req):
    lf=LoginForm()
    return render(req,'login.html',{'lform':lf})
    