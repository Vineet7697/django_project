from django.shortcuts import render,redirect

from .models import *


def all_data(req):
    # Stu_data=Students.objects.all() #parent to child access
    Stu_data=Students.objects.select_related('student') #join the two or multiple  table select_related
    # print(Stu_data.query)
    # for i in Stu_data:
        # print(i.name,i.father_name,i.email,i.mobile,i.course,i.student.roll_no,i.student.allotted_date)
        
    Uni_data=UniversityRoll.objects.all() #child to parent access
    # for i in Uni_data:
        # print(i.roll_no,i.allotted_date,i.student.name,i.student.father_name,i.student.mobile,i.student.email,i.student.course)
    return render(req,'data.html',{'data1':Stu_data,'data2':Uni_data})
    