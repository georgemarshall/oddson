from django.conf.urls import patterns, include, url

from .views import (
    AttemptListView, AttemptView, ContractListView, ContractView, Resources
)


urlpatterns = patterns('',
    url(r'^$', Resources.as_view(), name='index'),
    url(r'^contract/$', ContractListView.as_view(), name='contract_list'),
    url(r'^contract/(?P<id>\d+)/$', ContractView.as_view(), name='contract_detail'),
    url(r'^contract/(?P<contract_id>\d+)/attempt/$', AttemptListView.as_view(), name='attempt_list'),
    url(r'^contract/(?P<contract_id>\d+)/attempt/(?P<id>\d+)/$', AttemptView.as_view(), name='attempt_detail'),
)
