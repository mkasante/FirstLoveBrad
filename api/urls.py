from django.conf.urls import url
from api.views import MemberViewSet
from member.views import index, member_info, all_members  
from member.views import _sort_members_by_alphabet



urlpatterns = [
  url(
    regex=r'^$',
    view = MemberViewSet.as_view({'get': 'list'}), name = 'academicinstitution-detail'
  )
]