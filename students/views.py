from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login as auth_log
from django.contrib import messages as messages
from django.contrib.auth.models import User
from .forms import StudentUpdateForm




# Create your views here.

def student(request):
 return render(request, 'student.html')

def Register(request):
 form = forms.StudentSignUpForm()

 if request.method == 'POST':
  form = forms.StudentSignUpForm(request.POST)

  if form.is_valid():
   username = form.cleaned_data.get('username').lower()
   user = form.save(commit=False)
   user.username = username
   user.save()
   messages.success(request, f'Account was created for: {user.first_name}')

   auth_log(request, user)
   return redirect('/courses/')
 return render(request, 'register.html', {'form' : form}) 