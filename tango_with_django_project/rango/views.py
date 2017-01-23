from django.shortcuts import render
from django.http import HttpResponse

# Each view exists as a series of individual functions.
def index(request):
    return HttpResponse("Rango says hey there partner!     <a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("Rango Says: Here is the about page.     <a href='/rango/'>Index</a>")
