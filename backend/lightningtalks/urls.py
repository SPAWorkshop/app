from django.conf.urls import patterns
from django.conf.urls import url
from accounts import views as accounts_views
from talks import views as talks_views


urlpatterns = patterns('',
    url(r'^api/auth/register$', accounts_views.RegistrationView.as_view(),
        name='register'),
    url(r'^api/auth/login$', accounts_views.LoginView.as_view(),
        name='login'),
    url(r'^api/auth/me$', accounts_views.ProfileView.as_view(),
        name='profile'),
    url(r'^api/sessions/(?P<pk>\d+)$', talks_views.SessionRetrieveView.as_view(),
        name='session-detail'),
    url(r'^api/sessions$', talks_views.SessionListView.as_view(),
        name='session-list'),
    url(r'^api/talks/(?P<pk>\d+)$', talks_views.TalkUpdateDestroyView.as_view(),
        name='talk-detail'),
    url(r'^api/talks$', talks_views.TalkListCreateView.as_view(),
        name='talk-list'),
)
