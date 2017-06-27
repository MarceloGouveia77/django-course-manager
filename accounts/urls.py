from django.conf.urls import url, include
from django.contrib.auth.views import login as authLogin

urlpatterns = [
    url(r'^entrar/$', authLogin,
    {'template_name': 'accounts/login.html'},
    name='login'),
]