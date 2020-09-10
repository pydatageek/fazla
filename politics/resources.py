from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from places.models import Country
from .models import (
    InternationalOrganization, LocalOrganization,
    InternationalOrganizationMemberships)


# class OrganizationResource(resources.ModelResource):
#     """"""
#     class Meta:
#         model = Organization


class InternationalOrganizationResource(resources.ModelResource):
    """"""
    parent = fields.Field(
        attribute='parent',
        column_name='parent',
        widget=ForeignKeyWidget(InternationalOrganization, field='code')
    )

    class Meta:
        model = InternationalOrganization


class LocalOrganizationResource(resources.ModelResource):
    """"""
    class Meta:
        model = LocalOrganization


class InternationalOrganizationMembershipsResource(resources.ModelResource):
    """"""
    country = fields.Field(
        attribute='country',
        column_name='country',
        widget=ForeignKeyWidget(Country, field='iso2')
    )
    organization = fields.Field(
        attribute='organization',
        column_name='organization',
        widget=ForeignKeyWidget(InternationalOrganization, field='code')
    )

    class Meta:
        model = InternationalOrganizationMemberships
