from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout # for login system
from django.contrib import messages


# Create your views here.

def home(request):
    # Check to see if user login or not
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have login !!")
            return redirect('home')

        else:
            messages.success(request, "There was an error login, Please try again !!")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

# want to put this with home (login then show content, unlogin then show login page)
# def login_user(request): # name cannot be login because will conflict with login func
#     pass

def logout_user(request):
    pass