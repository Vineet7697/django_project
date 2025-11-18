from django.shortcuts import render
from .models import Students
# Create your views here.


def form(req):
        return render(req,'form.html')    
def formdata(req):
        if req.method=="POST":
                n=req.POST.get('name')
                e=req.POST.get('email')
                Mo=req.POST.get('mobile_Number')
                i=req.FILES.get('image')
                d=req.FILES.get('document')
                a=req.FILES.get('audio')
                v=req.FILES.get('video')
                # print(n,e,Mo,i,d,a,v)
                Students.objects.create(name=n,email=e,mobile_Number=Mo,image=i,document=d,audio=a,video=v)
                return render(req,'showdata.html')
                
def show(req):
        ## Query that work on multiple objects:
        # data=Students.objects.all()
        # print(type(data))
        # data=Students.objects.values()
        # data=Students.objects.values_list()
        # data=Students.objects.values_list('id','name')
        # data=Students.objects.filter(name='Vineet kushwaha')
        # data=Students.objects.filter(name='Vineet kushwaha',email='vineetkushwaha2010@gmail.com')
        # data=Students.objects.exclude(name='Vineet kushwaha')
        # data=Students.objects.order_by()
        # data=Students.objects.order_by('- name')
        # data=(Students.objects.all().reverse)
        # data=(Students.objects.all()[2:3])
        
        
        
        ## Query that work on single objects:
        # data=Students.objects.get(name='hi')
        # data=Students.objects.first()
        # data=Students.objects.last()
        # data=Students.objects.latest('name')
        # data=Students.objects.earliest('name')
        # data=Students.objects.create(name='Vineet Kushwaha',email='vineetkushwaha2010@gmail.com')
        
        
        
        
        ##Composite Query:
        # data=Students.objects.bulk_create([    
        # Students(name='Vineet Kushwaha',email='vineetkushwaha2010@gmail.com'),
        # Students(name='Vineet Kushwaha',email='vineetkushwaha2010@gmail.com'),
        # Students(name='Vineet Kushwaha',email='vineetkushwaha2010@gmail.com')
        # ])
        
        # data=Students.objects.get(email='vineetkushwaha2010@gmail.com').delete()
        # data=Students.objects.filter(email='vineetkushwaha2010@gmail.com').delete()
        # data=Students.objects.update_or_create(name='Vineet Kushwaha',email='vineetkushwaha2010@gmail.com',default={'key':'value'})
        # data=Students.objects.filter(name='Vineet Kushwaha').update(name='Vineet')
        # data=data,created = Students.objects.get_or_create(name='Vineet',email='vineetkushwaha2010@gmail.com')
        # data=Students.objects.order_by('name').first()
        data=Students.objects.order_by('name').last()
        
        
        return render(req,'showdata.html' ,{'all_data':data})