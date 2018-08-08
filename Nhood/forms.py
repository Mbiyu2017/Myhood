from django.forms import ModelForm
from .models import *

class NeighbourhoodForm(ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['occupants','admin']

class BusinessForm(ModelForm):
    class Meta:
        model = Business
        exclude = ['owner']

class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = ['poster','nhood']
