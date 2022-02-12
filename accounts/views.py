from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
from .models import CustomUser
from .forms import CustomUserForm



def user_register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = CustomUserForm(request.POST)
            if form.is_valid():
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was creatd for ' + user)
                user = form.save()
                return redirect('user_login')
            else:
                messages.error(request, "Error")
        else:
            form = CustomUserForm()
    
    context = {
        'form':form,
    }
    return render(request, 'accounts/user_register.html', context)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request,"Invalid username or password.")

    return render(request, 'accounts/user_login.html')


def user_logout(request, username):
    user = CustomUser.objects.filter(username=username)
    logout(request, user)
    return redirect('index')
