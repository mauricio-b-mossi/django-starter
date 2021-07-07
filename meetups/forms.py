from django import forms
from django.db.models.fields import EmailField

# from .models import Participant

"""class RegistrationForm(forms.ModelForm):
    # we specify to what model connect the form
    # Methods are referenced as properties in the template 
        class Meta:
        model = Participant
        # fields that should be filled
        fields = ["email"]"""

class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Your email')
