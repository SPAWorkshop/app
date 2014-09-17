from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
import accounts.urls


urlpatterns = patterns('',
    url(r'^api/auth/', include(accounts.urls)),
    url(r'^api/sessions/(?P<pk>\d+)', 'talks.views.session_detail', name='session-detail'),
    url(r'^api/sessions', 'talks.views.session_list', name='session-list'),
    url(r'^api/talks/(?P<pk>\d+)', 'talks.views.talk_detail', name='talk-detail'),
    url(r'^api/talks', 'talks.views.talk_list', name='talk-list'),
)
