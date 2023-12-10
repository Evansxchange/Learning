from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib import messages as messages
from . import forms
from .models import Posts
from .forms import ProfileUpdateForm, UserUpdateForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.


def home(request):
 return render(request, 'home.html', {'nav' : 'home'})

@login_required()
def courses(request):
 context = {
  'Posts': Posts
 }
 return render(request, 'courses.html', {'nav' : 'courses'})
 
def sign_up(request):
 form = forms.SignUpForm()

 if request.method == 'POST':
  form = forms.SignUpForm(request.POST)

  if form.is_valid():
   email = form.cleaned_data.get('email').lower()
   user = form.save(commit=False)
   user.username = email
   user.save()
   messages.success(request, f'Account was created for: {user.first_name}')

   auth_login(request, user)
   return redirect('/courses/')
 return render(request, 'sign-up.html', {'form' : form}) 

class PostListView(LoginRequiredMixin,  ListView):
 model = Posts
 template_name = 'courses_page.html'
 context_object_name = 'Posts'
 ordering = ["-date_posted"]
 paginate_by = 3

class UserPostListView(LoginRequiredMixin,  ListView):
 model = Posts
 template_name = 'author_courses_page.html'
 context_object_name = 'Posts'
 ordering = ["-date_posted"]
 paginate_by = 7

 def get_queryset(self):
  user = get_object_or_404(User, first_name=self.kwargs.get('first_name'))
  return Posts.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(LoginRequiredMixin,  DetailView):
 model = Posts
 template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin,  CreateView):
 model = Posts
 fields = ['title', 'content']
 template_name = 'new_post.html'
 success_url = '/courses_page'


 def form_valid(self, form):
  form.instance.author = self.request.user
  return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
 model = Posts
 fields = ['title', 'content']
 template_name = 'update_post.html'


 def form_valid(self, form):
  form.instance.author = self.request.user
  return super().form_valid(form)
 
 def test_func(self):
   Posts = self.get_object()
   if self.request.user == Posts.author:
    return True
   return False
 
class PostDeleteView(DeleteView):
 model = Posts
 template_name = 'post_confirm_delete.html'
 success_url = '/courses_page'

 def test_func(self):
   Posts = self.get_object()
   if self.request.user == Posts.author:
    return True
   return False
  


@login_required
def profile(request):
 return render(request, 'profile.html', {'nav': 'profile'})

@login_required
def update_profile(request):
 if request.method == 'POST':
  u_form = UserUpdateForm(request.POST, instance=request.user)
  p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
  if u_form.is_valid() and p_form.is_valid():
    u_form.save()
    p_form.save()
    messages.success(request, f"Your profile was updated!!")
    return redirect('profile')
  
 else:
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    
 context = {
    "u_form": u_form,
    "p_form": p_form
  }
 return render(request, 'up-profile.html',  context)

