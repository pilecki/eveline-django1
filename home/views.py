from django.shortcuts import render
from django.core.mail import send_mail


def index(request):

    """ A view for index page"""

    if request.method == 'POST':
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        phone_number = request.POST['phone-number']
        message = request.POST['message']

    # sending email
        send_mail(
           'A person ' + first_name + ' ' + last_name
           + ' with phone number: ' + phone_number
           + ' sent you a message.',  # subject
           message,  # message
           'example@gmail.com',
           ['test@poj.com']
           )

    return render(request, 'home/index.html')
