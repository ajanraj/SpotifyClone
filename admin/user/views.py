from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from admin.user.models import CustomUser

# Create your views here.


@login_required(login_url='admin.login')
def index(request):

    data = CustomUser.objects.order_by('-id')
    return render(request, 'adminTemplates/user/index.html', {'data': data})
