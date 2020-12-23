from django.urls import include, path

urlpatterns = [
    path("management/", include("pagelets.urls.management")),
    path("/", include("pagelets.urls.content")),
]
