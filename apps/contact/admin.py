from django.contrib import admin
from .models import ContactSubmission, NewsletterSubscriber

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'inquiry_type', 'status', 'created_at']
    list_filter = ['status', 'inquiry_type']
    search_fields = ['full_name', 'email', 'subject']

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_active', 'subscribed_at']
    list_filter = ['is_active']
    search_fields = ['email']