from django.conf.urls import patterns
from django.conf.urls import url, include
from talks import views as talks_views


urlpatterns = patterns('',
    url(r'^api/sessions/(?P<pk>\d+)$', talks_views.SessionRetrieveView.as_view()),
    url(r'^api/sessions$', talks_views.SessionListView.as_view()),
    url(r'^api/talks/(?P<pk>\d+)$', talks_views.TalkUpdateDestroyView.as_view()),
    url(r'^api/talks$', talks_views.TalkListCreateView.as_view()),
    url(r'^api/auth/', include('djoser.urls')),
)
