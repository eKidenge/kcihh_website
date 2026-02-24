from django.contrib import admin
from .models import Category, Post, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_type']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'published_date', 'featured']
    list_filter = ['featured', 'published', 'category']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']
    date_hierarchy = 'published_date'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_date', 'approved']
    list_filter = ['approved']
    search_fields = ['name', 'email', 'content']