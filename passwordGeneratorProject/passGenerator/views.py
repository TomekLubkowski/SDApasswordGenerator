from django.shortcuts import render

# form


def home(request):
    return render(request, 'home.html')


def password(request):
    return render(request, 'password.html')
