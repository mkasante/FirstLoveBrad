from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from event.models import Event, EventType
import datetime, re, os, requests

# Create your views here.
@login_required
def index(request):
	now = datetime.datetime.now()
	events = Event.objects.all()
	event_types = EventType.objects.all()

	context = {
		'events': events,
		'event_types': event_types,
	}

	return render (request, 'all_events.html', context)


@login_required
def event_info(request, id):
	event = Event.objects.get(pk = id)

	context = {
		'event': event
	}

	return render (request, 'event_info.html', context)


# Partial
@login_required
def _list_event_by_date(request, start_date, end_date):
	pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")

	end_date2 = str(datetime.datetime.strptime(end_date, "%Y-%m-%d") + datetime.timedelta(days=1))

	if pattern.match(start_date) and pattern.match(end_date):
		events = Event.objects.filter(date__gte = start_date, date__lte = end_date2)
	else:
		events = Event.objects.all()

	context = {
		'events': events
	}

	return render (request, '_partial/event_data.html', context)

@login_required
def _list_event_by_type(request, event_type):

	try:
		event_name = EventType.objects.get(name__iexact = event_type).name
		events = Event.objects.filter(event__name__iexact = event_name)
	except:
		events = Event.objects.all()

	context = {
		'events': events
	}

	return render (request, '_partial/event_data.html', context)
