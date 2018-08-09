from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from . import SignUpForm

def home(request):
    return render(request, 'authenticate/home.html', {})

def login_user(request):

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('Logged In'))
            return redirect('home')

        else:
            messages.success(request, (' Error Logged In *Try again'))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html',{})


def logout_user(request):
    logout(request)
    messages.success(request, (' you have been Logged Out'))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('you have registered'))
            return redirect('home')
    else:
        form = SignUpForm()
        context = {'form':form}
    return render(request, 'authenticate/register.html',context )
