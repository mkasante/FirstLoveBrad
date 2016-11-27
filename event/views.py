from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from event.models import Event, EventType
import datetime, re

def time_range(amount):
	lastxmonths = []

	for x in range (0, amount):
		latest = datetime.date.today() - datetime.timedelta((x*365/12))
		earliest = datetime.date.today() - datetime.timedelta(((x+1)*365/12)-1)
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


@login_required
def event_info(request, id):
	# date = datetime.datetime.strptime(date, '%d %b %Y').strftime('%Y-%m-%d')
	event = Event.objects.get(pk = id)

	context = {
		'event': event
	}

	return render (request, 'event_info.html', context)


# Partial
@login_required
def _list_event_by_date(request, start_date, end_date):
	pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")

	# try:
	start_date = datetime.datetime.strptime(start_date, '%d %b %Y').strftime('%Y-%m-%d')
	end_date = datetime.datetime.strptime(
		end_date, '%d %b %Y').strftime('%Y-%m-%d') #2016-10-29 

	if pattern.match(start_date) and pattern.match(end_date):
		events = Event.objects.filter(date__gte = start_date, date__lte = end_date)
	# else:
	# 	events = Event.objects.all()
	# except:
	# 		events = Event.objects.all()


	context = {
		'events': events
	}

	return render (request, '_partial/event_data.html', context)