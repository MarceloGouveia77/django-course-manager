from django.conf.urls import url, include
from django.contrib.auth.views import login as authLogin
from django.contrib.auth.views import logout as authLogout
from .views import register, dashboard, edit, edit_password

urlpatterns = [
    url(r'^$', dashboard, name='dashboard'),
    url(r'^editar/$', edit, name='edit'),
    url(r'^editar-senha/$', edit_password, name='edit_password'),
    url(r'^entrar/$', authLogin,

    {'template_name': 'accounts/login.html'},
    name='login'),

    url(r'^sair/$', authLogout,
    {'next_page': 'core:home'},
    name='logout'),
    
    url(r'^cadastre-se/$', register, name='register'),
]