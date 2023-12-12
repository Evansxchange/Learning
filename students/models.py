from django.db import models
from django.contrib.auth.models import User as StudentUser
from django.utils import timezone
from PIL import Image
from django.urls import reverse

# Create your models here.
class student(models.Model):
 id = models.IntegerField()
 email = models.CharField(max_length=50,  primary_key=True)
 password = models.CharField(max_length=50)
 confirm_password = models.CharField(max_length=50)
 
class StudentProfile(models.Model):
 user = models.OneToOneField(StudentUser, on_delete=models.CASCADE)
 image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')

 def __str__(self):
  return f'{self.user.username} Profile'
 
 def save(self, *args, **kwargs):
  super().save(*args, **kwargs)
  img = Image.open(self.image.path)
  if img.height > 300 or img.width > 300:
   output_size = (250, 250)
   img.thumbnail(output_size)
   img.save(self.image.path)
 