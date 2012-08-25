from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'', include('number_match.urls', namespace='number_match')),
)