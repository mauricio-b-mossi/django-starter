from django.contrib import admin

from .models import Meetup, Location, Participant

# Register your models here.
# granting access to models

class MeetupAdmin(admin.ModelAdmin):
    # defining fields/colums
    # only can call actuall info from the schema
    list_display = ('title', 'date', 'location')
    list_filter = ('location', 'date')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)


