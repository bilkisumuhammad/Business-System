from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .forms import SignupForm, LoginForm

# Create your views here.


def signup(request):
    form = SignupForm()
    context = {'signup': form}

    if request.method == 'POST':
        form = SignupForm(request.POST)
        name = request.POST["name"]
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if form.is_valid():
            form.save()
            if password == confirm_password:
                if User.objects.filter(email=email).exists():
                    messages.info(request, "email already exist")
                    return redirect('signup')
                elif User.objects.filter(username=username).exists():
                    messages.info(request, 'username already exits')
                    return redirect('signup')
                else:
                    form = User.objects.create_user(name,username=username, email=email, password=password)
                    form.save()
                    return redirect('login')
            else:
                messages.info(request, "incorrect password")
                return redirect('signup')
    return render(request, 'signup.html', context)


def user_login(request):
    user = LoginForm(request.POST)
    context = {'login': user}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('business')
        else:
            messages.info(request, 'Invalid login credentials')
            return redirect('login')
    else:
        return render(request, 'login.html', context)


                

