from django.contrib.sitemaps import GenericSitemap

from pagelets.models import Page


class PageSiteMap(GenericSitemap):
    def __init__(self, priority=None, changefreq=None):
        info_dict = {
            'queryset': Page.objects.all(),
            'date_field': 'last_changed'
        }
        super(PageSiteMap, self).__init__(info_dict, priority, changefreq)
