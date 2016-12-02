from django.conf.urls import url
from welcome.views import index, _get_birthdays, _get_firsttimers, _get_evangelismlist

urlpatterns = [
  url(
    regex=r'^$',
    view = index,
    name = 'index'
  ),

  # 

  url(
    regex=r'^_newsfeed/birthdays/$',
    view = _get_birthdays,
    name = '_get_birthdays'
  ),

  url(
    regex=r'^_newsfeed/first-timers/$',
    view = _get_firsttimers,
    name = '_get_firsttimers'
  ),

  url(
    regex=r'^_newsfeed/evangelism/$',
    view = _get_evangelismlist,
    name = '_get_evangelismlist'
  ),


]
