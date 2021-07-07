# TODO: HERE WE CONNECT THE URL TO THE FUNCTION
from django.urls import path
# From this folder pull views (which hold the response)
from . import views

# time 3:52:00

# TODO: PATH('url/, (views.handler), nameToBeReferred')

urlpatterns = [
    # /meetups, serve index
    # add slash (/) to avoid prob
    path('meetups/', views.index, name='all-meetups'),
    # instead of :id === <id>
    # slug: has to match slug fromat
    path('meetups/success', views.confirm_registration, name='confirm-registration'),
    path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-detail')
    
   
]