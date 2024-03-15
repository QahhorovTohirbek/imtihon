from django.shortcuts import render
from . import models

def index(request):
    banner = models.Banner.objects.last()
    about_us = models.About_us.objects.last()
    services = models.Service.objects.all()
    blogs = models.Blog.objects.all()
    contact = models.Contact.objects.all()
    context = {
        'banner':banner,
        'about_us':about_us,
        'services':services,
        'blogs':blogs,
        'contact':contact,
    }
    return render(request,'index.html',context)


def about_us(request):
    about_us = models.About_us.objects.last()
    context = {
        'about_us':about_us,
    }
    return render(request,'about.html',context)


def blog(request):
    blogs = models.Blog.objects.all()
    context = {
        'blogs':blogs,
    }
    return render(request,'blog.html',context)

def service(request):
    services = models.Service.objects.all()
    context = {
        'services':services,
    }
    return render(request,'service.html',context)

def contact(request):
    if request.method == 'POST':
        try:
            models.Contact.objects.create(
                name=request.POST['name'],
                phone=request.POST['phone'],
                email=request.POST['email'],
                body=request.POST['message']
            )
        except:
            ...
    return render(request, 'contact.html')

