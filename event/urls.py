from django.conf.urls import url

from event.views import index, event_info
from event.views import _list_event_by_date, _list_event_by_type



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
    regex=r'^_daterange/(?P<start_date>[\d/-]+)--(?P<end_date>[\d/-]+)/$',
    view = _list_event_by_date, name = '_list_event_by_date'
  ),

  url(
    regex=r'^_eventtype/(?P<event_type>[\w\s\d/-_\.,]+)/$',
    view = _list_event_by_type, name = '_list_event_by_type'
    )
]