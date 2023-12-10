from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile

class SignUpForm(UserCreationForm):
 email = forms.CharField(max_length=50)
 first_name = forms.CharField(max_length=50)
 last_name = forms.CharField(max_length=50)


 class Meta:
  model = User
  fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

 def clean_email(self):
  email = self.cleaned_data['email'].lower()
  if User.objects.filter(email=email):
   raise ValidationError('This email address aready exits.')
  return email

class UserUpdateForm(forms.ModelForm):
 email = forms.EmailField
 bio = forms.TextInput

 class Meta:
  model = User
  fields = ['first_name', 'username']

class ProfileUpdateForm(forms.ModelForm):
 class Meta:
  model = Profile
  fields = ['image']  