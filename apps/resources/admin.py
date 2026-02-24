from django.contrib import admin
from .models import ResourceType, Resource

@admin.register(ResourceType)
class ResourceTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'resource_type', 'published_date', 'featured']
    list_filter = ['resource_type', 'featured', 'language']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'author']