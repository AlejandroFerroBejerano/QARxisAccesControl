from django.contrib import admin
from .models import Event, Intercom, ActionCommand, Door, AccessCode, Route, Person, Location, Image, Sound, State, ImageUploader

# Register your models here.
admin.site.register(Intercom)
admin.site.register(ActionCommand)
admin.site.register(Door)
admin.site.register(AccessCode)
admin.site.register(Route)
admin.site.register(Person)
admin.site.register(Location)
admin.site.register(Event)
admin.site.register(Image)
admin.site.register(ImageUploader)
admin.site.register(Sound)
admin.site.register(State)
