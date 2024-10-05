from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms

# Create your views here.
def register(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Welcome {username}!")
            return redirect('gym-home')
    else:
        form = forms.RegisterForm()
        return render(request, 'userreg/register.html', {'form': form})