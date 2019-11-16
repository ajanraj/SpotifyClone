from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from admin.user.models import CustomUser
import json
# Create your views here.


@login_required(login_url='admin.login')
def index(request):
    data = CustomUser.objects.order_by('-id')
    return render(request, 'adminTemplates/user/index.html', {'data': data})


@login_required(login_url='admin.login')
def details(request, id):

    if request.method == 'GET':

        user = CustomUser.objects.filter(pk=id)

        if not user:
            messages.error(request, "No such record found!")
            return redirect('admin.user.index')

        else:
            user = user.get()

        return render(request, 'adminTemplates/user/details.html', {'data': user})


@login_required(login_url='admin.login')
def make_admin(request):

    if request.is_ajax():

        if not 'action' in request.POST.keys():

            return HttpResponse(json.dumps({'key': '0', 'msg': 'Parameters are missing!'}))

        if not 'id' in request.POST.keys():

            return HttpResponse(json.dumps({'key': '0', 'msg': 'Parameters are missing!'}))

        user = CustomUser.objects.filter(pk=request.POST['id'])

        if not user:

            return HttpResponse(json.dumps({'key': '0', 'msg': 'Not a Valid User!'}))
        else:
            user = user.get()

        if request.POST['action'] == '1':

            user.is_superuser = True

            user.save()

        elif request.POST['action'] == '2':

            user.is_superuser = False

            user.save()

        else:
            return HttpResponse(json.dumps({'key': '0', 'msg': 'Invalid Action Values!'}))

        return HttpResponse(json.dumps({'key': '1', 'msg': 'User Record Updated!'}))
