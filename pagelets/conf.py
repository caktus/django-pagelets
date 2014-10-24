from django.conf import settings


CONTENT_AREAS = getattr(settings, 'PAGELET_CONTENT_AREAS', (
    ('main', 'Main'),
))

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

try:
    ATTACHMENT_PATH = settings.PAGELET_ATTACHMENT_PATH
except AttributeError:
    ATTACHMENT_PATH = getattr(settings, 'PAGE_ATTACHMENT_PATH', 'attachments/pages/')

try:
    settings.PAGELET_CONTENT_DEFAULT
except AttributeError:
    settings.PAGELET_CONTENT_DEFAULT = 'html'

# settings.PAGELET_TEMPLATE_TAGS is a list of template tag names that
# will load before each pagelet is rendered, allowing custom template
# tags to be included without including {% load <template_tag> %}
tags = set(['pagelet_tags'])
if hasattr(settings, 'PAGELET_TEMPLATE_TAGS'):
    for tag in settings.PAGELET_TEMPLATE_TAGS:
        tags.add(tag)
AUTO_LOAD_TEMPLATE_TAGS = '{%% load %s %%}' % ' '.join(tags)

BASE_TEMPLATES = getattr(settings, 'PAGELET_BASE_TEMPLATES', [])

PAGELET_TYPES = list(getattr(settings, 'PAGELET_ADDITIONAL_PAGELET_TYPES', ())) + [
    'pagelets.InlinePagelet',
    'pagelets.SharedPagelet',
]
