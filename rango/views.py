from django.shortcuts import render
from django.http import HttpResponse

# Each view exists as a series of individual functions.
def index(request):
    # Construct a dictionary to pass to the template engine as its context
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Crunchy, reamy, cookie, candy, cupcake!"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make out lives easier
    # Note that the first parameter is the template we wish to use.
    # return render(request, 'rango/index.html', context_dict)
    return render(request, 'rango/index.html', context=context_dict)
    #return HttpResponse("Rango says hey there partner!     <a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("Rango Says: Here is the about page.     <a href='/rango/'>Index</a>")
