from django.conf.urls import url
from welcome.views import index

urlpatterns = [
  url(
    regex=r'^$',
    view = index,
    name = 'index'
  ),
]