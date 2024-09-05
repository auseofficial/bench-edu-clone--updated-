from django.contrib import admin
from .models import Session, Version, Section

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('session_code', 'session', 'institution', 'branch', 'status', 'created_by_display', 'created_at')
    search_fields = ('session_code', 'session', 'institution', 'branch')
    list_filter = ('status', 'created_at', 'institution', 'branch')

    def created_by_display(self, obj):
        return obj.created_by.username if obj.created_by else None
    created_by_display.short_description = 'Created By'

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('version_code', 'version', 'status', 'created_at', 'updated_by_display', 'updated_at')
    search_fields = ('version_code', 'version')
    list_filter = ('status', 'created_at', 'updated_at')

    def updated_by_display(self, obj):
        return obj.updated_by.username if obj.updated_by else None
    updated_by_display.short_description = 'Updated By'

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('section_code', 'section', 'institution', 'branch', 'status', 'created_at')
    search_fields = ('section_code', 'section', 'institution', 'branch')
    list_filter = ('status', 'created_at')
