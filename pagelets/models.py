from datetime import datetime

from django.conf import settings
from django.db import models
from django.template import Template, TemplateSyntaxError
from django.urls import reverse
from django.utils.html import strip_tags
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager

from pagelets import conf, validators
from pagelets.utils import truncate_html_words

ORDER_CHOICES = [(x, x) for x in range(-10, 11)]


class PageletBase(models.Model):
    creation_date = models.DateTimeField(
        _("creation date"),
        auto_now_add=True,
        editable=False,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(app_label)s_%(class)s_created",
        editable=False,
        on_delete=models.CASCADE,
    )

    last_changed = models.DateTimeField(
        _("last changed"),
        auto_now=True,
        editable=False,
    )
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(app_label)s_%(class)s_last_modified",
        editable=False,
        on_delete=models.CASCADE,
    )

    def save(self, **kwargs):
        if not self.id:
            self.creation_date = datetime.now()
        self.last_changed = datetime.now()
        super(PageletBase, self).save(**kwargs)

    class Meta:
        abstract = True


class Page(PageletBase):
    title = models.CharField(
        _("title"),
        max_length=255,
        help_text=_(
            "The page title.  To be displayed in the browser's title "
            "bar as well as at the top of the page."
        ),
    )
    slug = models.CharField(
        _("slug"),
        unique=True,
        max_length=255,
        help_text=_(
            "A short string that uniquely identifies this page. "
            "It's used in the page "
            "URL, so don't change it unless you're positive nothing "
            "links to this page. Valid url chars include "
            "uppercase and lowercase letters, decimal digits, "
            "hyphen, period, underscore, and tilde. "
            "Do not include leading or trailing slashes."
        ),
        validators=[
            validators.validate_url_chars,
            validators.validate_leading_slash,
            validators.validate_trailing_slash,
        ],
    )
    description = models.TextField(
        _("description"),
        blank=True,
        help_text=_(
            "A description of the page for use in the meta tags and "
            "teaser or other short excepts"
        ),
    )
    base_template = models.CharField(
        _("base template"),
        max_length=255,
        blank=True,
        help_text=_(
            "Specify an alternative layout template to use for this "
            "page.  Clear the selection to use the default layout."
        ),
        default="pagelets/view_page.html",
    )
    meta_keywords = models.CharField(
        _("meta keywords"),
        max_length=200,
        help_text=_("A comma delineated list of keywords"),
        blank=True,
    )
    meta_robots = models.CharField(
        _("meta Robots"),
        max_length=20,
        blank=True,
        choices=[
            ("FOLLOW, INDEX", "FOLLOW, INDEX"),
            ("NOFOLLOW, NOINDEX", "NOFOLLOW, NOINDEX"),
            ("FOLLOW, NOINDEX", "FOLLOW, NOINDEX"),
            ("NOFOLLOW, INDEX", "NOFOLLOW, INDEX"),
        ],
    )

    tags = TaggableManager()

    def get_area_pagelets(self, area_slug, with_shared=True):
        """
        Combines and sorts the inline and shared pagelets for a given content
        area.  Pagelets without an order are given 0, so they show up
        in the middle.
        """
        pagelets = list(self.inline_pagelets.filter(area=area_slug))
        if with_shared:
            pagelets.extend(self.shared_pagelets.filter(area=area_slug))
        pagelets.sort(key=lambda a: a.order or 0)
        return pagelets

    def get_absolute_url(self):
        return reverse("view_page", kwargs={"page_slug": self.slug})

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title


