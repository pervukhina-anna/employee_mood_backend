from django.contrib import admin

from .models import HelpType, NeedHelp


@admin.register(HelpType)
class HelpTypeAdmin(admin.ModelAdmin):
    fields = ('title', 'role')
    list_display = fields


@admin.register(NeedHelp)
class NeedHelpAdmin(admin.ModelAdmin):
    fields = ('created', 'sender', 'recipient', 'type', 'viewed')
    list_display = fields
    readonly_fields = ('created',)
