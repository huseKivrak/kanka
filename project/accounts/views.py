from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from . forms import CustomUserCreationForm
from letters.models import mailbox_count_for


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            auth_login(request, new_user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {'form': form})


def login(request):
    return render(request, "login.html")


def profile(request):
    user = request.user
    mailbox_count = mailbox_count_for(user)
    context = {
        'user':user,
        'mailbox_count': mailbox_count
    }
    return render(request, "profile.html", context)


def logout(request):
    auth_logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('/')
