# news/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib import messages

def signup(request):
    """
    Handle user signup.

    If the request method is POST, processes the CustomUserCreationForm with the submitted data.
    If the form is valid, the user is created and logged in, then redirected to the search page.
    If the request method is GET, renders an empty CustomUserCreationForm.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered signup page if the request method is GET, 
                      or a redirect to the search page if the form is valid and the user is created.
    """
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('search')
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentication/signup.html', {'form': form})

def user_login(request):
    """
    Handle user login.

    If the request method is POST, processes the CustomAuthenticationForm with the submitted data.
    If the form is valid, the user is authenticated and logged in, then redirected to the search page.
    If the user is blocked, an error message is displayed and the user is redirected to the login page.
    If the request method is GET, renders an empty CustomAuthenticationForm.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered login page if the request method is GET or the form is invalid,
                      or a redirect to the search page if the form is valid and the user is authenticated,
                      or a redirect to the login page if the user is blocked.
    """

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if not user.is_blocked:
                login(request, user)
                return redirect('search')
            else:
                messages.error(request, 'You have been blocked.')
                return redirect('login')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})

def user_logout(request):
    """
    Handle user logout.

    Logs out the user and displays a success message.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Redirect to the login page.
    """

    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')
