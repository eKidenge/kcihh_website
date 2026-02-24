from django.contrib import admin
from .models import WorkCategory, FocusArea, Program, SuccessStory

@admin.register(WorkCategory)
class WorkCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_type']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(FocusArea)
class FocusAreaAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'order']
    list_editable = ['order']

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']

@admin.register(SuccessStory)
class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'person_name', 'featured']
    list_filter = ['featured', 'category']