from django.contrib.auth import authenticate, login as login_, logout as logout_
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login_(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Невалидни Потр. име/парола')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    logout_(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Потребителското име е заето')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Този имейл се използва от друг акаунт')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Паролите не съвпадат')
            return redirect('register')
    else:
        return render(request, 'register.html')