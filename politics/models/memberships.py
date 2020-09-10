from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import Item
from places.models import Country
from .organizations import InternationalOrganization


class InternationalOrganizationMemberships(models.Model):
    """"""
    MEMBERSHIPTYPES = (
        ('M', 'Member'),
        ('O', 'Observer'),
        ('T', 'Temporary'),
        ('AA', 'Approval'),
        ('AP', 'Acceptance'),
        ('AS', 'Accession'),
        ('SU', 'Succession'),
        ('R', 'Ratification'),
    )

    country = models.ForeignKey(
        Country, on_delete=models.CASCADE,
        related_name='membershipinternationalorganizations',
        verbose_name='country')
    organization = models.ForeignKey(
        InternationalOrganization, on_delete=models.CASCADE,
        related_name='membershipinternationalorganizations',
        verbose_name='organization')
    membership_type = models.CharField(
        _('type'), max_length=2, default='M', choices=MEMBERSHIPTYPES)
    started_at = models.DateField(
        _('started at'), blank=True, null=True)
    ended_at = models.DateField(
        _('ended at'), blank=True, null=True)

    item = GenericRelation(Item)
