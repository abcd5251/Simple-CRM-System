from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout # for login system
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

# Create your views here.

def home(request):
    records = Record.objects.all()

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
        return render(request, 'home.html', {'records': records})

# want to put this with home (login then show content, unlogin then show login page)
# def login_user(request): # name cannot be login because will conflict with login func
#     pass


def logout_user(request): 
    logout(request)
    messages.success(request, "You have been Logged Out ...")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, "You have successfully register !!!")
            return redirect('home')
    
    else:
        form = SignUpForm() # just going to the page and not fillout the form yet
        return render(request, 'register.html', {'form' : form}) # pass the form(SignUpForm) to the page
    
    return render(request, 'register.html', {'form' : form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        customer_record = Record.objects.get(id = pk) # pk means primary key
        return render(request, 'record.html', {'customer_record' : customer_record})
    else:
        messages.success(request, "You must login to view that page!!!")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Records deleted Successfully !!")
        return redirect('home')
    else:
        messages.success(request, "You must login to do that!!!")
        return redirect('home')
