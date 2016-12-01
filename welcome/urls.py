from django.conf.urls import url
from welcome.views import index, _get_birthdays, _get_firsttimers, _get_evangelismlist
from welcome.views import __attendance_api, __member_api, __academin_institution_api, __event_api

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


# API
  url(
    regex=r'^__api/member/$',
    view = __member_api,
    name = '__member_api'
  ),

  url(
    regex=r'^__api/attendance/$',
    view = __attendance_api,
    name = '__attendance_api'
  ),

  url(
    regex=r'^__api/event/$',
    view = __event_api,
    name = '__event_api'
  ),

  url(
    regex=r'^__api/academic-institution/$',
    view = __academin_institution_api,
    name = '__academin_institution_api'
  ),

]
