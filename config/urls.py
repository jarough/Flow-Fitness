"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from userreg import views as userviews
from django.contrib.auth import views as authviews
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gym.urls')),
    path('register/', userviews.register, name="user-register"),
    path('profile/', userviews.profile, name="user-profile"),
    path('login/', authviews.LoginView.as_view(template_name="userreg/login.html"), name="user-login"),
    path('logout/', authviews.LogoutView.as_view(template_name="userreg/logout.html"), name="user-logout"),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('home/', views.home, name='home'),
]   
