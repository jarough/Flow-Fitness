from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="gym-home"),
    path('about/', views.about, name="gym-about"),
]
