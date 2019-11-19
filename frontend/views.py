from django.shortcuts import render
from admin.homepage.models import Homepage
# Create your views here.


def index(request):

    if request.user.is_authenticated:
        data = Homepage.objects.order_by('-id')
        return render(request, 'frondendTemplates/home/index.html', {'data': data})

    return render(request, 'frondendTemplates/home/index.html')


def signup(request):

    return render(request, 'frondendTemplates/signup/index.html')
