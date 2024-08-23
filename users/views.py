from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect if user is already authenticated.
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                # Add an error message if authentication fails
                messages.error(request, 'Invalid username or password.')
        
        return render(request, "authenticate/login_user.html", {})


def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect if user is already authenticated. This makes login users not having access to register pages.
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)

                    return redirect('home')

        else:
            form = UserCreationForm()  # Initialize the form for GET requests

        return render(request, 'authenticate/register_user.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login_user')
