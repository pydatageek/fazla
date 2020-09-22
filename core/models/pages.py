from unidecode import unidecode

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from .base_02 import BaseContentStampedModel
from .base_03 import SeoBaseContentStampedModel


class Contact(BaseContentStampedModel):
    """"""
    name = models.CharField(
        _('subject'), max_length=245)
    content = models.TextField(
        _('content'))
    email = models.EmailField(
        _('email'), max_length=250)

    slug = models.SlugField(
        _('slug'), max_length=255, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))

        super().save(*args, **kwargs)
