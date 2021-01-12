"""stuff5e URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('edit_profile/',UserEditView.as_view(), name="edit-profile"),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html'), name="change-password"),
    path('password_success/', views.password_success, name="password-success"),
    path('<int:pk>/profile', ShowProfilePageView.as_view(), name="show-profile-page"),
    path('<int:pk>/edit_profile_page', EditProfilePageView.as_view(), name="edit-profile-page"),
    path('create_profile_page', CreateProfilePageView.as_view(), name="create-profile-page"),

]
