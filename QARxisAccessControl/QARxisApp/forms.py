from datetime import datetime
from django import forms

from .models import Event, Intercom, ActionCommand, Door, AccessCode, Route, Person, Location

class IntercomForm(forms.ModelForm):
  class Meta:
    model = Intercom
    fields = '__all__'

class ActionCommandForm(forms.ModelForm):
  class Meta:
    model = ActionCommand
    fields = '__all__'

class DoorForm(forms.ModelForm):
  class Meta:
    model = Door
    fields = '__all__'

class AccessCodeForm(forms.ModelForm):
  class Meta:
    model = AccessCode
    fields = '__all__'

class PersonForm(forms.ModelForm):
  class Meta:
    model = Person
    fields = '__all__'

class LocationForm(forms.ModelForm):
  class Meta:
    model = Location
    fields = '__all__'

class RouteForm(forms.ModelForm):
  class Meta:
    model = Route
    fields = '__all__'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class LoginForm(forms.Form):
  username = forms.CharField(label = 'Username', max_length=64)
  password = forms.CharField(widget=forms.PasswordInput())
