from django.contrib import admin
from .models import Host


class HostAdmin(admin.ModelAdmin):
    list_display = (
        'ip',
        'port',
        'resource_type',
        'host_owner',
        'last_modified',
    )

    list_filter = (
        'ip',
        'port',
        'resource_type',
        'host_owner',
        'last_modified',

    )

    empty_value_display = '-пусто-'


admin.site.register(Host, HostAdmin)
