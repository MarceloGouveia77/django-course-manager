from django.conf.urls import include, url
from core.views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^contato/$', contact, name='contact'),
]