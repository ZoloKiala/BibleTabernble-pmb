from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request, 'index.html', {})

def team(request):
    
    return render(request, 'team-members.html', {})

def prayer(request):
    
    return render(request, 'prayer-request.html', {})

def announcement(request):
    
    return render(request, 'announcements.html', {})


def library(request):
    
    return render(request, 'library.html', {})

def gallery(request):
    
    return render(request, 'gallery.html', {})

def contact(request):
    
    return render(request, 'contact.html', {})

def ministries(request):
    
    return render(request, 'ministries.html', {})
