from django.db import models
from django.utils.translation import gettext_lazy as _


class AddressModel(models.Model):
    """"""
    # address OR address1
    # address2 ?
    # city
    # subcountry
    # country


class SocialModel(models.Model):
    """"""
    linkedin = models.CharField(
        _('linkedin'), max_length=250, default='', blank=True)
    twitter = models.CharField(
        _('twitter'), max_length=250, default='', blank=True)
    facebook = models.CharField(
        _('facebook'), max_length=250, default='', blank=True)
    instagram = models.CharField(
        _('instagram'), max_length=250, default='', blank=True)
    youtube = models.CharField(
        _('youtube'), max_length=250, default='', blank=True)
    whatsapp = models.CharField(
        _('whatsapp'), max_length=250, default='', blank=True)
    skype = models.CharField(
        _('skype'), max_length=250, default='', blank=True)

    # badoo
    # mailru
    # vkontakte
    # qq
    # wechat
    # weibo

    class Meta:
        abstract = True


class ContactModel(AddressModel, SocialModel):
    """"""
    # phone OR phone1
    # phone2 ?
    # fax
    # email
    # website

    class Meta:
        abstract = True
