from django.conf.urls import include, url
from .views import index, details

urlpatterns = [
    url(r'^$', index, name='index'),
    #url(r'^(?P<pk>\d+)/$', details, name='details')
    url(r'^(?P<slug>[\w_-]+)/$', details, name='details')
]