from django.contrib import admin
from .models import Event, Intercom, ActionCommand, Door, AccessCode, Route, Person, Location, Image, Sound, State, ImageUploader

#ModelAdmin clases

class IntercomAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'description')

class ActionCommandAdmin(admin.ModelAdmin):
    list_display = ('name', 'action_uri', 'description')

class DoorAdmin(admin.ModelAdmin):
    list_display = ('name', 'intercom')

# Register your models here.
admin.site.register(Intercom, IntercomAdmin)
admin.site.register(ActionCommand, ActionCommandAdmin)
admin.site.register(Door, DoorAdmin)
admin.site.register(AccessCode)
admin.site.register(Route)
admin.site.register(Person)
admin.site.register(Location)
admin.site.register(Event)
admin.site.register(Image)
admin.site.register(ImageUploader)
admin.site.register(Sound)
admin.site.register(State)
