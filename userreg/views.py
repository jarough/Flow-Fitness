from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def register(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Welcome to FlowFitness {username}! Please login to continue.")
            return redirect('user-login')
    else:
        form = forms.RegisterForm()
        return render(request, 'userreg/register.html', {'form': form})

@login_required()
def profile(request):
    return render(request, 'userreg/profile.html')