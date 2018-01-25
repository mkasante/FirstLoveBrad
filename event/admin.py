from django.contrib import admin
from event.models import Event
from event.models import EventType

from firstlove.helpers import admin_actions


class EventAdmin(admin.ModelAdmin):
    filter_by = ['event']
    list_display = ['event', 'date', 'attendance_count', 'first_timers_count', 'born_again_count']
    list_filter = ['event']
    list_per_page = 50
    order_by = ('event', 'attendance_count')
    search_fields = ('event__name', 'venue')
    actions = [admin_actions.export_to_csv]

class EventTypeAdmin(admin.ModelAdmin):
    filter_by = ['name']
    list_filter = ['name']
    list_per_page = 50
    order_by = ['name']
    search_fields = ['name']
    actions = [admin_actions.export_to_csv]    


admin.site.register(Event, EventAdmin)
admin.site.register(EventType, EventTypeAdmin)