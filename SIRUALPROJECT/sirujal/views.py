from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')

def events(request):
    return render(request,'events.html')

def blogs(request):
    return render(request,'blogs.html')
       
def videos(request):
    return render(request,'videos.html')
       
def About(request):
    return render(request,'about.html')
              