from django.shortcuts import render
from django.http import HttpResponse

# Each view exists as a series of individual functions.
def index(request):
    return HttpResponse("Rango says hey there partner!")
