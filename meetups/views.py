from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Meetup, Participant
from .forms import RegistrationForm

# Create your views here.


def index(request):
    # List
    # Object give us the ability to query data simplly
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.htm', {
        # Object key (same as props/typical json response)
        'meetups': meetups
    })

# add a param for slug
def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            # Django will auto parse the info and save it in DB
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                # stores email in participant URL
                 user_email = registration_form.cleaned_data['email']
                #  Check if there is no existing user already
                # returns a tupal
                # TODO: HERE THE OBJECT IS CREATED
                 participant, wasCreated = Participant.objects.get_or_create(email=user_email)
                 selected_meetup.participants.add(participant)
                 return redirect('confirm-registration')
                 

        return render(request, 'meetups/meetup-details.htm', {
                'meetup_found': True,
                'meetup': selected_meetup,
                'form': registration_form
        })

    except Exception as exc:
        # return HttpResponse("Error no page found")
        return render(request, 'meetups/meetup-details.htm', {
            'meetup_found': False,
        })

def confirm_registration(request):
    return render(request, 'meetups/registration-success.htm')
