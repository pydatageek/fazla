from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import SeoBaseContentStampedModel, Item


class Info(SeoBaseContentStampedModel):
    """"""

    class Meta:
        verbose_name = _('Info')
        verbose_name_plural = _('Infos')

    def save(self, *args, **kwargs):
        if not self.meta_title:
            self.meta_title = f'{self.name}'

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('info-detail', args=['self.slug'])
