from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def show(request):
    return render(request, 'show.html')

def home(request):
    return render(request, 'home.html')