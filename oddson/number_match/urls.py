from django.conf.urls import patterns, include, url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.Resources.as_view(), name='index'),
    url(r'^number-match/$', views.GameListView.as_view(), name='list'),
    url(r'^number-match/(?P<id>\d+)/$', views.GameView.as_view(), name='detail'),
    url(r'^number-match/(?P<game_id>\d+)/attempt/$', views.AttemptListView.as_view(), name='attempt_list'),
    url(r'^number-match/(?P<game_id>\d+)/attempt/(?P<id>\d+)/$', views.AttemptView.as_view(), name='attempt_detail'),
)
