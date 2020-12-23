from django.contrib import admin
from django.urls import include, path

admin.autodiscover()

urlpatterns = [
    path("pagelets/", include("pagelets.urls")),
    path("admin/", admin.site.urls),
]
