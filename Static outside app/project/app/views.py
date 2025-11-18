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


def dtl(req):
    # data={'name':'vineet', 'email':"v@gmail.com", 'age':21}
    # return render(req,'dtl.html',data)
    
    # value={"value":"my FIRST post"}
    # return render(req,'dtl.html',value)

    # value={"value":"Joel is a slug"}
    # return render(req,'dtl.html',value)
    
    # value={"value":"Joel is a slug"}
    # return render(req,'dtl.html',value)
    
    # value={"value":"Joel is a slug"}
    # return render(req,'dtl.html',value)
    
    
    # value={"value":" Totally LOVING this Album!"}
    # return render(req,'dtl.html',value)
    
    # value={"value":" Joel is a slug"}
    # return render(req,'dtl.html',value)
    
    # value={"key": "django"}
    # return render(req,'dtl.html',value)
    
    # value={"key": "Django"}
    # return render(req,'dtl.html',value)
    
    # value={"key": "Django"}
    # return render(req,'dtl.html',value)
    
    
    # context={"value": "String with spaces"}
    # return render(req,'dtl.html',context)
    
    
    # context={"value": ['a', 'b', 'c']}
    # return render(req,'dtl.html',context)
    
    # context={"value": ""}
    # return render(req,'dtl.html',context)
    
    # context={"value": None}
    # return render(req,'dtl.html',context)
    
    # context={"value": ['a', 'b', 'c', 'd']}
    # return render(req,'dtl.html',context)
    
    # context={"value": ['a', 'b', 'c', 'd']}
    # return render(req,'dtl.html',context)
    
    
    # context={"value": ['a', 'b', 'c', 'd']}
    # return render(req,'dtl.html',context)
    
    # context={"value": "abcd"}
    # return render(req,'dtl.html',context)
    
    
    
    
    
    # context={"value": "abcd"}
    # return render(req,'dtl.html',context)

    # context={"value": "abcd"}
    # return render(req,'dtl.html',context)

    # context={"value": "abcd"}
    # return render(req,'dtl.html',context)
    
    
    
        data={'name':'neeraj','age':37,'l':['python','java','php']}
        return render(req,'dtl.html',data)