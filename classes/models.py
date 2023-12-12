from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.urls import reverse

# Create your models here.
class user(models.Model):
 id = models.IntegerField()
 email = models.CharField(max_length=50,  primary_key=True)
 password = models.CharField(max_length=50)
 confirm_password = models.CharField(max_length=50)

class Posts(models.Model): 
 course = models.CharField(max_length=200, null=False, blank=True)
 sub_course = models.CharField(max_length=200, null=False, blank=True)
 title = models.CharField(max_length=200, null=False, blank=True)
 sub_title = models.CharField(max_length=200, null=False, blank=True)
 content = models.TextField()
 date_posted = models.DateTimeField(default=timezone.now)
 author = models.ForeignKey(User, on_delete=models.CASCADE)

 def __self__(self):
  return self.title
 
 def __self__(self):
  return self.sub_title 
 
 def __self__(self):
  return self.course 
 
 def get_absolute_url(self):
  return reverse('post_detail', kwargs={'pk':self.pk})
 
class Profile(models.Model):
 user = models.OneToOneField(User, on_delete=models.CASCADE)
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
 