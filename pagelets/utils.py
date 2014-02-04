
def truncate_html_words(value, num_words):
    """Backwords compatibility shim."""
    try:
        # Django 1.4+
        from django.utils.text import Truncator
    except ImportError:
        # Django 1.3
        from django.utils.text import truncate_html_words
        return truncate_html_words(value, num_words)
    else:
        return Truncator(value).words(num_words, html=True)
