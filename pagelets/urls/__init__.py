from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^content/', include('pagelets.urls.content')),
    url(r'^management/', include('pagelets.urls.management')),
)
