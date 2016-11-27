from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from event.models import Event, EventType
import datetime

def time_range(amount):
	lastxmonths = []

	for x in range (0, amount):
		latest = datetime.date.today() - datetime.timedelta(x*365/12)
		earliest = datetime.date.today() - datetime.timedelta((x+1)*365/12)
		lastxmonths.append((earliest, latest))

	return lastxmonths

# Create your views here.
@login_required
def index(request):
	now = datetime.datetime.now()
	events = Event.objects.all()
	event_types = EventType.objects.all()

	last12months = time_range(12)

	context = {
		'events': events,
		'event_types': event_types,
		'last12months': last12months
	}

	return render (request, 'all_events.html', context)