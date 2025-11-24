from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator,MinLengthValidator,MaxValueValidator,MinValueValidator,EmailValidator

# Create your models here.

def validation_name(value):
    if not value.replace(' ','').isalpha():
        raise ValidationError ("Enter correct name")
    
class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField(validators=[MaxValueValidator(60),MinValueValidator(18)])
    # def clean(self):
        # model level inheritence
        # if not value.replace(' ','').isalpha():
        # raise ValidationError ("name contain error")
    def save(self,*args,**kwargs):
        self.full_clean()
        super().save(*args,**kwargs)
    