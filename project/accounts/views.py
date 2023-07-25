from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from . forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            auth_login(request, new_user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {'form': form})


def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            logger.debug("user:  %s", user)

            if user is not None:
                auth_login(request, user)
                messages.info(request, f'welcome back, {user.username}!')
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, form.errors)

    else:
        form = CustomAuthenticationForm()
    return render(request, "login.html", {'form': form})

@login_required
def profile(request):
    return render(request, "profile.html")


def logout(request):
    auth_logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('/')
