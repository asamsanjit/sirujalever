from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home-page'),
    path('events',views.events, name='events-page'),
    path('blogs',views.blogs, name='blogs-page'),
    path('videos',views.videos, name='videos-page'),
    path('About',views.About, name='about-page'),

]