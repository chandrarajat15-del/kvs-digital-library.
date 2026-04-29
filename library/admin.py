from django.contrib import admin
from .models import Resource

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    # We changed 'category' to 'resource_type' to match your model
    list_display = ('title', 'subject', 'class_level', 'resource_type')
    list_filter = ('class_level', 'resource_type', 'subject')
    search_fields = ('title', 'subject')