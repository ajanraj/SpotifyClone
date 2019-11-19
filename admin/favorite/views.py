from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import re
from django.contrib import messages
from admin.favorite.models import Favorite
from admin.user.models import CustomUser

# Create your views here.
@login_required(login_url='admin.login')
def index(request):

    data = Favorite.objects.order_by('-id')
    return render(request, 'adminTemplates/favorite/index.html', {'data': data})


@login_required(login_url='admin.login')
def index_id(request, id):

    user = CustomUser.objects.filter(pk=id)

    if not user:
        messages.error(request, "No such record found!")
        return redirect('admin.favorite.index')

    else:
        user = user.get()

    data = Favorite.objects.filter(user=user)
    return render(request, 'adminTemplates/favorite/index.html', {'data': data})
