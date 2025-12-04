from django.shortcuts import render,redirect

from .models import *


# def all_data(req):
#     # Stu_data=Students.objects.all() #parent to child access
#     # Stu_data=Students.objects.select_related('student') #join the two or multiple  table select_related
#     # Stu_data=Students.objects.select_related('student_set()') #join the two or multiple  table select_related
#     # print(Stu_data.query)
#     # for i in Stu_data:
#     #     print(i.students_set.all())
#     # Stu_data=Students.objects.prefetch_related('student') #join the two or multiple  table select_related
#     Stu_data=Students.objects.prefetch_related('student_set') #join the two or multiple  table select_related
#     print(Stu_data.query)
#     for i in Stu_data:
#         print(i.student_set.all())
#     #     print(i.name,i.father_name,i.email,i.mobile,i.course,i.student.roll_no,i.student.allotted_date)
        
#     Uni_data=UniversityRoll.objects.all() #child to parent access
#     # for i in Uni_data:
#         # print(i.roll_no,i.allotted_date,i.student.name,i.student.father_name,i.student.mobile,i.student.email,i.student.course)
#     return render(req,'data.html',{'data1':Stu_data,'data2':Uni_data})
    
    
def forward_data(req):
    # data=Course.objects.all()
    # for i in data:
    #     print(i.c_name,i.s_name.all())
    
    # reverse access without using ralated name
    # data=Student1.objects.all()
    # for i in data:
    #     print(i.stu_name,i.course_set.all())
    
    # data=Course.objects.prefetch_related('s_name')
    # for i in data:
    #     print(i.c_name,i.s_name.all())
    
    # reverse access without using ralated name
    # data=Student1.objects.prefetch_related('course_set')
    # for i in data:
    #     print(i.stu_name,i.course_set.all())
        
    # using realted name
    # data=Student1.objects.all()
    # for i in data:
    #     print(i.stu_name,i.curs.all())
        
        
    #  using ralated name
    data=Student1.objects.prefetch_related('curs')
    for i in data:
        print(i.stu_name,i.curs.all())
        
        
        
        
# related_name not used for forward access
        # 1. onetoone
        # 2. foreignkey
        # 1. manytomany
        
# related_name effected to reverse access
    #   for single object related_model in lowercase
    # for multiple object related_model_set
   
   
    
# check in terminal
# (env) PS C:\Django_project\modelsRelation\project> py manage.py shell    
# 11 objects imported automatically (use -v 2 for details).

# Ctrl click to launch VS Code Native REPL
# Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from app .models import Student1 as S
# >>> data=S.objects.prefetch_related('curs')
# >>> for i in data:
# ...     print(i.stu_name,i.curs.all())
# ... 
# vineet <QuerySet [<Course: Course object (1)>]>
# rahul <QuerySet [<Course: Course object (2)>]>
# >>>