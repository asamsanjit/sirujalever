from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
from .models import Video
# Create your views here.
def home(request):
    return render(request,'home.html')

def events(request):
    return render(request,'events.html', {'title': 'events'})

def blogs(request):
    context = {
        'posts': Blog.objects.all()
    }
    return render(request,'blogs.html', context)
       
def videos(request):
    context = {
        'posts': Video.objects.all()
    }
    return render(request,'videos.html', context)
       
def About (request):
    return render(request,'about.html', {'title': 'About'})
              