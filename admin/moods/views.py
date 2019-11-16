from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import re
from django.contrib import messages
from admin.moods.models import Moods
# Create your views here.


@login_required(login_url='admin.login')
def add(request):
    return render(request, 'adminTemplates/moods/moods-add.html')


@login_required(login_url='admin.login')
def save(request):
    if request.method == 'POST':

        name = request.POST['name']
        description = request.POST['description']

        if not re.match('^[(a-z)?(A-Z)?\d?_?\-?\.?\,?\s?]+$', name):
            messages.error(request, "Enter a valid name!")
            return redirect("admin.moods.add")

        if not re.match('^[(a-z)?(A-Z)?\d?!?_?\-?\.?\,?\s?]+$', description):
            messages.error(request, "Enter a valid Description!")
            return redirect("admin.moods.add")

        moods = Moods(moods_name=name, moods_des=description)
        moods.save()

        messages.success(request, "Data Added successfully")
        return redirect("admin.moods.index")

    else:
        return redirect("admin.moods.add")


@login_required(login_url='admin.login')
def index(request):

    data = Moods.objects.order_by('-id')
    return render(request, 'adminTemplates/moods/index.html', {'data': data})


@login_required(login_url='admin.login')
def delete(request, id):

    if request.method == 'GET':

        moods = Moods.objects.filter(pk=id)

        if not moods:
            messages.error(request, "No Such Record Found!")
            return redirect('admin.moods.index')
        else:
            moods.delete()
            messages.success(request, "Record Deleted Successfully")
            return redirect('admin.moods.index')


@login_required(login_url='admin.login')
def edit(request, id):
    if request.method == 'GET':

        moods = Moods.objects.filter(pk=id)

        if not moods:
            messages.error(request, "No Such Record Found!")
            return redirect('admin.moods.index')
        else:
            moods = moods.get()
            return render(request, 'adminTemplates/moods/edit.html', {'moods': moods})


@login_required(login_url='admin.login')
def update(request, id):
    if request.method == 'POST':

        moods = Moods.objects.filter(pk=id)

        if not moods:
            messages.error(request, "No Such Record Found!")
            return redirect('admin.moods.index')
        else:
            moods = moods.get()
            name = request.POST['name']
            description = request.POST['description']

            if not re.match('^[(a-z)?(A-Z)?\d?_?\-?\.?\,?\s?]+$', name):
                messages.error(request, "Enter a valid name!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            if not re.match('^[(a-z)?(A-Z)?\d?!?_?\-?\.?\,?\s?]+$', description):
                messages.error(request, "Enter a valid Description!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            moods.moods_name = name
            moods.moods_des = description

            moods.save()

            messages.success(request, " Record Updated Successfully")

            return redirect('admin.moods.index')
