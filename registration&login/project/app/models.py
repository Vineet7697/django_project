from django.db import models

# Create your models here.


GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]

QUALIFICATION_CHOICES = [
    ('10', '10th'),
    ('12', '12th'),
    ('UG', 'Undergraduate'),
    ('PG', 'Postgraduate'),
]



class Registration(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_number = models.CharField( max_length=15)
    description = models.TextField(blank=True, null=True)

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,null=True)
    qualification = models.CharField(max_length=3, choices=QUALIFICATION_CHOICES)
    higher_education = models.CharField( max_length=100,  blank=True )

    profile_picture = models.ImageField(
        upload_to='profiles',
        blank=True,
        null=True
    )
    document = models.FileField(
        upload_to='document',
        blank=True,
        null=True
    )
    audio = models.FileField(
        upload_to='audio',
        blank=True,
        null=True
    )
    video = models.FileField(
        upload_to='video',
        blank=True,
        null=True
    )
    
    password = models.CharField( max_length=50,  blank=True )
    
    
