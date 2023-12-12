"""
URL configuration for Learning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from students import views as StudentView
from classes import views
from django.contrib.auth import views as form_validation
from django.contrib.auth import views as student_form_validation
from classes.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, CoursePostListView, TitlePostListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('login/', student_form_validation.LoginView.as_view(template_name="student.html"), name='login'),
    path('register/', StudentView.Register, name="register"),


    path('courses/', views.courses, name="courses"),
    path('courses_page/', PostListView.as_view(), name="courses_page"),
    path('author_page/<str:first_name>/' , UserPostListView.as_view(), name="author_page"),
    path('author_courses_page/<str:first_name>/', CoursePostListView.as_view(), name="author_courses_page"),
    path('author_title_page/<str:first_name>/' , TitlePostListView.as_view(), name="author_title_page"),

    path('post/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('post/new', PostCreateView.as_view(), name="new_post"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="post_update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="post_delete"),


    path('profile/', views.profile, name="profile"),
    path('update_profile/', views.update_profile, name="update_profile"),

    path('sign-in/', form_validation.LoginView.as_view(template_name="sign-in.html"), name='sign-in'),
    path('logout/', form_validation.LogoutView.as_view(next_page="/")),
    path('sign-up/', views.sign_up, name="SignUp"),

    path('password-reset/', form_validation.PasswordResetView.as_view(template_name="password_reset.html"), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', form_validation.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('password-reset/done/', form_validation.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name='password_reset_done'),
    path('password-reset-complete/', form_validation.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name='password_reset_complete'),

    ]


if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)