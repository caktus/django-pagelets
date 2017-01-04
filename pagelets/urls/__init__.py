from django.conf.urls import include, url

urlpatterns = [
    url(r'^management/', include('pagelets.urls.management')),
    url(r'^', include('pagelets.urls.content')),
]
