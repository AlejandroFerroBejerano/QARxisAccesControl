from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import json
from .models import Event, Intercom, ActionCommand, Door, AccessCode, Route, Person, Location
from .models import User
from django.db import models

# Create your views here.
@login_required(login_url="/login/")
def index(request):
  return render(request, 'index.html')

@login_required(login_url="/login/")
def event_log(request):
	return render(request, 'event_log.html')

#Views od serialized models for her representation in AngularJS
@login_required(login_url="/login/")
def get_dataset(request, dataset):
    model = {'events':models.Event}[dataset]
    objects = [m.marshallable() for m in model.objects.all()]
    data = json.dumps(objects)
    return HttpResponse(data)

@login_required(login_url="/login/")
def profile(request, username):
  msg = ""
  current_user = request.user
  if current_user.username != username:
    msg = 'Only the administrator can access the profile of other users'
  user = User.objects.get(username = current_user.username)
  return render(request, 'profile.html', {'username':user.username, 'msg': msg})

# Login/Logout
from django import forms
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout


def login_view(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(username = username, password = password)
      print(user)
      if user is not None:
        if user.is_active:
          login(request, user)
          return HttpResponseRedirect('/')
        else:
          state = "AccDisabled"
          msg = "This account has been disabled, please provide the credentials of another account or contact your system administrator"
          print(state)
      else:
        state = "BadUsrPass"
        msg = "The username or password provided were incorrect, please enter a valid username and password"
        print(state)
    else:
        state = "EmptyForm"
        msg = "The username and password fields can not be empty, please provide a valid username and password"
        print (state)
  else:
    state =''
    msg = ''
    form = LoginForm()
    # return render (request, 'login.html', {'login_form': form})
  context = {'state': state, 'msg': msg, 'login_form': form}
  return render (request, 'login.html', context)

def logout_view(request):
  logout(request)
  return HttpResponseRedirect('/')

#API Views
from QARxisApp.models import Event, Intercom, ActionCommand, Door, AccessCode, Route, Person, Location
from QARxisApp.serializers import EventSerializer, IntercomSerializer, DoorSerializer, RouteSerializer, ActionCommandSerializer, AccessCodeSerializer, PersonSerializer, LocationSerializer
from rest_framework import generics, permissions, viewsets
from django_filters.rest_framework import DjangoFilterBackend


#Intercom
class IntercomAPIList(generics.ListCreateAPIView):
  queryset = Intercom.objects.all()
  serializer_class = IntercomSerializer
  filter_backends = (DjangoFilterBackend,)
  filter_fields = ('__all__')

class IntercomAPIDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Intercom.objects.all()
  serializer_class = IntercomSerializer

#Door
class DoorAPIList(generics.ListCreateAPIView):
  queryset = Door.objects.all()
  serializer_class = DoorSerializer
  filter_backends = (DjangoFilterBackend,)
  filter_fields = ('__all__')

class DoorAPIDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Door.objects.all()
  serializer_class = DoorSerializer

#Route
class RouteAPIList(generics.ListCreateAPIView):
  queryset = Route.objects.all()
  serializer_class = RouteSerializer
  filter_backends = (DjangoFilterBackend,)
  filter_fields = ('__all__')

class RouteAPIDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Route.objects.all()
  serializer_class = RouteSerializer

#ActionCommand
class ActionCommandAPIList(generics.ListCreateAPIView):
  queryset = ActionCommand.objects.all()
  serializer_class = ActionCommandSerializer
  filter_backends = (DjangoFilterBackend,)
  filter_fields = ('__all__')

class ActionCommandAPIDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = ActionCommand.objects.all()
  serializer_class = ActionCommandSerializer

#AccessCode
class AccessCodeAPIList(generics.ListCreateAPIView):
  queryset = AccessCode.objects.all()
  serializer_class = AccessCodeSerializer
  filter_backends = (DjangoFilterBackend,)
  filter_fields = ('__all__')

class AccessCodeAPIDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = AccessCode.objects.all()
  serializer_class = AccessCodeSerializer

#Person
class PersonAPIList(generics.ListCreateAPIView):
  queryset = Person.objects.all()
  serializer_class = PersonSerializer
  filter_backends = (DjangoFilterBackend,)
  filter_fields = ('__all__')

class PersonAPIDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Person.objects.all()
  serializer_class = PersonSerializer

#Location
class LocationAPIList(generics.ListCreateAPIView):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer
  filter_backends = (DjangoFilterBackend,)
  filter_fields = ('__all__')

class LocationAPIDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer

#EVENT
class EventAPIList(generics.ListCreateAPIView):
  queryset = Event.objects.all()
  serializer_class = EventSerializer
  filter_backends = (DjangoFilterBackend,)
  filter_fields = ('__all__')


class EventAPIDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Event.objects.all()
  serializer_class = EventSerializer

# Create your views here.
