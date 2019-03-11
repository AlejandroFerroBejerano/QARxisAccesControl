from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

# Create your models here.
class ImageUploader(models.Model):
  description = models.CharField(max_length = 50)
  image = models.ImageField(upload_to='media/')

  def save(self, *args, **kwargs):
    url = self.image.url
    description = self.description
    img = Image(description= description, url= '/media/' + url)
    img.save()

  def __str__(self):
    return self.description

  def marshallable(self):
    return{
      'description': self.description,
      'url': self.image.url,
    }

class Image(models.Model):
  description = models.CharField(max_length = 50)
  url = models.CharField(max_length = 50)

  def __str__(self):
    return self.description

  def marshallable(self):
    return{
      'description': self.description,
      'url': self.url,
    }

class Sound(models.Model):
  description= models.CharField(max_length=100)
  # sound_file = FileField(upload_to='sounds', default='sound/default_sound.mp3')

  def __str__(self):
    return self.description

  def marshallable(self):
    return{
      'description': self.description,
    }

class State(models.Model):
  REJECTED = 0
  VALID = 1
  EXPIRED = 2
  UNKNOWN = 3

  name = models.CharField(max_length=50)
  description = models.CharField(max_length=100)
  image = models.ForeignKey(Image, on_delete=models.CASCADE,)
  sound = models.ForeignKey(Sound, on_delete=models.CASCADE,)
  color = models.PositiveSmallIntegerField(
          choices = (
            (REJECTED, "REJECTED"),
            (VALID, "VALID"),
            (EXPIRED, "EXPIRED"),
            (UNKNOWN, "UNKNOWN"),)
  )

  def __str__(self):
    return self.name

  def marshallable(self):
    return {
      'name': self.name,
      'description': self.description,
      'image': self.image.marshallable(),
      'sound': self.sound.marshallable(),
      'color': self.color,
    }

class Event(models.Model):

  timestamp = models.DateTimeField(auto_now_add=True)
  #kind = models.CharField(max_length = 10, default=None)
  description = models.CharField(max_length = 50, default=None, null=True)
  location = models.CharField(max_length = 50, default=None, null=True)
  #status = models.ManyToManyField(State)
  hwid = models.CharField(max_length=12, default=None, null=True)
  barcode = models.CharField(max_length=20, default=None, null=True)

  def get_date(self, timestamp):
    return str(timestamp).split(' ')[0]

  def get_time(self, timestamp):
    return str(timestamp).split(' ')[1].split('+')[0]

  def marshallable(self):
    return {
      'id': self.pk,
      'date': self.get_date(self.timestamp),
      'time': self.get_time(self.timestamp),
      'kind': self.kind,
      'description': self.description,
      'location': self.location,
      'status': self.status.marshallable(),
    }

  def __str__(self):
    retval = str(self.get_date(self.timestamp)) + '-' + str(self.get_time(self.timestamp)) + '-' + str(self.description)
    return retval

class Intercom(models.Model):
  name = models.CharField(max_length=50)
  address = models.GenericIPAddressField(default='192.168.1.10')
  macaddres = models.CharField(max_length=12, default=None, unique=True)
  description = models.CharField(max_length=100, default=None, null=True)

  def __str__(self):
    return self.name

class ActionCommand(models.Model):
    name = models.CharField(max_length=50)
    action_uri = models.CharField(max_length = 100, default=None, null=True)
    description = models.CharField(max_length = 100, default=None, null=True)

    def __str__(self):
        return self.name

class Door(models.Model):
    name = models.CharField(max_length=50)
    intercom = models.ForeignKey(Intercom, on_delete=models.CASCADE)
    actions_commands = models.ManyToManyField(ActionCommand)

    def __str__(self):
      return self.name

class AccessCode(models.Model):
    code = models.CharField(max_length=20, unique=True)
    active = models.BooleanField(default=True)
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()

    def get_date_valid_from(self, valid_from):
        return str(valid_from).split(' ')[0]

    def get_time_valid_from(self, valid_from):
        return str(valid_from).split(' ')[1].split('+')[0]

    def get_date_valid_until(self, valid_until):
        return str(valid_until).split(' ')[0]

    def get_time_valid_until(self, valid_until):
        return str(valid_until).split(' ')[1].split('+')[0]

    def __str__(self):
        return self.code

class Route(models.Model):
    name = models.CharField(max_length=50)
    access_code = models.ManyToManyField(AccessCode)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dni =  models.CharField(max_length = 9)
    access_code = models.ManyToManyField(AccessCode)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=50)
    intercoms = models.ManyToManyField(Intercom)

    def __str__(self):
        return self.name# Create your models here.
