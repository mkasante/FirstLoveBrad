from django.contrib import admin

# Register your models here.
from event.models import Event
from event.models import EventAdmin

from event.models import EventType
from event.models import EventTypeAdmin


admin.site.register(Event, EventAdmin)
admin.site.register(EventType, EventTypeAdmin)