from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import get_user_model, logout, login as auth_login
import re

# Create your views here.


def index(request):
    return render(request, 'adminTemplates/login/index.html')


def login(request):

    if request.method == "POST":

        username = request.POST['email']
        password = request.POST['password']

        if not re.match(r"^[\w\.\+\-\_]+\@[\w-]+\.[a-z]{2,3}$", username):
            messages.error(request, "Enter a valid Email!")
            return redirect('admin.login')
        if len(password) < 4:
            messages.error(request, "Password is Too Short")
            return redirect('admin.login')

        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)

            if not user.is_superuser:
                messages.error(request, "Not a actual admin")
                return redirect('admin.login')

            if user.check_password(password):
                auth_login(request, user)
                messages.success(request, "Logged In")
                return redirect('admin.dashboard.index')
            else:
                messages.error(request, "Invalid Password")
                return redirect('admin.login')

        except UserModel.DoesNotExist:
            messages.error(request, "Invalid Email")
            return redirect('admin.login')

    else:
        return redirect('admin.login')


def logout_now(request):
    logout(request)
    messages.success(request, "Logged out Successfully!")
    return redirect('admin.login')
