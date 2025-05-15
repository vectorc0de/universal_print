from django.contrib import admin
from django.apps import apps
from .models import PrinterOuts, Organization, Groupo


class PrinterOutsAdmin(admin.ModelAdmin):
    list_display = ('document_name', 'status')

    def status(self, obj):
        return "Error" if obj.job_status == 8210 else "Ok"


admin.site.register(PrinterOuts, PrinterOutsAdmin)


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Organization, OrganizationAdmin)


class GroupoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Groupo, GroupoAdmin)


all_models = apps.get_models()

for model in all_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

admin.site.site_header = 'SNO project'
