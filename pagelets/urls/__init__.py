from django.conf.urls import include, patterns, url

urlpatterns = patterns('',
    url(r'^management/', include('pagelets.urls.management')),
    url(r'^', include('pagelets.urls.content')),
)
