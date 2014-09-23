from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns('',
    url(r'^api/auth/register$', 'accounts.views.register', name='register'),
    url(r'^api/auth/login$', 'accounts.views.login', name='login'),
    url(r'^api/auth/me$', 'accounts.views.profile', name='profile'),
    url(r'^api/sessions/(?P<pk>\d+)$', 'talks.views.session_detail', name='session-detail'),
    url(r'^api/sessions$', 'talks.views.session_list', name='session-list'),
    url(r'^api/talks/(?P<pk>\d+)$', 'talks.views.talk_detail', name='talk-detail'),
    url(r'^api/talks$', 'talks.views.talk_list', name='talk-list'),
)
