from django.conf import settings


CONTENT_AREAS = getattr(settings, 'PAGELET_CONTENT_AREAS', (
    ('main', 'Main'),
))
CONTENT_AREA_DEFAULT = getattr(settings, 'PAGELET_CONTENT_AREA_DEFAULT', 'main')

CONTENT_TYPES = getattr(settings, 'PAGELET_CONTENT_TYPES', (
    ('html', 'HTML',
     (),
     {},),
    ('markdown', 'Markdown',
     (),
     {},),
    ('wymeditor', 'WYMeditor',
     ('wymeditor/jquery.wymeditor.js',),
     {},),
    ('textile', 'Textile',
     (),
     {},),
)) + getattr(settings, 'PAGELET_CONTENT_TYPES_EXTRA', ())
CONTENT_TYPE_CHOICES = tuple((c[0], c[1]) for c in CONTENT_TYPES)
CONTENT_TYPE_DEFAULT = getattr(settings, 'PAGELET_CONTENT_TYPE_DEFAULT', 'html')

try:
    ATTACHMENT_PATH = settings.PAGELET_ATTACHMENT_PATH
except AttributeError:
    ATTACHMENT_PATH = getattr(settings, 'PAGE_ATTACHMENT_PATH', 'attachments/pages/')

# settings.PAGELET_TEMPLATE_TAGS is a list of template tag names that
# will load before each pagelet is rendered, allowing custom template
# tags to be included without including {% load <template_tag> %}
tags = set(['pagelet_tags'])
if hasattr(settings, 'PAGELET_TEMPLATE_TAGS'):
    for tag in settings.PAGELET_TEMPLATE_TAGS:
        tags.add(tag)
AUTO_LOAD_TEMPLATE_TAGS = '{%% load %s %%}' % ' '.join(tags)

BASE_TEMPLATES = getattr(settings, 'PAGELET_BASE_TEMPLATES', [])
BASE_TEMPLATE_DEFAULT = getattr(settings, 'PAGELET_BASE_TEMPLATE_DEFAULT', None)
INLINE_PAGELET_EXTRA = getattr(settings, 'PAGELET_INLINE_PAGELET_EXTRA', 0)
INLINE_SHARED_EXTRA = getattr(settings, 'PAGELET_INLINE_SHARED_EXTRA', 0)
INLINE_ATTACHMENT_EXTRA = getattr(settings, 'PAGELET_INLINE_ATTACHMENT_EXTRA', 0)
