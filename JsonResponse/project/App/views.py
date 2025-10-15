from django.shortcuts import render
from django.http import JsonResponse
from . models import Employee

# Create your views here.
# def jsonresponse1(req):
#     data = {'name':'Neeraj','age':37,'quali':'M.Tech'}
#     return JsonResponse(data) # JsonResponse expect data must me either dict or list

# def jsonresponse1(req):
#  data = {'name':'Neeraj','age':35,'quali':'M.Tech'}
#  return JsonResponse(data, safe=True) # safe=True default parameter for dict only

def jsonresponse1(req):
    data = [10,20,'python','java','php']
    return JsonResponse(data, safe=False)  # In order to allow non-dict objects to be serialized set the safe parameter to False

def jsonresponse2(req):
    data = {'name':'Neeraj','age':37,'quali':'M.Tech'}
    return JsonResponse(data, json_dumps_params={'indent':2},status=200)




def employee_list(request):
    employees = Employee.objects.values("id", "name", "email")  # returns a QuerySet of dicts
    return JsonResponse(list(employees), safe=False)