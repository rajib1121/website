from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'frontend/index.html', {

    })


def about(request):
    return render(request, 'frontend/about.html', {

    })


def contact(request):
    return render(request, 'frontend/contact.html', {

    })


def gallery(request):
    return render(request, 'frontend/gallery.html', {

    })


def services(request):
    return render(request, 'frontend/services.html', {

    })
