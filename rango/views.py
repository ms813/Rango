from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("<a href='about'>Hello rango!</a>")

def about(request):
    return HttpResponse("About page");
