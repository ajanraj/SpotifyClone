from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import re
from django.contrib import messages
from admin.artists.models import Artists
# Create your views here.


@login_required(login_url='admin.login')
def add(request):
    return render(request, 'adminTemplates/artists/artists-add.html')


@login_required(login_url='admin.login')
def save(request):
    if request.method == 'POST':

        name = request.POST['name']
        description = request.POST['description']

        if not re.match('^[(a-z)?(A-Z)?\d?_?\-?\.?\,?\s?]+$', name):
            messages.error(request, "Enter a valid name!")
            return redirect("admin.artists.add")

        if not re.match('^[(a-z)?(A-Z)?\d?!?_?\-?\.?\,?\s?]+$', description):
            messages.error(request, "Enter a valid Description!")
            return redirect("admin.artists.add")

        artists = Artists(artists_name=name, artists_des=description)
        artists.save()

        messages.success(request, "Data Added successfully")
        return redirect("admin.artists.index")

    else:
        return redirect("admin.artists.add")


@login_required(login_url='admin.login')
def index(request):

    data = Artists.objects.order_by('-id')
    return render(request, 'adminTemplates/artists/index.html', {'data': data})


@login_required(login_url='admin.login')
def delete(request, id):

    if request.method == 'GET':

        artists = Artists.objects.filter(pk=id)

        if not artists:
            messages.error(request, "No Such Record Found!")
            return redirect('admin.artists.index')
        else:
            artists.delete()
            messages.success(request, "Record Deleted Successfully")
            return redirect('admin.artists.index')


@login_required(login_url='admin.login')
def edit(request, id):
    if request.method == 'GET':

        artists = Artists.objects.filter(pk=id)

        if not artists:
            messages.error(request, "No Such Record Found!")
            return redirect('admin.artists.index')
        else:
            artists = artists.get()
            return render(request, 'adminTemplates/artists/edit.html', {'artists': artists})


@login_required(login_url='admin.login')
def update(request, id):
    if request.method == 'POST':

        artists = Artists.objects.filter(pk=id)

        if not artists:
            messages.error(request, "No Such Record Found!")
            return redirect('admin.artists.index')
        else:
            artists = artists.get()
            name = request.POST['name']
            description = request.POST['description']

            if not re.match('^[(a-z)?(A-Z)?\d?_?\-?\.?\,?\s?]+$', name):
                messages.error(request, "Enter a valid name!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            if not re.match('^[(a-z)?(A-Z)?\d?!?_?\-?\.?\,?\s?]+$', description):
                messages.error(request, "Enter a valid Description!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            artists.artists_name = name
            artists.artists_des = description

            artists.save()

            messages.success(request, " Record Updated Successfully")

            return redirect('admin.artists.index')
