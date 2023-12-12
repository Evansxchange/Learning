from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as StudentUser
from django.core.exceptions import ValidationError
from .models import StudentProfile

class StudentSignUpForm(UserCreationForm):
 email = forms.CharField(max_length=50)
 first_name = forms.CharField(max_length=50)
 last_name = forms.CharField(max_length=50)
 username = forms.CharField(max_length=30)


 class Meta:
  model = StudentUser
  fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')

 def clean_username(self):
  username = self.cleaned_data['username'].lower()
  if StudentUser.objects.filter(username=username):
   raise ValidationError('This username address aready exits.')
  return username

class StudentUpdateForm(forms.ModelForm):
 email = forms.EmailField
 bio = forms.TextInput

 class Meta:
  model = StudentUser
  fields = ['first_name', 'username']

class ProfileUpdateForm(forms.ModelForm):
 class Meta:
  model = StudentProfile
  fields = ['image']  