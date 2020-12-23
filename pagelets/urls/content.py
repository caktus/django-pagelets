from django.urls import re_path

from pagelets import views
from pagelets.validators import PAGE_SLUG_RE

urlpatterns = [
    re_path(
        r"^(?P<page_slug>%s)/$" % PAGE_SLUG_RE,
        views.view_page,
        name="view_page",
    ),
]
