from django.conf.urls import patterns
from django.conf.urls import url, include
import talks.views

# TODO: TASK 1 - SESSION DETAILS
# - configure routing

urlpatterns = patterns('',
    url(r'^api/sessions$', talks.views.SessionListView.as_view()),
    url(r'^api/talks/(?P<pk>\d+)$', talks.views.TalkUpdateDestroyView.as_view()),
    url(r'^api/talks$', talks.views.TalkListCreateView.as_view()),
    url(r'^api/auth/', include('djoser.urls')),
)
