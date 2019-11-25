from django.shortcuts import render, redirect
from admin.homepage.models import Homepage
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, logout, login as auth_login
from admin.user.models import CustomUser
import re
import json


@login_required(login_url='frontend.login')
def index(request):

    user = CustomUser.objects.filter(pk=request.user.id)

    if not user:
        messages.error(request, "Login to Continue!")
        return redirect('frontend.index')

    else:
        user = user.get()

    return render(request, 'frontendTemplates/account/index.html', {'user': user})


@login_required(login_url='frontend.login')
def edit(request):

    user = CustomUser.objects.filter(pk=request.user.id)

    if not user:
        messages.error(request, "Login to Continue!")
        return redirect('frontend.index')

    else:
        user = user.get()

    return render(request, 'frontendTemplates/account/edit.html', {'user': user})


@login_required(login_url='frontend.login')
def update(request):
    if request.method == "POST":
        user = CustomUser.objects.filter(pk=request.user.id)

        if not user:
            messages.error(request, "Login to Continue!")
            return redirect('frontend.index')

        else:
            user = user.get()

        if not 'name' in request.POST.keys():
            messages.error(request, "Prameters is missing")
            return redirect("frontend.account.login")
        if not 'email' in request.POST.keys():
            messages.error(request, "Prameters is missing")
            return redirect("frontend.account.login")
        if not 'gender' in request.POST.keys():
            messages.error(request, "Prameters is missing")
            return redirect("frontend.account.login")
        if not 'mobile' in request.POST.keys():
            messages.error(request, "Prameters is missing")
            return redirect("frontend.account.login")

        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        gender = request.POST['gender']

        if not re.match('^[(a-z)?(A-Z)?\d?_?\-?\.?\,?\s?]+$', name):
            messages.error(request, "Enter a valid name!")
            return redirect("frontend.account.edit")
        if not re.match(r"^[\w\.\+\-\_]+\@[\w-]+\.[a-z]{2,3}$", email):
            messages.error(request, "Enter a valid Email!")
            return redirect('frontend.account.edit')
        if not re.match('^[\d]{10,12}$', mobile):
            messages.error(request, "Invalid Phone number")
            return redirect('frontend.account.edit')

        user.name = name
        user.email = email
        user.gender = gender
        user.phone = mobile

        user.save()

        messages.success(request, "Profile Updated")
        return redirect("frontend.account.index")
    else:
        return redirect("frontend.account.edit")


@login_required(login_url='frontend.login')
def edit_pass(request):
    user = CustomUser.objects.filter(pk=request.user.id)

    if not user:
        messages.error(request, "Login to Continue!")
        return redirect('frontend.index')

    else:
        user = user.get()

    return render(request, 'frontendTemplates/account/edit_pass.html', {'user': user})


@login_required(login_url='frontend.login')
def update_pass(request):
    if request.method == "POST":

        if not 'cpass' in request.POST.keys():
            messages.error(request, "Parameters is missing")
            return redirect("frontend.account.edit.pass")
        if not 'npass' in request.POST.keys():
            messages.error(request, "Parameters is missing")
            return redirect("frontend.account.edit.pass")
        if not 'conpass' in request.POST.keys():
            messages.error(request, "Parameters is missing")
            return redirect("frontend.account.edit.pass")

        cpass = request.POST['cpass']
        npass = request.POST['npass']
        conpass = request.POST['conpass']

        if((len(cpass) < 3) or (len(npass) < 3) or (len(conpass) < 3)):
            messages.error(
                request, "Password  Should not be less than 3 Characters")
            return redirect("frontend.account.edit.pass")

        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(pk=request.user.id)

            if user.check_password(cpass):
                if npass != conpass:
                    messages.error(
                        request, "New Password and Confirm Password Doesn't Match ")
                    return redirect("frontend.account.edit.pass")

                else:
                    user.Password = make_password(conpass)
                    user.save()
                    auth_login(request, user)
                    messages.error(request, "Password Updated Successfully")
                    return redirect("frontend.account.edit.pass")

            else:
                messages.error(request, "Current Password Doesn't Match")
                return redirect("frontend.account.edit.pass")

        except UserModel.DoesNotExist:
            messages.error(request, "Login First")
            return redirect("frontend.login")


@login_required(login_url='frontend.login')
def change_profile_pic(request):
    if request.is_ajax():
        if 'file' in request.FILES.keys():

            if not request.FILES['file'].name.split('.')[-1] in ['jpg', 'png', 'jpeg']:

                return HttpResponse(json.dumps({'key': '0', 'msg': 'Invalid File Type!'}))

            user = CustomUser.objects.filter(pk=request.user.id)

            if not user:
                messages.error(request, 'Log In First!')
                return redirect('home-login')
            else:
                user = user.get()

            if "team.jpg" in str(user.profile_pic):

                user.profile_pic = request.FILES['file']

                user.save()

            else:
                user.profile_pic.delete()

                user.profile_pic = request.FILES['file']

                user.save()

            return HttpResponse(json.dumps({'key': '1', 'msg': 'Success!'}))

        else:
            return HttpResponse(json.dumps({'key': '0', 'msg': 'No File Selected!'}))
