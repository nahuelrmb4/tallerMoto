from django.shortcuts import render

def home(request):
    return render(request, 'taller/home.html')