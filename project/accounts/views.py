from django.shortcuts import render, redirect
from . forms import CustomUserCreationForm


def login(request):
    return render(request, "login.html")

def profile(request):
    return render(request, "profile.html")

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {'form': form})