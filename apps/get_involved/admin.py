from django.contrib import admin
from .models import InvolvementOption, VolunteerApplication, Donation

@admin.register(InvolvementOption)
class InvolvementOptionAdmin(admin.ModelAdmin):
    list_display = ['title', 'option_type', 'order']
    list_editable = ['order']

@admin.register(VolunteerApplication)
class VolunteerApplicationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'county', 'status', 'submitted_at']
    list_filter = ['status', 'county']
    search_fields = ['full_name', 'email']

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'amount', 'currency', 'frequency', 'status', 'created_at']
    list_filter = ['status', 'frequency', 'currency']
    search_fields = ['full_name', 'email']