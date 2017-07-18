from django.conf.urls import url
from . import views

urlpatterns = [
    # /client/
    url(r'^$', views.index_contact, name='index_contact'),
    # /client/13
    url(r'^(?P<client_id>[0-9]+)/$', views.detail_contact, name='detail_contact'),
]
