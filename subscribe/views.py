from django.shortcuts import render, redirect
from django.urls import reverse

from subscribe.models import Subscribe
from subscribe.forms import SubscribeForm


# Create your views here.
def subscribe(request):
    subscribe_form = SubscribeForm()
    email_error_empty = ""

    if request.POST:
        # firstname = request.POST['firstname']
        # lastname = request.POST['lastname']
        # email = request.POST['email']
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
        #     print("POST REQUEST : ")
        #     print(subscribe_form.cleaned_data)
        #     print(subscribe_form.cleaned_data['email'])

        #     firstname = subscribe_form.cleaned_data['first_name']
        #     lastname = subscribe_form.cleaned_data['last_name']
        #     email = subscribe_form.cleaned_data['email']
        #     subscribe = Subscribe(first_name=firstname, last_name=lastname, email=email)
        #     subscribe.save()
            return redirect(reverse('thank_you'))

            # if email == '':
            #     email_error_empty = 'Email is not entered'

    context = {"form": subscribe_form, "email_error_empty": email_error_empty}
    return render(request, "subscribe/subscribe.html", context)


def thank_you(request):
    context = {}
    return render(request, 'subscribe/thank_you.html', context)
