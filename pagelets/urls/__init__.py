from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^management/', include('pagelets.urls.management')),
    url(r'^', include('pagelets.urls.content')),
)
