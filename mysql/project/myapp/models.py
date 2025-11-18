from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(null=True)
    mobile_Number= models.IntegerField(null=True)
    image=models.ImageField(upload_to='image',null=True)
    document=models.FileField(upload_to='file',null=True)
    audio=models.FileField(upload_to='audio',null=True)
    video=models.FileField(upload_to='video',null=True)
    
    def __str__(self):
        # return self.name
        return self.email