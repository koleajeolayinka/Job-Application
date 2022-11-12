from django.shortcuts import render
from subscribe.models import Subscribe
from subscribe.forms import SubscribeForm

# Create your views here.
def subscribe(request):
    subscribe_forms = SubscribeForm()
    email_error_empty = ''
    
    if request.POST:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        print('POST REQUEST : ', email)

        if email == '':
            email_error_empty = 'Email is not entered'

        subscribe = Subscribe(first_name=firstname, last_name=lastname, email=email)
        subscribe.save()
    context = {'form': subscribe_forms, 'email_error_empty': email_error_empty}
    return render(request, "subscribe/subscribe.html", context)
