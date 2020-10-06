from django.shortcuts import render


def index(request):
    """ A view for index page"""

    return render(request, 'home/index.html')
