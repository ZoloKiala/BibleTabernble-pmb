
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name = 'index'),
     path('team-members', views.team, name = 'team'),
     path('prayer-request', views.prayer, name = 'prayer'),
     path('announcements', views.announcement, name = 'announcements'),
     path('library', views.library, name = 'library'),
     path('gallery', views.gallery, name = 'gallery'),
     path('contact', views.contact, name = 'contact'),
     path('ministries', views.ministries, name = 'ministries'),
]
