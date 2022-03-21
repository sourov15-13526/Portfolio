from django.shortcuts import render 
from . import views 

def deshboard(request):
    return render(request, 'home.html')
def home(request): 
    return render(request, 'home.html') 
def blog(request): 
    return render(request, 'blog.html') 
def about(request): 
    return render(request, 'about.html') 
def contact(request): 
    return render(request, 'contact.html')