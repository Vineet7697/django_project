from django import forms
from .models import Student
# class StudentForm(forms.Form):
#     name=forms.CharField()
#     age=forms.IntegerField()
#     email=forms.EmailField()

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'