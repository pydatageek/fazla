from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from core.admin import BaseAdmin
from .models import (
    InternationalOrganization, LocalOrganization,
    InternationalOrganizationMemberships)
from .resources import (
    InternationalOrganizationResource, LocalOrganizationResource,
    InternationalOrganizationMemberships)


# @admin.register(Organization)
# class OrganizationAdmin(BaseAdmin, ImportExportModelAdmin):
#     """"""
#     resource_class = OrganizationResource


@admin.register(InternationalOrganization)
class InternationalOrganizationAdmin(BaseAdmin, ImportExportModelAdmin):
    """"""
    resource_class = InternationalOrganizationResource


@admin.register(LocalOrganization)
class LocalOrganizationAdmin(BaseAdmin, ImportExportModelAdmin):
    """"""
    resource_class = LocalOrganizationResource


@admin.register(InternationalOrganizationMemberships)
class InternationalOrganizationMembershipsAdmin(ImportExportModelAdmin):
    """"""
    resource_class = InternationalOrganizationResource
