from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

# Each view exists as a series of individual functions.
def index(request):

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retreive the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary
    # that will be passed to the template engine
    category_list = Category.objects.order_by('-likes')[:5]

    # Construct a dictionary to pass to the template engine as its context
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'categories': category_list}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make out lives easier
    # Note that the first parameter is the template we wish to use.
    # return render(request, 'rango/index.html', context_dict)
    return render(request, 'rango/index.html', context_dict)
    #return HttpResponse("Rango says hey there partner!     <a href='/rango/about'>About</a>")

def about(request):
    context_dict = {'boldmessage': "This is the about page!"}
    return render(request, 'rango/about.html', context=context_dict)
    #return HttpResponse("Rango Says: Here is the about page.     <a href='/rango/'>Index</a>")
