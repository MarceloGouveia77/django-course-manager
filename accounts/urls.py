from django.conf.urls import url, include
from django.contrib.auth.views import login as authLogin
from django.contrib.auth.views import logout as authLogout
from .views import register

urlpatterns = [
    url(r'^entrar/$', authLogin,
    {'template_name': 'accounts/login.html'},
    name='login'),

    url(r'^sair/$', authLogout,
    {'next_page': 'core:home'},
    name='logout'),
    
    url(r'^cadastre-se/$', register, name='register'),
]