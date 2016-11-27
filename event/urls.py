from django.conf.urls import url

from event.views import index, event_info
from event.views import _list_event_by_date



urlpatterns = [
  url(
    regex=r'^$',
    view = index, name = 'index'
  ),

  url(
    regex=r'^(?P<id>[\d]+)/$',
    view = event_info, name = 'event_info'
  ),

  # Partial views
  url(
    regex=r'^_daterange/(?P<start_date>[a-zA-Z\s\d/]+)-(?P<end_date>[a-zA-Z\s\d/]+)/$',
    view = _list_event_by_date, name = '_list_event_by_date'
  ),
]