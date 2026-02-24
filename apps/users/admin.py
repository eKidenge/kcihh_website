from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'user_type', 'county', 'is_staff']
    list_filter = ['user_type', 'is_staff', 'is_superuser']
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('user_type', 'phone_number', 'profile_image', 'bio', 
                      'organization', 'position', 'county', 'country', 
                      'date_of_birth', 'website', 'linkedin', 'twitter',
                      'newsletter_opt_in', 'email_notifications'),
        }),
    )