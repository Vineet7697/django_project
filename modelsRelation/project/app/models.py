
from django.db import models

# Create your models here.
class Branch(models.Model):
    b_name=models.CharField(max_length=50)
    b_dis=models.TextField()
    
    def __str__(self):
        return self.b_name

class Students(models.Model):      # related_name='students' required related_name='roll'
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=50)
    branch= models.ForeignKey(Branch,on_delete=models.CASCADE, related_name='branch',null=True)

    def __str__(self):
        return self.name

class UniversityRoll(models.Model):
    student = models.OneToOneField(Students, on_delete=models.CASCADE, related_name='student')
    roll_no = models.CharField(max_length=20, unique=True)
    allotted_date = models.DateField(auto_now_add=True)

    # def __str__(self):
    #     return f"{self.roll_no} → {self.student.name}"
    
    
