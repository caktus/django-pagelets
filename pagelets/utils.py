from django.utils.text import Truncator


def truncate_html_words(value, num_words):
    """Truncate 'value' to num_words words, ignoring HTML tags."""
    return Truncator(value).words(num_words, html=True)
