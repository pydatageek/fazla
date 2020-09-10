"""Project-wide base models inherited by other models"""

from unidecode import unidecode

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from crum import get_current_user

from ..utils import random_chars

User = settings.AUTH_USER_MODEL


class StampedModel(models.Model):
    """an abstract model with
    added_at, added_by and updated_at, updated_by fields
    """
    added_at = models.DateTimeField(
        _('added date'), editable=False)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, blank=True, default=None,
        related_name='%(app_label)s_%(class)s_adders',
        verbose_name=_('added by'),
        help_text=_('User who added the db record.'))

    updated_at = models.DateTimeField(
        _('updated date'), editable=False, blank=True, null=True)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, blank=True, default=None,
        related_name='%(app_label)s_%(class)s_modifiers',
        verbose_name=_('updated by'),
        help_text=_('User who updated the db record.'))

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if self._state.adding:
            self.added_by = user
            self.added_at = timezone.now()
        else:
            self.updated_by = user
            self.updated_at = timezone.now()
        self.full_clean()
        super().save(*args, **kwargs)


class NameSlugModel(models.Model):
    """name and automatically created slug fields"""
    name = models.CharField(
        _('name'), max_length=245, unique=True)
    slug = models.SlugField(
        _('slug'), max_length=255, blank=True, unique=True, db_index=True)

    unique_code = models.CharField(
        _('unique code'), max_length=9, default='', blank=True,
        unique=True, db_index=True)

    code = models.CharField(
        _('code'), max_length=250, default='', blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """slug is created once at the creation of object,
        unidecode converts the non-english letters to english ones.
        """
        class_short_name = self.__class__.__name__.lower()[:6:2]
        class_short_name = class_short_name.strip()
        len_csn = len(class_short_name)
        if not self.slug:
            self.slug = slugify(unidecode(self.name))
        if not self.unique_code:
            self.unique_code = class_short_name + random_chars(9-len_csn)
        # self.slug += f'-{self.unique_code}'

        super().save(*args, **kwargs)

    @cached_property
    def url_slug_chars(self):
        # count = self.extra_chars_count
        # if count:
        #     return f'{self.slug}-{random_chars(count)}'
        # return f'{self.slug}-{self.unique_code}'
        return f'{self.slug}'

    @cached_property
    def url_slug_code(self):
        if self.code:
            return f'{self.slug}-{self.code}'
        else:
            return f'{self.slug}'

    @cached_property
    def url_slug_id(self):
        return f'{self.slug}-{self.id}'


class ContentModel(models.Model):
    """"""
    short_content = models.TextField(
        _('short content'), max_length=250, default='', blank=True,
        help_text=_('you can give short information.'))
    content = models.TextField(
        _('content'), default='', blank=True)

    class Meta:
        abstract = True


class SeoModel(models.Model):
    """"""
    meta_title = models.CharField(
        _('meta title'), max_length=245,
        unique=True, db_index=True)
    meta_description = models.CharField(
        _('meta description'), max_length=245, default='', blank=True)

    # meta_author
    # meta_keywords

    class Meta:
        abstract = True
