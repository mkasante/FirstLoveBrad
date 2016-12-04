from django.conf.urls import url

from member.views import index, member_info, all_members  
from member.views import _list_members_by_alphabet, _list_members_by_status, _list_members_by_gender



urlpatterns = [
  url(
    regex=r'^$',
    view = index, name = 'index'
  ),

  url(
    regex=r'^all/$',
    view = all_members, name = 'all_members'
  ),

  url(
    regex=r'^(?P<name>[^\`]+)/$',
    view = member_info, name = 'member_info'
  ),


  # Partial views
  url(
    regex=r'^_group/(?P<alphabet>[a-zA-Z]+)$',
    view = _list_members_by_alphabet, name = '_list_members_by_alphabet'
  ),

  url(
    regex=r'^_status/(?P<status>[\w\s\d\.-_]+)$',
    view = _list_members_by_status, name = '_list_members_by_status'
  ),

  url(
    regex=r'^_gender/(?P<gender>[\w]+)$',
    view = _list_members_by_gender, name = '_list_members_by_gender'
  ),
  
]