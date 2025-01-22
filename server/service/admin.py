from django.contrib import admin
from service.models import BackupModel


class BackupModelAdmin(admin.ModelAdmin):
    list_display = ( 'uuid','service', 'created_at', 'file')
    search_fields = ('service', 'created_at')
    list_filter = ('service', 'created_at')
    readonly_fields = ('uuid', 'created_at')
    fieldsets = (
        (None, {
            'fields': ( 'uuid','service', 'file', 'created_at')
        }),
    )



admin.site.register(BackupModel, BackupModelAdmin)