class Pagelet(PageletBase):
    """
    Primary model for storing pieces of static content in the database.
    """

    # whenever you need to reference a pagelet in CSS, use its slug
    slug = models.CharField(
        _("slug"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "A short string with no spaces or special characters that "
            "uniquely identifies this pagelet.  It may be used to link "
            "to load this pagelet dynamically from other places on the "
            "site, so don't change it unless you're positive nothing "
            "depends on the current name."
        ),
    )
    css_classes = models.CharField(
        _("CSS classes"),
        max_length=255,
        blank=True,
        help_text=_(
            "Extra CSS classes, if any, to be added to the pagelet DIV " "in the HTML."
        ),
    )
    type = models.CharField(
        _("content type"),
        max_length=32,
        default="html",
        help_text=_(
            "Controls the markup language and, in some cases, the "
            "JavaScript editor to be used for this pagelet's content."
        ),
    )
    content = models.TextField(_("content"), blank=True)

    # a property that consistently gives you access to the real "Pagelet"
    # instance for Pagelets, InlinePagelets, and SharedPagelets
    real = property(lambda self: self)

    def render(self, context):
        # pagelets can automagically use pagelets templatetags
        # in order to remove boilerplate
        loaded_cms = conf.AUTO_LOAD_TEMPLATE_TAGS + self.content
        compiled = Template(loaded_cms).render(context)
        try:
            if self.type in ("html", "tinymce", "wymeditor"):
                html = compiled
            elif self.type == "textile":
                from textile import textile

                html = textile(str(compiled))
            elif self.type == "markdown":
                from markdown import markdown

                html = markdown(compiled)
            return html
        except TemplateSyntaxError as e:
            return "Syntax error, %s" % e

        raise Exception(
            "Unsupported template content type '%s'" % self.content.content_type
        )

    def save(self, *args, **kwargs):
        # force empty slugs to None so we don't get a DuplicateKey
        if self.slug == "":
            self.slug = None
        super(Pagelet, self).save(*args, **kwargs)

    class Meta:
        ordering = ("slug",)

    def __str__(self):
        if self.slug:
            return self.slug
        else:
            beginning = strip_tags(truncate_html_words(self.content, 5))
            if beginning:
                return beginning
            else:
                img_count = self.content.lower().count("<img")
                if img_count:
                    return "%s #%d (%s Images, no text)" % (
                        type(self).__name__,
                        self.id,
                        img_count,
                    )
                else:
                    return "%s #%d" % (
                        type(self).__name__,
                        self.id,
                    )


class PlacedPageletBase(models.Model):
    """
    Abstract base model with the common fields for the inline and shared
    pagelet models.
    """

    area = models.CharField(
        _("content area"),
        max_length=32,
        default="main",
        help_text=_("Specifies the placement of this pagelet on the page."),
    )
    order = models.SmallIntegerField(
        null=True,
        blank=True,
        choices=ORDER_CHOICES,
        help_text=_(
            "The order in which pagelets should show up on the page. "
            "Lower numbers show up first."
        ),
    )

    class Meta:
        abstract = True


class InlinePagelet(Pagelet, PlacedPageletBase):
    """
    A pagelet that shoes up on a single page.
    """

    page = models.ForeignKey(
        Page, related_name="inline_pagelets", on_delete=models.CASCADE
    )

    # a property that consistently gives you access to the real "Pagelet"
    # instance for Pagelets, InlinePagelets, and SharedPagelets
    real = property(lambda self: self)

    class Meta:
        ordering = ("order",)


class SharedPagelet(PlacedPageletBase):
    """
    A pagelet that may show up on multiple pages.
    """

    pagelet = models.ForeignKey(Pagelet, on_delete=models.CASCADE)
    page = models.ForeignKey(
        Page, related_name="shared_pagelets", on_delete=models.CASCADE
    )

    def __init__(self, *args, **kwargs):
        super(SharedPagelet, self).__init__(*args, **kwargs)
        self.__pagelet_dirty = False

    def _get_slug(self):
        return self.pagelet.slug

    def _set_slug(self, slug):
        self.__pagelet_dirty = True
        self.pagelet.slug = slug

    slug = property(_get_slug, _set_slug)

    def _get_css_classes(self):
        return self.pagelet.css_classes

    def _set_css_classes(self, css_classes):
        self.__pagelet_dirty = True
        self.pagelet.css_classes = css_classes

    css_classes = property(_get_css_classes, _set_css_classes)

    def _get_type(self):
        return self.pagelet.type

    def _set_type(self, type):
        self.__pagelet_dirty = True
        self.pagelet.type = type

    type = property(_get_type, _set_type)

    def _get_content(self):
        return self.pagelet.content

    def _set_content(self, content):
        self.__pagelet_dirty = True
        self.pagelet.content = content

    content = property(_get_content, _set_content)

    # a property that consistently gives you access to the real "Pagelet"
    # instance for Pagelets, InlinePagelets, and SharedPagelets
    real = property(lambda self: self.pagelet)

    def render(self, *args, **kwargs):
        return self.pagelet.render(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.__pagelet_dirty:
            self.pagelet.save()
            self.__pagelet_dirty = False
        return super(SharedPagelet, self).save(*args, **kwargs)

    class Meta:
        unique_together = (("pagelet", "page"),)
        ordering = ("order",)


class PageAttachment(models.Model):
    page = models.ForeignKey(Page, related_name="attachments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to=conf.ATTACHMENT_PATH)
    order = models.SmallIntegerField(
        null=True,
        blank=True,
        choices=ORDER_CHOICES,
    )

    class Meta:
        ordering = ("order",)

    def __str__(self):
        return self.name
