from django.shortcuts import render

from .models import Registration
from django.urls import reverse
from urllib.parse import urlencode
from django.shortcuts import  redirect


# Create your views here.


def landing(req):
    return render(req,'landing.html')


def register(req):
    return render(req,'register.html')
def login(req):
    return render(req,'login.html')

def registerdata(req):
    if req.method == 'POST':
        n = req.POST.get('name')
        e = req.POST.get('email')
        c = req.POST.get('contact_number')
        d = req.POST.get('description')
        g = req.POST.get('gender')  
        hg = req.POST.get('education')
        q_list = req.POST.getlist('qualification')
        q = ",".join(q_list)  
        pro = req.FILES.get('profile_pic')
        doc = req.FILES.get('document')
        a = req.FILES.get('audio')
        v = req.FILES.get('video')
        p = req.POST.get('password')
        cp = req.POST.get('cpassword')
       

        # Check if user already exists
        if Registration.objects.filter(email=e).exists():
            msg = 'email already exists'
            return render(req, 'register.html', {'x': msg})
        else:
            if p==cp:
                # print(n,e,c,g,d,q,hg,pro,doc,a,v)
                
                Registration.objects.create(
                full_name=n,
                email=e,
                contact_number=c,
                gender=g,
                description=d,
                qualification=q,
                higher_education=hg,
                profile_picture=pro,
                document=doc,
                audio=a,
                video=v,
                password=p
                )
                
                return render(req, 'login.html', {'y': 'Register successful'})
            else:
                print("he...........")
                msg="password nad confirm password not match"
                data={'name':n,'email':e,'contact_number':c,'gender':g,'description':d,'qualification':q,'higher_education':hg,'profile_picture':pro,'document':doc,'audio':a,'video':v}
                return render(req, 'register.html', {'pmsg':msg, 'data':data})
def logindata(req):
    if req.method == 'POST':
         # print(req.POST)
        le = req.POST.get('email')
        lp = req.POST.get('password')
        user=Registration.objects.filter(email=le)
        if user:
            userdata=Registration.objects.get(email=le)
            name=userdata.full_name
            email=userdata.email
            contact=userdata.contact_number
            gender=userdata.gender
            description=userdata.description
            qualification=userdata.qualification
            higher_education=userdata.higher_education
            profile_picture=userdata.profile_picture
            document=userdata.document
            audio=userdata.audio
            video=userdata.video
            password=userdata.password
            print(name,email,contact,gender,description,qualification,higher_education,profile_picture,document,audio,video,password)
            data={'name':name,'email':email,'contact':contact,'gender':gender,'description':description,'qualification':qualification,'higher_education':higher_education,'profile_picture':profile_picture,
                  'document':document,'audio':audio,'video':video}
            
            if password==lp:
                # return render (req,'dashboard.html',data) #  error ligindata page is same page
                base_url=reverse('dashboard')
                data=urlencode(data)
                url=f'{base_url}?{data}'
                return redirect(url)
                
            
            else:
                msg="Email and password not matched"
                return render(req,'login.html',{'msg':msg})
        else:
            msg="Email id not register"
            return render(req,'register.html',{'msg':msg,'email':le})
        
def dashboard(req):
    print(req.GET)
    e=req.GET.get('email')
    p=req.GET.get('password')
    
    if e and p:
        n=req.GET.get('name')
        c=req.GET.get('contact')
        g=req.GET.get('gender')
        d=req.GET.get('description')
        q=req.GET.get('qualification')
        hg=req.GET.get('higher_education')
        p=req.GET.get('profile_picture')
        doc=req.GET.get('document')
        a=req.GET.get('audio')
        v=req.GET.get('video')
        data={'name':n,'contact':c,'gender':g,'description':d,'qualification':q,'higher_education':hg,'profile_picture':p,'document':doc,'audio':a,'video':v}
        return render (req,'dashboard.html',data)
    else:
        return render(req,'login.html')
    
            
        