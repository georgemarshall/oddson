from django.conf.urls import patterns, include, url

from .views import (
    AttemptListView, AttemptView, GameListView, GameView, Resources
)


urlpatterns = patterns('',
    url(r'^$', Resources.as_view(), name='index'),
    url(r'^number-match/$', GameListView.as_view(), name='list'),
    url(r'^number-match/(?P<id>\d+)/$', GameView.as_view(), name='detail'),
    url(r'^number-match/(?P<game_id>\d+)/attempt/$', AttemptListView.as_view(), name='attempt_list'),
    url(r'^number-match/(?P<game_id>\d+)/attempt/(?P<id>\d+)/$', AttemptView.as_view(), name='attempt_detail'),
)
