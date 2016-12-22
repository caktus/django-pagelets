import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


PAGE_SLUG_RE = r'[-\w/\.~]+'


def validate_url_chars(value):
    if re.match(PAGE_SLUG_RE, value) is None:
        raise ValidationError(_(u"Enter a valid 'slug' consisting of valid url characters. "
                                u"These include uppercase and lowercase letters, decimal digits, "
                                u"hyphen, period, underscore, and tilde."), code=u'invalid')


def validate_leading_slash(value):
    if value.startswith('/'):
        raise ValidationError(_(u"Cannot start with a slash"), code=u'invalid')


def validate_trailing_slash(value):
    if value.endswith('/'):
        raise ValidationError(_(u"Cannot end with a slash"), code=u'invalid')
